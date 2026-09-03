from __future__ import annotations

import sqlite3
import unittest
from pathlib import Path
from unittest import mock

from search.paper_db import (
    fetch_usenix,
    has_reusable_sync,
    initialize,
    store_records,
)


CATALOG = Path(__file__).resolve().parents[1] / "venues.json"


class PaperDatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        initialize(self.connection, CATALOG)

    def tearDown(self) -> None:
        self.connection.close()

    def test_zero_sync_is_not_reusable(self) -> None:
        self.connection.execute(
            """INSERT INTO sync_run(
                   venue_id, year, started_at, finished_at, status, fetched_count
               ) VALUES ('conference/osdi', 2026, 'now', 'now', 'ok', 0)"""
        )
        self.assertFalse(has_reusable_sync(
            self.connection, "conference/osdi", 2026
        ))
        self.connection.execute(
            """INSERT INTO sync_run(
                   venue_id, year, started_at, finished_at, status, fetched_count
               ) VALUES ('conference/osdi', 2026, 'now', 'now', 'ok', 2)"""
        )
        self.assertTrue(has_reusable_sync(
            self.connection, "conference/osdi", 2026
        ))

    @mock.patch("search.paper_db.open_text")
    def test_usenix_parser(self, open_text: mock.Mock) -> None:
        open_text.return_value = """
        <article id="node-1" class="node node-paper view-mode-schedule">
          <h2><a href="/conference/osdi26/presentation/example">
            Example &amp; System
          </a></h2>
          <div class="field-name-field-paper-description-long">
            <p>First <em>abstract</em> paragraph.</p><p>Second paragraph.</p>
          </div>
        </article>
        """
        records = fetch_usenix(
            {"conference_slug": "osdi{yy}"}, 2026, "OSDI"
        )
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["info"]["title"], "Example & System")
        self.assertEqual(
            records[0]["info"]["abstract"],
            "First abstract paragraph. Second paragraph.",
        )
        self.assertEqual(records[0]["_source"], "official:usenix")

    def test_dblp_record_reconciles_official_record(self) -> None:
        official = {
            "_source": "official:usenix",
            "info": {
                "key": "official/usenix/osdi26/example",
                "title": "Example System.",
                "year": 2026,
                "venue": "OSDI",
                "url": "https://www.usenix.org/example",
            },
        }
        dblp = {
            "info": {
                "key": "conf/osdi/Example26",
                "title": "Example System",
                "year": 2026,
                "venue": "OSDI",
                "url": "https://dblp.org/rec/conf/osdi/Example26",
            },
        }
        with self.connection:
            store_records(self.connection, "conference/osdi", [official])
            store_records(self.connection, "conference/osdi", [dblp])
        rows = self.connection.execute(
            """SELECT p.dblp_record_key, p.metadata_source
               FROM paper p JOIN paper_venue pv ON pv.paper_id=p.id
               WHERE pv.venue_id='conference/osdi' AND p.year=2026"""
        ).fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["dblp_record_key"], "conf/osdi/Example26")
        self.assertEqual(rows[0]["metadata_source"], "dblp")

    def test_official_record_enriches_existing_dblp_record(self) -> None:
        dblp = {
            "info": {
                "key": "conf/fast/Example26",
                "title": "Generative File System.",
                "year": 2026,
                "venue": "FAST",
                "url": "https://dblp.org/rec/conf/fast/Example26",
            },
        }
        official = {
            "_source": "official:usenix",
            "info": {
                "key": "official/usenix/fast26/example",
                "title": "Generative File System",
                "abstract": "Uses LLM agents to generate a file system.",
                "year": 2026,
                "venue": "FAST",
                "url": "https://www.usenix.org/example",
            },
        }
        with self.connection:
            store_records(self.connection, "conference/fast", [dblp])
            store_records(self.connection, "conference/fast", [official])
        rows = self.connection.execute(
            """SELECT p.dblp_record_key, p.metadata_source, p.abstract
               FROM paper p JOIN paper_venue pv ON pv.paper_id=p.id
               WHERE pv.venue_id='conference/fast' AND p.year=2026"""
        ).fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["dblp_record_key"], "conf/fast/Example26")
        self.assertIn("official:usenix", rows[0]["metadata_source"])
        self.assertEqual(
            rows[0]["abstract"], "Uses LLM agents to generate a file system."
        )


if __name__ == "__main__":
    unittest.main()

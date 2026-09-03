# Agent for Systems 与系统自动化论文精筛示例（2024–2026）

> DeepSeek semantic run `22`; generated from the local CCF A/B paper database. Scores measure estimated topical relevance, not paper quality.

- Model: `deepseek-v4-flash`
- Topic: Strictly select papers whose primary research contribution directly automates the construction, evolution, or operation of computer systems or software infrastructure. Include AI/LLM agents, agentic AIOps/SRE, autonomous or self-managing systems, and automated methods for generating or evolving complete system-software components, or for configuring, tuning, scheduling, diagnosing, debugging, securing, repairing, and recovering databases, operating systems, distributed/cloud systems, networks, storage, compilers, and computer architecture. Require a concrete systems artifact, systems-management task, or infrastructure-automation contribution. Exclude generic multi-agent or reinforcement-learning applications, user/recommender agents, ordinary application code generation and general program repair, software-development assistants without a systems-software or systems-operation impact, LLM inference/serving optimizations without an agentic automation contribution, and automation in non-computing domains. Be conservative when evidence is only a title.
- Scope: categories `DS, SE, DB`, years `2024–2026`, source run `20`
- Threshold: `0.75`
- Screened: `296`; selected records: `127`; unique titles: `126`
- Evidence: `7` selected papers had cached abstracts; `119` were judged conservatively from titles.

## 2026 (48)

1. **[Sharpen the Spec, Cut the Code: A Case for Generative File System with SYSSPEC.](https://dblp.org/rec/conf/fast/LiuZZ0X026)** — FAST; `DS-A`; score `0.96`
   - Introduces SYSSPEC, an LLM-agent framework for generating and evolving a concurrent file system, directly automating construction and evolution of a core OS component.

2. **[An Agentic Framework for Triaging Incidents in Production Cloud Infrastructure.](https://dblp.org/rec/conf/sigsoft/YaoJMVDHBLC26)** — FSE; `SE-A`; score `0.95`
   - The paper proposes an agentic framework for automating incident triage in production cloud infrastructure, directly addressing systems operation and management.

3. **[Why Database Manuals Are Not Enough: Efficient and Reliable Configuration Tuning for DBMSs via Code-Driven LLM Agents.](https://dblp.org/rec/journals/pvldb/ZhangCHHLWSWZLLD26)** — VLDB; `DB-A`; score `0.95`
   - Directly automates DBMS configuration tuning using code-driven LLM agents, a concrete systems-management task.

4. **[Aloha: Localizing Batch Failures in Large-scale Cloud Systems via Contrast Analysis and Human-in-the-Loop Agent.](https://dblp.org/rec/conf/sigsoft/ZhangWRSGZLLZRB26)** — FSE; `SE-A`; score `0.90`
   - Directly automates failure localization in large-scale cloud systems via contrast analysis and an agentic human-in-the-loop approach.

5. **[CMA+DB: How to Automatically Tune Database Parameters Through Collaborative Multi-Agents.](https://dblp.org/rec/journals/tkde/QiaoTLGXHWYW26)** — TKDE; `DB-A`; score `0.90`
   - The paper directly addresses automatic tuning of database parameters using collaborative multi-agents, an infrastructure-automation task.

6. **[DBAIOps: A Reasoning LLM-Enhanced Database Operation and Maintenance System using Knowledge Graphs.](https://dblp.org/rec/journals/pvldb/ZhouSZZXZLW26)** — VLDB; `DB-A`; score `0.90`
   - The title explicitly describes an LLM-enhanced system for database operation and maintenance, directly targeting infrastructure automation.

7. **[Diagnosing Performance Issues in Application-Defined Resources](https://www.usenix.org/conference/osdi26/presentation/hu-yigong)** — OSDI; `SE-A`; score `0.90`
   - The paper presents gigiprofiler, an automated profiler that uses LLM-based inference and static analysis to diagnose performance bottlenecks in system software such as MariaDB, directly contributing to systems-operation and diagnosis automation.

8. **[ECO: An AI-Driven Code Efficiency Optimizer for Warehouse Scale Computers (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/lin-hannah)** — OSDI; `SE-A`; score `0.90`
   - ECO is a deployed AI-driven system that automatically localizes, optimizes, verifies, and ships production code-efficiency improvements in Google's hyperscale fleet, directly automating software-infrastructure evolution and operation.

9. **[Generative AI as an infrastructure copilot: automating Infrastructure-As-Code across the DevSecOps lifecycle.](https://dblp.org/rec/journals/ase/EspositoRBTL26)** — ASE; `SE-B`; score `0.90`
   - The title explicitly describes a generative AI copilot for automating Infrastructure-as-Code across the DevSecOps lifecycle, which directly contributes to automated construction and operation of software infrastructure.

10. **[Harmonia: Enhancing Data Placement and Migration in Hybrid Storage Systems via Multi-Agent Reinforcement Learning.](https://dblp.org/rec/conf/ics/NadigABSSKYSPM26)** — ICS; `DS-B`; score `0.90`
   - Proposes a multi-agent RL system for automating data placement and migration in hybrid storage, directly addressing storage-systems operation.

11. **[SMARTTalk: Teaching SMART Logs to Talk to LLMs](https://www.usenix.org/conference/osdi26/presentation/akewar)** — OSDI; `SE-A`; score `0.90`
   - Presents a concrete systems architecture that converts SSD SMART telemetry into LLM-reasoned failure prediction and health classification, directly supporting storage infrastructure operations.

12. **[SPADE: Signal-Aware DAG Scheduling and Dynamic Provisioning for Data Processing Clusters](https://www.usenix.org/conference/osdi26/presentation/lechowicz)** — OSDI; `SE-A`; score `0.90`
   - Presents SPADE, a concrete cluster scheduling and dynamic provisioning system that autonomously adapts data-processing DAGs to time-varying infrastructure signals.

13. **[This is Going to Sound Crazy, But What If We Used Large Language Models to Boost Automatic Database Tuning Algorithms By Leveraging Prior History? We Will Find Better Configurations More Quickly Than Retraining From Scratch!](https://dblp.org/rec/journals/pacmmod/ZhangLP26)** — SIGMOD; `DB-A`; score `0.90`
   - Directly targets automatic database configuration tuning using LLMs to leverage prior tuning history, a concrete systems-management task.

14. **[TrainMover: An Interruption-Resilient Runtime for ML Training](https://www.usenix.org/conference/osdi26/presentation/lao)** — OSDI; `SE-A`; score `0.90`
   - The paper presents TrainMover, a concrete runtime system that automatically handles interruptions and failure recovery for large-scale ML training, directly contributing to resilient operation of computing infrastructure.

15. **[kAPR: A coverage-guided, context-aware agent for automated repair of Linux kernel bugs.](https://dblp.org/rec/journals/infsof/LiYZLJ26)** — IST; `SE-B`; score `0.90`
   - Directly targets automated repair of Linux kernel bugs, a core operating-system infrastructure repair task.

16. **[Automated Repair of TEE Partitioning Issues via DSL-Guided and LLM-Assisted Patching.](https://dblp.org/rec/journals/pacmse/MaSHLLNL26)** — FSE; `SE-A`; score `0.85`
   - The paper directly addresses automated repair of TEE partitioning issues, a concrete system-software security and infrastructure task.

17. **[LLM-VeriOpt: Verification-Guided Reinforcement Learning for LLM-Based Compiler Optimization.](https://dblp.org/rec/conf/cgo/FangKRAM26)** — IEEE/ACM CGO; `DS-B`; score `0.85`
   - The paper directly targets compiler optimization using LLMs with verification-guided RL, a concrete systems-software infrastructure task.

18. **[Root-Cause Diagnosis with Remediation Recommendations for ETL Pipelines via LLM-Based Reasoning.](https://dblp.org/rec/conf/sigmod/VijaykeerthyCAS26)** — SIGMOD; `DB-A`; score `0.85`
   - Directly targets automated diagnosis and remediation for ETL pipelines, an infrastructure operation task.

19. **[RunbookFX: Type- and Effect-Safe LLM Synthesis for Executable Incident Diagnosis and Mitigation.](https://dblp.org/rec/journals/pacmpl/XiaoLG26)** — ICFP; `SE-B`; score `0.85`
   - The title indicates LLM-based synthesis of executable artifacts for incident diagnosis and mitigation, directly targeting automated systems operation and infrastructure management.

20. **[A Hierarchical GNN-Based Multi-Agent Framework for Workflow Scheduling in Hybrid Clouds Considering Privacy Constraints.](https://dblp.org/rec/journals/tsc/GuZLFZTC26)** — TSC; `SE-A`; score `0.80`
   - Directly addresses automated workflow scheduling in hybrid cloud systems, a concrete infrastructure-automation task, through a hierarchical multi-agent framework with privacy constraints.

21. **[An Agent Framework for Fault Recovery Planning Generation Based on Model Context Protocol.](https://dblp.org/rec/conf/iscas/YaoYWXWCZ26)** — ISCAS; `DS-B`; score `0.80`
   - The title describes an agent framework for generating fault recovery plans, directly addressing automated diagnosis and recovery of computer systems, which fits the requested infrastructure-automation scope.

22. **[CAP: Detecting Network Device Misconfigurations with Context-Aware Prompting of LLMs.](https://dblp.org/rec/journals/pomacs/JiangGF26)** — SIGMETRICS; `DS-B`; score `0.80`
   - The paper directly automates network device misconfiguration detection using LLMs, a systems-management task for network infrastructure.

23. **[CHIP-MAP: A Collaborative Optimization Framework for Macro Placement Using Large Language Models.](https://dblp.org/rec/conf/date/DuYYQTZGLWC26)** — DATE; `DS-B`; score `0.80`
   - Directly targets automated macro placement for chip design, an infrastructure-automation task in computer architecture using collaborative LLMs.

24. **[Can LLMs Hack Enterprise Networks? Autonomous Assumed Breach Penetration-Testing Active Directory Networks.](https://dblp.org/rec/journals/tosem/HappeC26)** — TOSEM; `SE-A`; score `0.80`
   - Autonomously conducts assumed-breach penetration testing of Active Directory enterprise networks, directly automating a security assessment task for infrastructure.

25. **[Compiler-Runtime Co-operative Chain of Verification for LLM-Based Code Optimization.](https://dblp.org/rec/conf/cgo/KwonSLYSKJLK26)** — IEEE/ACM CGO; `DS-B`; score `0.80`
   - The paper proposes an LLM-based code optimization method with compiler-runtime cooperative verification, directly targeting compiler system software optimization.

26. **[DevGen: Automated Generation of Virtual Device Models for Kernel Drivers via Large Language Models.](https://dblp.org/rec/conf/sigsoft/WangYLGWWLT26)** — FSE; `SE-A`; score `0.80`
   - Directly automates generation of kernel driver virtual device models, a concrete systems-software infrastructure component.

27. **[DrWASI: LLM-assisted Differential Testing for WebAssembly System Interface Implementations.](https://dblp.org/rec/journals/tosem/ZhangHGCLWMHL26)** — TOSEM; `SE-A`; score `0.80`
   - Directly automates differential testing to diagnose bugs in WASI implementations, a concrete system-software infrastructure automation task.

28. **[Effective Bug Detection in Graph Database Engines: An LLM-Based Approach.](https://dblp.org/rec/journals/tkde/WuWLLQW26)** — TKDE; `DB-A`; score `0.80`
   - Proposes an LLM-based method for automatically detecting bugs in graph database engines, which directly targets debugging a concrete software-infrastructure component.

29. **[Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers.](https://dblp.org/rec/journals/tsc/ZhaoWYLJ26)** — TSC; `SE-A`; score `0.80`
   - Proposes a multi-agent RL method for scheduling computing services in distributed data centers, directly targeting infrastructure operation.

30. **[Identifying performance-sensitive configurations in software systems with LLM-based agents.](https://dblp.org/rec/journals/ese/WangKC26)** — ESE; `SE-B`; score `0.80`
   - The paper applies LLM-based agents to identify performance-sensitive configurations, directly automating software system configuration analysis and tuning.

31. **[Integrating Multi-Agent Reinforcement Learning and XGBoost for Efficient Large-Scale Dynamic Workflow Scheduling in Cloud Environments.](https://dblp.org/rec/journals/tsc/DingZY26)** — TSC; `SE-A`; score `0.80`
   - The paper directly addresses automated workflow scheduling in cloud environments, which is a systems-management task for cloud infrastructure.

32. **[KernelEvolve: Scaling Agentic Kernel Coding for Heterogeneous AI Accelerators at Meta.](https://dblp.org/rec/conf/isca/LiaoQWGKYXAFHHJLLLMPSYY26)** — ISCA; `DS-A`; score `0.80`
   - Directly targets agentic automation of low-level kernel code for heterogeneous AI accelerators, a system-software/infrastructure task.

33. **[LLM Agents for AIOps in Kubernetes: An Industrial Experience Report with Red Hat OpenShift.](https://dblp.org/rec/conf/sigsoft/VituiC26)** — FSE; `SE-A`; score `0.80`
   - Directly addresses LLM agents for AIOps on Kubernetes, an explicit infrastructure-automation and systems-operation task.

34. **[LLM-Based Misconfiguration Detection for AWS Serverless Computing.](https://dblp.org/rec/journals/tosem/WenCZSLPW26)** — TOSEM; `SE-A`; score `0.80`
   - Directly targets automated detection of misconfigurations in AWS serverless infrastructure, a systems-management and security task.

35. **[MARL: A Multi-Agent Reinforcement Learning Framework for Buffer Management in Multi-Tenant Cloud Databases.](https://dblp.org/rec/conf/icdcs/HuangZWJ26)** — ICDCS; `DS-B`; score `0.80`
   - Proposes an MARL framework specifically for database buffer management, directly automating a database system operation task.

36. **[MeshAgent: Enabling Reliable Network Management with Large Language Models.](https://dblp.org/rec/conf/sigmetrics/ZhouHMKL26)** — SIGMETRICS; `DS-B`; score `0.80`
   - The title indicates an LLM-based agent specifically for network management, which is an infrastructure-automation task.

37. **[MoProteus: LLM-Driven Multi-Version Operator Generation for Energy-Aware Scheduling in Heterogeneous Cloud-Edge Environments.](https://dblp.org/rec/conf/europar/LiuWMWYL26)** — Euro-Par; `DS-B`; score `0.80`
   - Paper directly applies LLM to generate multi-version operators for energy-aware scheduling in cloud-edge systems, a concrete infrastructure-automation contribution.

38. **[Multi-agent deep reinforcement learning for penetration testing of IoT devices through their mobile companion app.](https://dblp.org/rec/journals/jss/PaganoCMT26)** — JSS; `SE-B`; score `0.80`
   - The paper directly automates penetration testing of IoT devices, a concrete security and infrastructure-operation task, via multi-agent deep reinforcement learning.

39. **[Practical Machine Learning Autotuning for Large-Scale Collective Communication.](https://dblp.org/rec/journals/tpds/WilkinsGTDH26)** — TPDS; `DS-A`; score `0.80`
   - The paper directly addresses automated tuning of large-scale collective communication, a concrete systems-software infrastructure task.

40. **[Q-Doctor: Retrieval-Augmented Diagnosis and Multi-agent Correction for Query Performance Anomalies.](https://dblp.org/rec/conf/dasfaa/HanPCYZZ26)** — DASFAA; `DB-B`; score `0.80`
   - The paper targets automated diagnosis and multi-agent correction of database query performance anomalies, directly addressing systems-operation automation.

41. **[StepFly: Agentic Troubleshooting Guide Automation for Incident Diagnosis.](https://dblp.org/rec/journals/pacmse/MaoLGPHZQKLRLZ26)** — FSE; `SE-A`; score `0.80`
   - The title indicates an agentic system that automates troubleshooting guides for incident diagnosis, directly targeting operations of computer systems.

42. **[Towards Fully Automated Compiler Backend Generation with Multi-Agent Systems: How Far Are We?](https://dblp.org/rec/conf/ics/ZhongQWGSL26)** — ICS; `DS-B`; score `0.80`
   - The paper directly targets automation of a concrete systems-software component (compiler backend generation) via multi-agent systems.

43. **[ReThermal: Co-Design of Thermal-Aware Static and Dynamic Scheduling for LLM Training on Liquid-Cooled Wafer-Scale Chips.](https://dblp.org/rec/conf/hpca/LiWLLYLJDHY26)** — HPCA; `DS-A`; score `0.78`
   - Directly addresses automated scheduling for thermal management in wafer-scale chip systems, a concrete systems-operation task.

44. **[LLM4Hint: Leveraging Large Language Models for Hint Recommendation in Offline Query Optimization.](https://dblp.org/rec/conf/icde/LiuLHG26)** — ICDE; `DB-A`; score `0.75`
   - The paper directly targets automated database query optimization via LLM-generated hints, a concrete systems-management task.

45. **[LPO: Discovering Missed Peephole Optimizations with Large Language Models.](https://dblp.org/rec/conf/asplos/XuX0ZS26)** — ASPLOS; `DS-A`; score `0.75`
   - Uses LLMs to discover missed peephole optimizations, directly automating evolution of compiler infrastructure.

46. **[Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-based Multi-Agent Systems.](https://dblp.org/rec/conf/icdcs/WangZSZLWWHY26)** — ICDCS; `DS-B`; score `0.75`
   - Presents a concrete workload-aware scheduler for cross-cluster operation of LLM-based multi-agent systems, directly contributing to distributed systems automation.

47. **[Many hands make light work: An LLM-based multi-agent system for detecting malicious PyPI packages.](https://dblp.org/rec/journals/jss/ZeshanISNR26)** — JSS; `SE-B`; score `0.75`
   - The title describes an LLM-based multi-agent system that automates detection of malicious PyPI packages, directly contributing to securing software infrastructure.

48. **[Rudder: Steering Prefetching in Distributed GNN Training using LLM Agents.](https://dblp.org/rec/conf/ics/SarkarGTCRJ26)** — ICS; `DS-B`; score `0.75`
   - The title indicates an LLM-agent-driven system that automates prefetching decisions in distributed GNN training, directly addressing infrastructure operation and performance management.

## 2025 (46)

1. **[AgentTune: An Agent-Based Large Language Model Framework for Database Knob Tuning.](https://dblp.org/rec/journals/pacmmod/LiLZBWZCSLC25)** — SIGMOD; `DB-A`; score `0.95`
   - This paper directly targets automated database configuration tuning using LLM agents, a concrete systems-management task.

2. **[AgentFM: Role-Aware Failure Management for Distributed Databases with LLM-Driven Multi-Agents.](https://dblp.org/rec/conf/sigsoft/ZhangZJHD025)** — FSE; `SE-A`; score `0.92`
   - The paper targets automated failure management for distributed databases using LLM-driven multi-agents, directly addressing database operations and infrastructure automation.

3. **[Andromeda: Debugging Database Performance Issues with Retrieval-Augmented Large Language Models.](https://dblp.org/rec/conf/sigmod/WangCF00025)** — SIGMOD; `DB-A`; score `0.90`
   - The paper directly targets automated debugging of database performance issues, a concrete systems-management task for infrastructure.

4. **[CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building.](https://dblp.org/rec/journals/pacmse/YuZWNZY25)** — FSE; `SE-A`; score `0.90`
   - The paper presents an LLM agent that automates building C/C++ software, directly contributing to software construction and infrastructure automation.

5. **[Clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs.](https://dblp.org/rec/conf/icse/GaoYSWZX25)** — ICSE; `SE-A`; score `0.90`
   - Directly automates fuzzing the Rust compiler, a core system-software component, using LLMs for test generation.

6. **[Finding Missed Code Size Optimizations in Compilers using Large Language Models.](https://dblp.org/rec/conf/cc/ItalianoC25)** — CC; `SE-B`; score `0.90`
   - Directly contributes to automating compiler infrastructure improvement by using LLMs to discover missed code size optimizations.

7. **[FleetIO: Managing Multi-Tenant Cloud Storage with Multi-Agent Reinforcement Learning.](https://dblp.org/rec/conf/asplos/SunRLCSH25)** — ASPLOS; `DS-A`; score `0.90`
   - Presents a multi-agent reinforcement learning system for managing multi-tenant cloud storage, directly automating storage infrastructure operation.

8. **[GRACE: A Strategic LLM-Enhanced Graph Reinforcement Learning Framework for Adaptive Fault Recovery in Microservice Systems.](https://dblp.org/rec/conf/icsoc/ChenPXWLZW25)** — ICSOC; `SE-B`; score `0.90`
   - Directly targets automated fault recovery in microservice systems, a core systems-management task under AIOps/SRE.

9. **[IOAgent: Democratizing Trustworthy HPC I/O Performance Diagnosis Capability via LLMs.](https://dblp.org/rec/conf/ipps/EgersdoerferSBB25)** — IPDPS; `DS-B`; score `0.90`
   - IOAgent directly automates HPC I/O performance diagnosis via LLMs, which is a concrete systems-management and infrastructure-automation task.

10. **[Interleaving Large Language Models for Compiler Testing.](https://dblp.org/rec/journals/pacmpl/Ni025)** — OOPSLA; `SE-A`; score `0.90`
   - The title indicates a direct contribution to automating compiler testing, a core systems software verification and debugging task.

11. **[KnobTuneX:LLM-Enhanced Automatic Database Tuning via Structured Reasoning.](https://dblp.org/rec/conf/icdm/YangZXWZD25)** — ICDM; `DB-B`; score `0.90`
   - The paper directly addresses automatic database configuration tuning, a concrete systems-management task.

12. **[LLM Compiler: Foundation Language Models for Compiler Optimization.](https://dblp.org/rec/conf/cc/CumminsSGRGSL25)** — CC; `SE-B`; score `0.90`
   - The paper directly addresses compiler optimization with foundation language models, a concrete systems-infrastructure automation task.

13. **[LLM4FP: LLM-Based Program Generation for Triggering Floating-Point Inconsistencies Across Compilers.](https://dblp.org/rec/conf/sc/WangR25)** — SC; `DS-A`; score `0.90`
   - Presents an LLM-based test program generator to detect floating-point inconsistencies across compilers, directly contributing to automated compiler diagnostics.

14. **[MCTuner: Spatial Decomposition-Enhanced Database Tuning via LLM-Guided Exploration.](https://dblp.org/rec/journals/pacmmod/YanXH25)** — SIGMOD; `DB-A`; score `0.90`
   - Directly automates database configuration tuning via LLM-guided exploration, a concrete systems-management task.

15. **[STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High Performance Parallel File Systems.](https://dblp.org/rec/conf/sc/EgersdoerferCSR25)** — SC; `DS-A`; score `0.90`
   - The title describes an LLM-driven autonomous engine specifically for tuning high-performance parallel file systems, directly automating storage system configuration.

16. **[TAMO:Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems.](https://dblp.org/rec/journals/tsc/ZhangWLYXZY25)** — TSC; `SE-A`; score `0.90`
   - Directly applies an LLM agent to fine-grained root cause analysis in cloud-native systems, which is an agentic AIOps infrastructure-diagnosis task.

17. **[λ-Tune: Harnessing Large Language Models for Automated Database System Tuning.](https://dblp.org/rec/journals/pacmmod/GiannakourisT25)** — SIGMOD; `DB-A`; score `0.90`
   - Directly uses large language models to automate database system tuning, a concrete systems-management task in infrastructure automation.

18. **[AI-Driven and QoS-Aware Orchestration of Interdependent Services in the Cloud Continuum.](https://dblp.org/rec/conf/icsoc/SfaxiSLYJ25)** — ICSOC; `SE-B`; score `0.85`
   - Proposes AI-driven orchestration of interdependent services in the cloud continuum, directly automating cloud infrastructure operation.

19. **[AMSES: A Novel Autonomic Model Construction Framework for System Fault Diagnosis of Microservice Architecture.](https://dblp.org/rec/conf/icws/SongCXLML25)** — ICWS; `SE-B`; score `0.85`
   - The framework directly automates construction of diagnostic models for microservice systems, targeting system fault diagnosis in infrastructure operations.

20. **[Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub.](https://dblp.org/rec/journals/ese/MinnaMT25)** — ESE; `SE-B`; score `0.85`
   - The paper applies LLMs to detect and remediate security misconfigurations in Helm charts, directly automating hardening of Kubernetes infrastructure.

21. **[Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents.](https://dblp.org/rec/conf/icse/XiangYPBKQC25)** — ICSE; `SE-A`; score `0.85`
   - Directly targets automated detection of bugs in cloud infrastructure-as-code using LLM agents, a concrete systems-infrastructure automation task.

22. **[Bridging the Gap: LLM-Powered Transfer Learning for Log Anomaly Detection in New Software Systems.](https://dblp.org/rec/conf/icde/SuiWCXHZZYSP25)** — ICDE; `DB-A`; score `0.85`
   - Automates log anomaly detection to aid diagnosis and operation of software systems.

23. **[Cracking SQL Barriers: An LLM-based Dialect Translation System.](https://dblp.org/rec/journals/pacmmod/ZhouGZL25)** — SIGMOD; `DB-A`; score `0.85`
   - Primary contribution is CrackSQL, an automated LLM-based SQL dialect translation system that directly reduces manual effort in database migration, a concrete systems/infrastructure task.

24. **[H5Intent: Autotuning HDF5 With User Intent.](https://dblp.org/rec/journals/tpds/DevarajanHM25)** — TPDS; `DS-A`; score `0.85`
   - Autotuning HDF5 directly automates configuration/tuning of a storage/data-management system, matching systems infrastructure automation.

25. **[KernelGPT: Enhanced Kernel Fuzzing via Large Language Models.](https://dblp.org/rec/conf/asplos/YangZZ25)** — ASPLOS; `DS-A`; score `0.85`
   - The paper presents an LLM-based method for automating kernel fuzzing, directly contributing to security testing and diagnosis of OS kernels, a concrete systems-infrastructure automation task.

26. **[L4: Diagnosing Large-scale LLM Training Failures via Automated Log Analysis.](https://dblp.org/rec/conf/sigsoft/Jiang0YC0ZFYYL25)** — FSE; `SE-A`; score `0.85`
   - The paper presents automated log analysis for diagnosing failures in large-scale LLM training, which directly targets a systems-management and infrastructure-automation task.

27. **[Micro-MAMA: Multi-Agent Reinforcement Learning for Multicore Prefetching.](https://dblp.org/rec/conf/micro/BlockGT25)** — MICRO; `DS-A`; score `0.85`
   - Directly applies multi-agent RL to automate prefetching in multicore processors, a concrete computer-architecture systems operation task.

28. **[Multi-agent Independent PPO-based Automatic ECN Tuning for High-Speed Data Center Networks.](https://dblp.org/rec/conf/cluster/WangCD25)** — CLUSTER; `DS-B`; score `0.85`
   - Presents an RL-based multi-agent method for automatic ECN tuning in data center networks, directly automating network infrastructure configuration.

29. **[Parse-LLM: A Prior-Free LLM Parser for Unknown System Logs.](https://dblp.org/rec/conf/cikm/SongYZLYMC25)** — CIKM; `DB-B`; score `0.85`
   - Introduces an LLM-based method for parsing unknown system logs, directly automating a systems-management diagnostic task.

30. **[RFCAudit: AI Agent for Auditing Protocol Implementations Against RFC Specifications.](https://dblp.org/rec/conf/kbse/ZhengWLGFZ25)** — ASE; `SE-A`; score `0.85`
   - RFCAudit directly automates auditing of network protocol implementations against RFC specifications, a concrete systems diagnosis/validation task.

31. **[LLM Agents for Automated Dependency Upgrades.](https://dblp.org/rec/conf/kbse/TawosiALV25)** — ASE; `SE-A`; score `0.82`
   - The paper directly addresses LLM agents automating dependency upgrades, a concrete software infrastructure evolution task.

32. **[Accurate and Interpretable Log-Based Fault Diagnosis Using Large Language Models.](https://dblp.org/rec/journals/tsc/SunMXZCDSZZHP25)** — TSC; `SE-A`; score `0.80`
   - The paper directly addresses automated log-based fault diagnosis for computer systems, which is a concrete AIOps/SRE task.

33. **[Agentic AI vs ML-based Autotuning: A Comparative Study for Loop Reordering Optimization.](https://dblp.org/rec/conf/sc/RosasEI25)** — SC; `DS-A`; score `0.80`
   - The paper directly addresses automated compiler optimization via agentic AI compared to ML autotuning for loop reordering, a concrete systems-software infrastructure task.

34. **[Agentic Auto-Scheduling: An Experimental Study of LLM-Guided Loop Optimization.](https://dblp.org/rec/conf/IEEEpact/MerouaniBB25)** — PACT; `DS-B`; score `0.80`
   - The paper directly targets compiler loop optimization, an infrastructure-automation task, using LLM-guided agents to schedule optimizations.

35. **[Can LLMs Write CI? a Study on Automatic Generation of GitHub Actions Configurations.](https://dblp.org/rec/conf/icsm/GhalebR25)** — ICSME; `SE-B`; score `0.80`
   - Directly studies automatic generation of CI/CD configuration files, a concrete infrastructure-automation task for software systems.

36. **[D-Bot: An LLM-Powered DBA Copilot.](https://dblp.org/rec/conf/sigmod/SunZWZ025)** — SIGMOD; `DB-A`; score `0.80`
   - The title indicates an LLM-powered database administrator copilot, directly automating database administration tasks, which constitutes systems-operation automation.

37. **[DeCOS: Data-Efficient Reinforcement Learning for Compiler Optimization Selection Ignited by LLM.](https://dblp.org/rec/conf/ics/CuiYMZ25)** — ICS; `DS-B`; score `0.80`
   - The paper's title directly addresses automating compiler optimization selection via RL and LLMs, a concrete compiler-tuning infrastructure task.

38. **[Dynamic Power Management Through Multi-agent Deep Reinforcement Learning for Heterogeneous Systems.](https://dblp.org/rec/journals/taco/WangZHKW25)** — TACO; `DS-A`; score `0.80`
   - The paper directly targets dynamic power management for heterogeneous computing systems via multi-agent deep RL, constituting autonomous system operation and infrastructure control.

39. **[Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning.](https://dblp.org/rec/journals/kais/LiuYY25)** — KAIS; `DB-B`; score `0.80`
   - Directly addresses automated resource orchestration in edge computing, a concrete systems-management task.

40. **[FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution.](https://dblp.org/rec/conf/kdd/ShiLWZZHZSZSLSC25)** — SIGKDD; `DB-A`; score `0.80`
   - Title indicates multi-agent orchestration of troubleshooting workflows, a direct automation contribution to IT operations and AIOps.

41. **[HYPERF: End-to-End Autotuning Framework for High-Performance Computing.](https://dblp.org/rec/conf/hpdc/ParkSLLKKS25)** — HPDC; `DS-A`; score `0.80`
   - It presents an end-to-end autotuning framework for HPC, directly automating performance tuning of computing infrastructure.

42. **[Identifying Performance-Sensitive Configurations in Software Systems with LLM-Driven Agents.](https://dblp.org/rec/conf/icse/Wang25)** — ICSE; `SE-A`; score `0.80`
   - The title clearly indicates an LLM-driven agent system for identifying performance-sensitive configurations in software systems, a direct infrastructure-automation contribution.

43. **[LLM-Powered Fully Automated Chaos Engineering: Towards Enabling Anyone to Build Resilient Software Systems at Low Cost.](https://dblp.org/rec/conf/kbse/KikutaIT25)** — ASE; `SE-A`; score `0.80`
   - The paper proposes an LLM-driven autonomous chaos engineering system, directly targeting automated resilience testing and operation of software systems.

44. **[Model and Agentic AI-driven Middleware for Distributed Systems Design and Validation.](https://dblp.org/rec/conf/middleware/Das25)** — Middleware; `SE-B`; score `0.80`
   - The title explicitly describes an agentic AI-driven middleware for automating distributed systems design and validation, a concrete infrastructure-automation contribution.

45. **[ReproCopilot: LLM-Driven Failure Reproduction with Dynamic Refinement.](https://dblp.org/rec/journals/pacmse/LeesatapornwongsaFN25)** — FSE; `SE-A`; score `0.75`
   - Proposes an LLM-driven system for automatically reproducing failures, directly targeting diagnosis and debugging of software infrastructure.

46. **[Tutoring LLM into a Better CUDA Optimizer.](https://dblp.org/rec/conf/europar/BrabecKTK25)** — Euro-Par; `DS-B`; score `0.75`
   - The paper's title indicates an LLM-based method for optimizing CUDA code, directly automating a systems-software optimization task for GPU infrastructure.

## 2024 (32)

1. **[Demonstrating λ-Tune: Exploiting Large Language Models for Workload-Adaptive Database System Tuning.](https://dblp.org/rec/conf/sigmod/GiannakourisT24)** — SIGMOD; `DB-A`; score `0.95`
   - Directly automates database system tuning using LLMs for workload adaptation, a concrete infrastructure-automation task.

2. **[Sparkle: Deep Learning Driven Autotuning for Taming High-Dimensionality of Spark Deployments.](https://dblp.org/rec/journals/tcc/MasourosRXS24)** — TCC; `DS-B`; score `0.95`
   - Proposes a deep learning-driven autotuning framework for Spark deployment configurations, directly automating configuration tuning of a distributed data-processing system.

3. **[Automatic Root Cause Analysis via Large Language Models for Cloud Incidents.](https://dblp.org/rec/conf/eurosys/ChenXMKGSCGFWZG24)** — EuroSys; `DS-A`; score `0.90`
   - Proposes LLM-based automatic root cause analysis for cloud incidents, directly targeting systems operation and diagnosis.

4. **[D-Bot: Database Diagnosis System using Large Language Models.](https://dblp.org/rec/journals/pvldb/ZhouLSLCWLFZ24)** — VLDB; `DB-A`; score `0.90`
   - D-Bot explicitly targets automated database diagnosis, a core systems-operation task using LLMs.

5. **[Hit the Gym: Accelerating Query Execution to Efficiently Bootstrap Behavior Models for Self-Driving Database Management Systems.](https://dblp.org/rec/journals/pvldb/LimMZBAP24)** — VLDB; `DB-A`; score `0.90`
   - The paper directly addresses automation in self-driving database management systems by accelerating query execution to bootstrap behavior models, a concrete systems-operation contribution.

6. **[LATuner: An LLM-Enhanced Database Tuning System Based on Adaptive Surrogate Model.](https://dblp.org/rec/conf/pkdd/FanPSYC24)** — ECML-PKDD; `DB-B`; score `0.90`
   - Presents an LLM-enhanced automated database tuning system, directly targeting infrastructure performance management.

7. **[Panda: Performance Debugging for Databases using LLM Agents.](https://dblp.org/rec/conf/cidr/SinghVKKNGK24)** — CIDR; `DB-B`; score `0.90`
   - Directly applies LLM agents to database performance debugging, a concrete systems-management task.

8. **[RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented Large Language Models.](https://dblp.org/rec/conf/cikm/WangLZZWYF0W24)** — CIKM; `DB-B`; score `0.90`
   - The paper introduces an autonomous LLM-agent system for root cause analysis in cloud systems, directly contributing to AIOps/SRE automation.

9. **[Self-Managing DRAM: A Low-Cost Framework for Enabling Autonomous and Efficient DRAM Maintenance Operations.](https://dblp.org/rec/conf/micro/HassanOYLM24)** — MICRO; `DS-A`; score `0.90`
   - Proposes a self-managing DRAM framework that directly automates memory maintenance operations, a concrete systems-infrastructure contribution.

10. **[The Holon Approach for Simultaneously Tuning Multiple Components in a Self-Driving Database Management System with Machine Learning via Synthesized Proto-Actions.](https://dblp.org/rec/journals/pvldb/ZhangLBP24)** — VLDB; `DB-A`; score `0.90`
   - The paper directly targets automated, ML-based tuning of multiple components in a self-driving database management system, a concrete infrastructure-automation task.

11. **[WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models.](https://dblp.org/rec/journals/pacmpl/YangDLY0J024)** — OOPSLA; `SE-A`; score `0.90`
   - Directly automates compiler fuzzing via white-box analysis and LLMs, a concrete infrastructure-testing and debugging contribution.

12. **[ECG: Augmenting Embedded Operating System Fuzzing via LLM-Based Corpus Generation.](https://dblp.org/rec/journals/tcad/ZhangSLXSJC24)** — TCAD; `DS-A`; score `0.85`
   - Directly augments embedded OS fuzzing with LLM-based corpus generation, contributing to automated diagnosis and security testing of operating-system software.

13. **[Pipette: Automatic Fine-Grained Large Language Model Training Configurator for Real-World Clusters.](https://dblp.org/rec/conf/date/YimSCL0JL24)** — DATE; `DS-B`; score `0.85`
   - Presents an automatic configurator for LLM training on real-world clusters, directly automating systems configuration and infrastructure operation.

14. **[AutoSched: An Adaptive Self-configured Framework for Scheduling Deep Learning Training Workloads.](https://dblp.org/rec/conf/ics/GaoZHGS0024)** — ICS; `DS-B`; score `0.80`
   - Proposes an adaptive self-configured scheduling framework for deep learning training workloads, directly targeting systems-level resource scheduling and automation.

15. **[Compiler Autotuning through Multiple-phase Learning.](https://dblp.org/rec/journals/tosem/ZhuHC24)** — TOSEM; `SE-A`; score `0.80`
   - Presents automated tuning of compiler configurations, directly targeting compiler infrastructure.

16. **[DBG-PT: A Large Language Model Assisted Query Performance Regression Debugger.](https://dblp.org/rec/journals/pvldb/GiannakourisT24)** — VLDB; `DB-A`; score `0.80`
   - Presents an LLM-assisted debugger for query performance regressions, directly automating database diagnosis and repair tasks.

17. **[Exploring LLM-Based Agents for Root Cause Analysis.](https://dblp.org/rec/conf/sigsoft/RoyZBBLFR24)** — FSE; `SE-A`; score `0.80`
   - Directly addresses automating root cause analysis of system failures using LLM agents, a core AIOps/SRE task.

18. **[Isolating Compiler Bugs by Generating Effective Witness Programs With Large Language Models.](https://dblp.org/rec/journals/tse/TuZJYLJ24)** — TSE; `SE-A`; score `0.80`
   - The paper directly automates the diagnosis and isolation of compiler bugs using LLM-generated witness programs, targeting system-software infrastructure.

19. **[LM-PACE: Confidence Estimation by Large Language Models for Effective Root Causing of Cloud Incidents.](https://dblp.org/rec/conf/sigsoft/ZhangZBLFR24)** — FSE; `SE-A`; score `0.80`
   - Targets LLM-based root cause analysis of cloud incidents, directly addressing a systems diagnosis and operation task.

20. **[MEIC: Re-thinking RTL Debug Automation using LLMs.](https://dblp.org/rec/conf/iccad/XuSHFSWJ24)** — ICCAD; `DS-B`; score `0.80`
   - Automates RTL debug for hardware design using LLMs, directly targeting computer architecture debugging.

21. **[Multi-Agent Deep Reinforcement Learning Framework for Renewable Energy-Aware Workflow Scheduling on Distributed Cloud Data Centers.](https://dblp.org/rec/journals/tpds/JayanettiHB24)** — TPDS; `DS-A`; score `0.80`
   - Proposes a multi-agent RL framework for scheduling workflows on distributed cloud data centers, directly automating infrastructure operation.

22. **[Multi-Agent Reinforcement Learning for Thermally-Restricted Performance Optimization on Manycores.](https://dblp.org/rec/conf/date/KhdrBZSH24)** — DATE; `DS-B`; score `0.80`
   - Applies multi-agent reinforcement learning to automate thermal-aware performance optimization on manycore processors, a concrete computer-architecture systems-management task.

23. **[The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators.](https://dblp.org/rec/conf/asplos/OuL0024)** — ASPLOS; `DS-A`; score `0.80`
   - LLM-generated mutation operators for fuzzing compilers directly automate the testing and diagnosis of a core system-software component.

24. **[Two-Timescale Joint Optimization of Task Scheduling and Resource Scaling in Multi-Data Center System Based on Multi-Agent Deep Reinforcement Learning.](https://dblp.org/rec/journals/tpds/ChenLYHLY24)** — TPDS; `DS-A`; score `0.80`
   - Proposes multi-agent deep RL for joint task scheduling and resource scaling in multi-data-center systems, directly automating cloud infrastructure operations.

25. **[A Multi-Agent DRL-Based Computation Offloading and Resource Allocation Method With Attention Mechanism in MEC-Enabled IIoT.](https://dblp.org/rec/journals/tsc/LingPWXL24)** — TSC; `SE-A`; score `0.75`
   - It directly automates resource allocation and computation offloading in MEC-enabled IIoT, a systems-management task for edge infrastructure.

26. **[AI-Driven Evaluation and Optimization of Bump Pitch Effects on Chiplet and Interposer Design Quality.](https://dblp.org/rec/conf/iccad/WooVL24)** — ICCAD; `DS-B`; score `0.75`
   - Automates AI-driven evaluation and optimization of chiplet and interposer design, a computer-architecture systems task.

27. **[Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs.](https://dblp.org/rec/conf/issta/ShanH000Z24)** — ISSTA; `SE-A`; score `0.75`
   - The title describes an LLM-based strategy for localizing configuration errors from logs, a direct systems-management diagnosis task.

28. **[If At First You Don't Succeed, Try, Try, Again...? Insights and LLM-informed Tooling for Detecting Retry Bugs in Software Systems.](https://dblp.org/rec/conf/sosp/StoicaSSZ0MMN24)** — SOSP; `SE-A`; score `0.75`
   - Presents LLM-informed tooling for detecting retry bugs, directly automating diagnosis of software-system reliability issues.

29. **[LLMs for Virtualized Networking Infrastructures: An Industrial Report.](https://dblp.org/rec/conf/europar/PannocchiLFAC24)** — Euro-Par; `DS-B`; score `0.75`
   - Title indicates application of LLMs to virtualized networking infrastructure, a concrete systems-management and automation context.

30. **[MissConf: LLM-Enhanced Reproduction of Configuration-Triggered Bugs.](https://dblp.org/rec/conf/icse/Fu00DZJ0JL24)** — ICSE; `SE-A`; score `0.75`
   - The title indicates an LLM-based method for reproducing configuration-triggered bugs, which is a direct systems-debugging automation contribution.

31. **[MonitorAssistant: Simplifying Cloud Service Monitoring via Large Language Models.](https://dblp.org/rec/conf/sigsoft/YuMZQ0BRDPPL024)** — FSE; `SE-A`; score `0.75`
   - The title indicates an LLM-based tool for automating cloud service monitoring, which directly concerns systems-operation and AIOps.

32. **[RESTLess: Enhancing State-of-the-Art REST API Fuzzing With LLMs in Cloud Service Computing.](https://dblp.org/rec/journals/tsc/ZhengSDJCS24)** — TSC; `SE-A`; score `0.75`
   - The paper directly uses LLMs to enhance automated fuzzing of REST APIs in cloud services, targeting infrastructure security and reliability.

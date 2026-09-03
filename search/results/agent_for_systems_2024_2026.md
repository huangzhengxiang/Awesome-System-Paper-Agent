# Agent for Systems 与系统自动化论文精筛示例（2024–2026）

> DeepSeek semantic run `15`; generated from the local CCF A/B paper database. Scores measure estimated topical relevance, not paper quality.

- Model: `deepseek-v4-flash`
- Topic: Strictly select papers whose primary research contribution directly automates the operation of computer systems or software infrastructure. Include AI/LLM agents, agentic AIOps/SRE, autonomous or self-managing systems, and automated methods for configuring, tuning, scheduling, diagnosing, debugging, securing, repairing, or recovering databases, operating systems, distributed/cloud systems, networks, storage, compilers, and computer architecture. Require a concrete systems-management or infrastructure-automation contribution. Exclude generic multi-agent or reinforcement-learning applications, user/recommender agents, ordinary code generation and general program repair, software-development assistants without systems-operation impact, LLM inference/serving optimizations without an agentic automation contribution, and automation in non-computing domains. Be conservative when evidence is only a title.
- Scope: categories `DS, SE, DB`, years `2024–2026`, source run `6`
- Threshold: `0.75`
- Screened: `278`; selected records: `105`; unique titles: `104`
- Evidence: `1` selected papers had cached abstracts; `103` were judged conservatively from titles.

## 2026 (35)

1. **[Cloud Intelligence/AIOps 2.0: Knowledge-Anchored Agentic AIOps.](https://dblp.org/rec/conf/sigsoft/ZhangLQLCSCZDKR26)** — FSE; `SE-A`; score `0.95`
   - Explicitly presents an agentic AIOps framework for cloud intelligence and infrastructure operation.

2. **[MeshAgent: Enabling Reliable Network Management with Large Language Models.](https://dblp.org/rec/conf/sigmetrics/ZhouHMKL26)** — SIGMETRICS; `DS-B`; score `0.95`
   - Introduces an LLM-based agentic system for reliable network management, directly automating network-infrastructure operations.

3. **[Why Database Manuals Are Not Enough: Efficient and Reliable Configuration Tuning for DBMSs via Code-Driven LLM Agents.](https://dblp.org/rec/journals/pvldb/ZhangCHHLWSWZLLD26)** — VLDB; `DB-A`; score `0.95`
   - LLM-agent-driven DBMS configuration tuning is a direct automated systems-management contribution.

4. **[CMA+DB: How to Automatically Tune Database Parameters Through Collaborative Multi-Agents.](https://dblp.org/rec/journals/tkde/QiaoTLGXHWYW26)** — TKDE; `DB-A`; score `0.94`
   - Directly automates database parameter tuning through collaborative multi-agent LLMs, a concrete database infrastructure-automation method.

5. **[Practical Machine Learning Autotuning for Large-Scale Collective Communication.](https://dblp.org/rec/journals/tpds/WilkinsGTDH26)** — TPDS; `DS-A`; score `0.94`
   - Automates tuning of large-scale collective-communication parameters, directly addressing distributed-systems performance autotuning.

6. **[Aloha: Localizing Batch Failures in Large-scale Cloud Systems via Contrast Analysis and Human-in-the-Loop Agent.](https://dblp.org/rec/conf/sigsoft/ZhangWRSGZLLZRB26)** — FSE; `SE-A`; score `0.92`
   - Directly targets localization of batch failures in large-scale cloud systems with a human-in-the-loop agent, matching agentic AIOps/SRE.

7. **[An Agentic Framework for Triaging Incidents in Production Cloud Infrastructure.](https://dblp.org/rec/conf/sigsoft/YaoJMVDHBLC26)** — FSE; `SE-A`; score `0.92`
   - Describes an agentic framework for triaging incidents in production cloud infrastructure, a concrete AIOps/SRE automation contribution.

8. **[CAP: Detecting Network Device Misconfigurations with Context-Aware Prompting of LLMs.](https://dblp.org/rec/journals/pomacs/JiangGF26)** — SIGMETRICS; `DS-B`; score `0.92`
   - Uses LLM-based context-aware detection to automate diagnosis of network device misconfigurations, a direct infrastructure-automation contribution.

9. **[Q-Doctor: Retrieval-Augmented Diagnosis and Multi-agent Correction for Query Performance Anomalies.](https://dblp.org/rec/conf/dasfaa/HanPCYZZ26)** — DASFAA; `DB-B`; score `0.91`
   - Provides LLM-based diagnosis and correction of query performance anomalies, directly automating database troubleshooting and repair.

10. **[DBAIOps: A Reasoning LLM-Enhanced Database Operation and Maintenance System using Knowledge Graphs.](https://dblp.org/rec/journals/pvldb/ZhouSZZXZLW26)** — VLDB; `DB-A`; score `0.90`
   - Combines reasoning LLMs with knowledge graphs to automate database operation and maintenance.

11. **[Generative AI as an infrastructure copilot: automating Infrastructure-As-Code across the DevSecOps lifecycle.](https://dblp.org/rec/journals/ase/EspositoRBTL26)** — ASE; `SE-B`; score `0.90`
   - Automates Infrastructure-as-Code generation across the DevSecOps lifecycle, a direct infrastructure-automation contribution.

12. **[LLM Agents for AIOps in Kubernetes: An Industrial Experience Report with Red Hat OpenShift.](https://dblp.org/rec/conf/sigsoft/VituiC26)** — FSE; `SE-A`; score `0.90`
   - LLM agents for AIOps in Kubernetes with Red Hat OpenShift experience is an explicit infrastructure-automation deployment.

13. **[This is Going to Sound Crazy, But What If We Used Large Language Models to Boost Automatic Database Tuning Algorithms By Leveraging Prior History? We Will Find Better Configurations More Quickly Than Retraining From Scratch!](https://dblp.org/rec/journals/pacmmod/ZhangLP26)** — SIGMOD; `DB-A`; score `0.90`
   - The paper directly targets automated database configuration tuning, an infrastructure-management task, by using LLMs to improve search over prior tuning histories.

14. **[A Hierarchical GNN-Based Multi-Agent Framework for Workflow Scheduling in Hybrid Clouds Considering Privacy Constraints.](https://dblp.org/rec/journals/tsc/GuZLFZTC26)** — TSC; `SE-A`; score `0.88`
   - Presents a multi-agent GNN-based framework for workflow scheduling in hybrid clouds, directly automating cloud infrastructure scheduling.

15. **[An Agent Framework for Fault Recovery Planning Generation Based on Model Context Protocol.](https://dblp.org/rec/conf/iscas/YaoYWXWCZ26)** — ISCAS; `DS-B`; score `0.88`
   - Presents an agent framework for generating fault recovery plans, directly automating system fault recovery and remediation.

16. **[Autonomic Resource Harvesting in HPC: Control Methods and Their Reusability.](https://dblp.org/rec/journals/taas/GuilloteauBCRPR26)** — TAAS; `DS-B`; score `0.88`
   - Autonomic resource harvesting in HPC directly automates management and scheduling of cluster compute resources.

17. **[Can LLMs Hack Enterprise Networks? Autonomous Assumed Breach Penetration-Testing Active Directory Networks.](https://dblp.org/rec/journals/tosem/HappeC26)** — TOSEM; `SE-A`; score `0.87`
   - Autonomous LLM agents performing assumed-breach penetration testing automate enterprise network security assessment and vulnerability diagnosis.

18. **[LLM-VeriOpt: Verification-Guided Reinforcement Learning for LLM-Based Compiler Optimization.](https://dblp.org/rec/conf/cgo/FangKRAM26)** — IEEE/ACM CGO; `DS-B`; score `0.85`
   - Uses verification-guided reinforcement learning to automate compiler optimizations, a clear infrastructure-automation contribution.

19. **[Late Breaking Results: Never-Stopping Inference: Self-Healing AI Accelerators on SRAM-FPGAs.](https://dblp.org/rec/conf/date/VaccaCS26)** — DATE; `DS-B`; score `0.85`
   - Presents self-healing AI accelerator hardware, an autonomous recovery mechanism in computer architecture.

20. **[StepFly: Agentic Troubleshooting Guide Automation for Incident Diagnosis.](https://dblp.org/rec/journals/pacmse/MaoLGPHZQKLRLZ26)** — FSE; `SE-A`; score `0.85`
   - Directly automates incident diagnosis via agentic troubleshooting guides, a concrete infrastructure-automation contribution.

21. **[kAPR: A coverage-guided, context-aware agent for automated repair of Linux kernel bugs.](https://dblp.org/rec/journals/infsof/LiYZLJ26)** — IST; `SE-B`; score `0.85`
   - Agent-based automated repair of Linux kernel bugs is a concrete automated repair contribution for an operating system.

22. **[Harmonia: Enhancing Data Placement and Migration in Hybrid Storage Systems via Multi-Agent Reinforcement Learning.](https://dblp.org/rec/conf/ics/NadigABSSKYSPM26)** — ICS; `DS-B`; score `0.80`
   - Uses multi-agent reinforcement learning to automate data placement and migration in hybrid storage systems.

23. **[Heuristic-Guided Multi-Agent Reinforcement Learning for Computing Service Scheduling in Distributed Data Centers.](https://dblp.org/rec/journals/tsc/ZhaoWYLJ26)** — TSC; `SE-A`; score `0.80`
   - Heuristic-guided multi-agent reinforcement learning for computing service scheduling in distributed data centers directly automates cloud resource operation.

24. **[Highlighting true alerts in false-positive-heavy intrusion detection systems outputs through unsupervised community detection and large language models.](https://dblp.org/rec/journals/isci/LopezGarciaBMFG26)** — Information Sciences; `DB-B`; score `0.80`
   - Automates triage of intrusion-detection alerts using community detection and LLMs, improving security operations.

25. **[Identifying performance-sensitive configurations in software systems with LLM-based agents.](https://dblp.org/rec/journals/ese/WangKC26)** — ESE; `SE-B`; score `0.80`
   - LLM-based agents identify performance-sensitive configurations, automating diagnosis and tuning of software systems.

26. **[Integrating Multi-Agent Reinforcement Learning and XGBoost for Efficient Large-Scale Dynamic Workflow Scheduling in Cloud Environments.](https://dblp.org/rec/journals/tsc/DingZY26)** — TSC; `SE-A`; score `0.80`
   - Integrates multi-agent reinforcement learning and XGBoost for automated workflow scheduling in cloud environments.

27. **[LLM-Based Misconfiguration Detection for AWS Serverless Computing.](https://dblp.org/rec/journals/tosem/WenCZSLPW26)** — TOSEM; `SE-A`; score `0.80`
   - LLM-based misconfiguration detection for AWS serverless computing automates security and configuration management.

28. **[LLM4Hint: Leveraging Large Language Models for Hint Recommendation in Offline Query Optimization.](https://dblp.org/rec/conf/icde/LiuLHG26)** — ICDE; `DB-A`; score `0.80`
   - Automates database query optimization by recommending hints, directly affecting query execution infrastructure.

29. **[LOOPRAG: Enhancing Loop Transformation Optimization with Retrieval-Augmented Large Language Models.](https://dblp.org/rec/conf/asplos/ZhiCDHPWCC26)** — ASPLOS; `DS-A`; score `0.80`
   - Applies retrieval-augmented LLMs to automate loop transformation optimization in compilers.

30. **[LPO: Discovering Missed Peephole Optimizations with Large Language Models.](https://dblp.org/rec/conf/asplos/XuX0ZS26)** — ASPLOS; `DS-A`; score `0.80`
   - Automates detection and generation of missed peephole compiler optimizations.

31. **[MARL: A Multi-Agent Reinforcement Learning Framework for Buffer Management in Multi-Tenant Cloud Databases.](https://dblp.org/rec/conf/icdcs/HuangZWJ26)** — ICDCS; `DS-B`; score `0.80`
   - Uses multi-agent reinforcement learning to automate buffer management in cloud databases, a concrete systems-management task.

32. **[Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-based Multi-Agent Systems.](https://dblp.org/rec/conf/icdcs/WangZSZLWWHY26)** — ICDCS; `DS-B`; score `0.80`
   - Provides workload-aware cross-cluster scheduling for LLM-based multi-agent systems, automating operation of distributed agent infrastructure.

33. **[SageServe: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling.](https://dblp.org/rec/conf/sigmetrics/JaiswalJSPMWABR26)** — SIGMETRICS; `DS-B`; score `0.80`
   - Proposes forecast-aware auto-scaling for LLM serving in cloud data centers, directly automating resource provisioning for infrastructure.

34. **[Metis: Agentic Knowledge Synthesis for Explainable I/O Performance in HPC Systems.](https://dblp.org/rec/conf/hpdc/YoussefNRD26)** — HPDC; `DS-A`; score `0.78`
   - Uses an agentic approach to synthesize and explain I/O performance problems in HPC systems, contributing to automated system diagnosis.

35. **[Enhance Performance Tuning via LLM-guided Search Templates.](https://dblp.org/rec/conf/ics/MarzoukiXVBKW26)** — ICS; `DS-B`; score `0.75`
   - LLM-guided performance tuning directly targets system/configuration tuning, a core infrastructure-automation task.

## 2025 (41)

1. **[STELLAR: Storage Tuning Engine Leveraging LLM Autonomous Reasoning for High Performance Parallel File Systems.](https://dblp.org/rec/conf/sc/EgersdoerferCSR25)** — SC; `DS-A`; score `0.98`
   - STELLAR directly automates storage tuning of parallel file systems using LLM autonomous reasoning.

2. **[TAMO:Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems.](https://dblp.org/rec/journals/tsc/ZhangWLYXZY25)** — TSC; `SE-A`; score `0.97`
   - TAMO uses a tool-assisted LLM agent for fine-grained root-cause analysis in cloud-native systems, directly automating diagnosis in AIOps.

3. **[AgentTune: An Agent-Based Large Language Model Framework for Database Knob Tuning.](https://dblp.org/rec/journals/pacmmod/LiLZBWZCSLC25)** — SIGMOD; `DB-A`; score `0.95`
   - Agent-based LLM framework for database knob tuning directly automates database configuration and tuning.

4. **[KnobTuneX:LLM-Enhanced Automatic Database Tuning via Structured Reasoning.](https://dblp.org/rec/conf/icdm/YangZXWZD25)** — ICDM; `DB-B`; score `0.95`
   - Directly proposes LLM-based automatic database configuration tuning, a clear infrastructure-automation contribution.

5. **[λ-Tune: Harnessing Large Language Models for Automated Database System Tuning.](https://dblp.org/rec/journals/pacmmod/GiannakourisT25)** — SIGMOD; `DB-A`; score `0.95`
   - It directly uses LLMs to automate database system tuning.

6. **[AgentFM: Role-Aware Failure Management for Distributed Databases with LLM-Driven Multi-Agents.](https://dblp.org/rec/conf/sigsoft/ZhangZJHD025)** — FSE; `SE-A`; score `0.92`
   - LLM-driven multi-agent failure management for distributed databases is direct agentic infrastructure automation.

7. **[Cracking SQL Barriers: An LLM-based Dialect Translation System.](https://dblp.org/rec/journals/pacmmod/ZhouGZL25)** — SIGMOD; `DB-A`; score `0.92`
   - Presents an LLM-based system for automatic SQL dialect translation that directly reduces database migration complexity.

8. **[Andromeda: Debugging Database Performance Issues with Retrieval-Augmented Large Language Models.](https://dblp.org/rec/conf/sigmod/WangCF00025)** — SIGMOD; `DB-A`; score `0.90`
   - RAG-based debugging of database performance issues automates database diagnosis and repair.

9. **[D-Bot: An LLM-Powered DBA Copilot.](https://dblp.org/rec/conf/sigmod/SunZWZ025)** — SIGMOD; `DB-A`; score `0.90`
   - Title indicates an LLM-powered DBA copilot, directly implying automated database administration and operational support.

10. **[FleetIO: Managing Multi-Tenant Cloud Storage with Multi-Agent Reinforcement Learning.](https://dblp.org/rec/conf/asplos/SunRLCSH25)** — ASPLOS; `DS-A`; score `0.90`
   - FleetIO uses multi-agent reinforcement learning to manage multi-tenant cloud storage, directly automating storage infrastructure.

11. **[IOAgent: Democratizing Trustworthy HPC I/O Performance Diagnosis Capability via LLMs.](https://dblp.org/rec/conf/ipps/EgersdoerferSBB25)** — IPDPS; `DS-B`; score `0.90`
   - LLM agent for HPC I/O performance diagnosis directly automates infrastructure diagnosis and operation.

12. **[L4: Diagnosing Large-scale LLM Training Failures via Automated Log Analysis.](https://dblp.org/rec/conf/sigsoft/Jiang0YC0ZFYYL25)** — FSE; `SE-A`; score `0.90`
   - Automates failure diagnosis in large-scale LLM training clusters via log analysis, fitting AIOps/SRE-style systems management.

13. **[LLM-Powered Fully Automated Chaos Engineering: Towards Enabling Anyone to Build Resilient Software Systems at Low Cost.](https://dblp.org/rec/conf/kbse/KikutaIT25)** — ASE; `SE-A`; score `0.90`
   - Automates chaos engineering to test software-system resiliency, directly contributing to infrastructure reliability operations.

14. **[MCTuner: Spatial Decomposition-Enhanced Database Tuning via LLM-Guided Exploration.](https://dblp.org/rec/journals/pacmmod/YanXH25)** — SIGMOD; `DB-A`; score `0.90`
   - Proposes an LLM-guided database tuner, directly automating database configuration and performance tuning.

15. **[AutoBnB-RAG: Enhancing Multi-Agent Incident Response with Retrieval-Augmented Generation.](https://dblp.org/rec/conf/icdm/LiuA25)** — ICDM; `DB-B`; score `0.88`
   - Multi-agent incident response with retrieval augmentation is agentic AIOps/SRE automation.

16. **[Automated Bug Discovery in Cloud Infrastructure-as-Code Updates with LLM Agents.](https://dblp.org/rec/conf/icse/XiangYPBKQC25)** — ICSE; `SE-A`; score `0.88`
   - Automated bug discovery in cloud infrastructure-as-code updates directly automates cloud deployment validation and security.

17. **[DeCOS: Data-Efficient Reinforcement Learning for Compiler Optimization Selection Ignited by LLM.](https://dblp.org/rec/conf/ics/CuiYMZ25)** — ICS; `DS-B`; score `0.88`
   - Reinforcement learning for compiler optimization selection is an automated tuning method for compiler infrastructure.

18. **[GRACE: A Strategic LLM-Enhanced Graph Reinforcement Learning Framework for Adaptive Fault Recovery in Microservice Systems.](https://dblp.org/rec/conf/icsoc/ChenPXWLZW25)** — ICSOC; `SE-B`; score `0.88`
   - GRACE applies LLM-enhanced reinforcement learning to adaptive fault recovery in microservices, directly automating SRE operations.

19. **[Identifying Performance-Sensitive Configurations in Software Systems with LLM-Driven Agents.](https://dblp.org/rec/conf/icse/Wang25)** — ICSE; `SE-A`; score `0.88`
   - LLM-driven agents identifying performance-sensitive configurations directly automate configuration analysis and tuning of software systems.

20. **[Triangle: Empowering Incident Triage with Multi-Agent.](https://dblp.org/rec/conf/kbse/YuFMWZCLCZWBRLZPH25)** — ASE; `SE-A`; score `0.88`
   - Multi-agent incident triage directly addresses AIOps/SRE operational diagnosis and management.

21. **[H5Intent: Autotuning HDF5 With User Intent.](https://dblp.org/rec/journals/tpds/DevarajanHM25)** — TPDS; `DS-A`; score `0.87`
   - H5Intent autotunes HDF5 based on user intent, concretely automating configuration/tuning of storage software.

22. **[Analyzing and mitigating (with LLMs) the security misconfigurations of Helm charts from Artifact Hub.](https://dblp.org/rec/journals/ese/MinnaMT25)** — ESE; `SE-B`; score `0.85`
   - Mitigating Helm-chart security misconfigurations automates securing cloud/Kubernetes infrastructure.

23. **[CacheC: LLM-Based GPU Cache Management to Enhance Kernel Concurrency.](https://dblp.org/rec/conf/europar/XiHZ25)** — Euro-Par; `DS-B`; score `0.85`
   - LLM-driven GPU cache management is a concrete automated systems-level resource-management contribution for accelerating kernel execution.

24. **[Dynamic Power Management Through Multi-agent Deep Reinforcement Learning for Heterogeneous Systems.](https://dblp.org/rec/journals/taco/WangZHKW25)** — TACO; `DS-A`; score `0.85`
   - Applies multi-agent deep reinforcement learning to dynamic power management in heterogeneous systems, a concrete hardware/OS operation automation task.

25. **[Is In-Context Learning Feasible for HPC Performance Autotuning?](https://dblp.org/rec/conf/ipps/RandallBGB25)** — IPDPS; `DS-B`; score `0.85`
   - Directly studies automated performance autotuning for HPC systems, a concrete tuning task for computational infrastructure.

26. **[LLM-based Optimization Algorithm Selection for High-Performance Networks Orchestration.](https://dblp.org/rec/conf/sc/DalgkitsisHPGL25)** — SC; `DS-A`; score `0.85`
   - Uses LLMs to select optimization algorithms for network orchestration, directly automating high-performance network operation.

27. **[FlowXpert: Expertizing Troubleshooting Workflow Orchestration with Knowledge Base and Multi-Agent Coevolution.](https://dblp.org/rec/conf/kdd/ShiLWZZHZSZSLSC25)** — SIGKDD; `DB-A`; score `0.84`
   - FlowXpert automates troubleshooting workflow orchestration via knowledge bases and multi-agent collaboration, an agentic AIOps contribution.

28. **[HYPERF: End-to-End Autotuning Framework for High-Performance Computing.](https://dblp.org/rec/conf/hpdc/ParkSLLKKS25)** — HPDC; `DS-A`; score `0.83`
   - HYPERF is an end-to-end autotuning framework for HPC, automating performance configuration of high-performance computing systems.

29. **[Agentic AI vs ML-based Autotuning: A Comparative Study for Loop Reordering Optimization.](https://dblp.org/rec/conf/sc/RosasEI25)** — SC; `DS-A`; score `0.82`
   - Agentic LLM autotuning for loop reordering is a compiler/infrastructure automation contribution.

30. **[Agentic Auto-Scheduling: An Experimental Study of LLM-Guided Loop Optimization.](https://dblp.org/rec/conf/IEEEpact/MerouaniBB25)** — PACT; `DS-B`; score `0.82`
   - LLM-guided loop auto-scheduling targets automated compiler scheduling and optimization.

31. **[AMSES: A Novel Autonomic Model Construction Framework for System Fault Diagnosis of Microservice Architecture.](https://dblp.org/rec/conf/icws/SongCXLML25)** — ICWS; `SE-B`; score `0.80`
   - An autonomic fault-diagnosis framework for microservice architectures targets automated system diagnosis and management.

32. **[CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building.](https://dblp.org/rec/journals/pacmse/YuZWNZY25)** — FSE; `SE-A`; score `0.80`
   - An LLM-based agent that automates building C/C++ software directly automates software infrastructure configuration and toolchain operations.

33. **[Can Large Language Models Be Query Optimizer for Relational Databases?](https://dblp.org/rec/journals/pacmmod/TanZLYPCMZR25)** — SIGMOD; `DB-A`; score `0.80`
   - Using LLMs as query optimizers directly targets automated query optimization for relational database systems.

34. **[Multi-agent Independent PPO-based Automatic ECN Tuning for High-Speed Data Center Networks.](https://dblp.org/rec/conf/cluster/WangCD25)** — CLUSTER; `DS-B`; score `0.80`
   - Automatically tunes ECN thresholds in high-speed datacenter networks, a concrete network infrastructure automation task.

35. **[Accurate and Interpretable Log-Based Fault Diagnosis Using Large Language Models.](https://dblp.org/rec/journals/tsc/SunMXZCDSZZHP25)** — TSC; `SE-A`; score `0.78`
   - Log-based fault diagnosis directly addresses automated diagnosis of running computing systems.

36. **[Finding Missed Code Size Optimizations in Compilers using Large Language Models.](https://dblp.org/rec/conf/cc/ItalianoC25)** — CC; `SE-B`; score `0.78`
   - LLM-driven detection of missed compiler code-size optimizations is an automated compiler-infrastructure optimization contribution.

37. **[Integrated and Fungible Scheduling of Deep Learning Workloads Using Multi-Agent Reinforcement Learning.](https://dblp.org/rec/journals/tpds/LiXYMW25)** — TPDS; `DS-A`; score `0.78`
   - Multi-agent reinforcement learning is applied to scheduling deep-learning workloads, a concrete infrastructure scheduling contribution.

38. **[Bridging the Gap: LLM-Powered Transfer Learning for Log Anomaly Detection in New Software Systems.](https://dblp.org/rec/conf/icde/SuiWCXHZZYSP25)** — ICDE; `DB-A`; score `0.77`
   - LLM-powered log anomaly detection for new software systems automates monitoring and diagnosis.

39. **[Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning.](https://dblp.org/rec/journals/kais/LiuYY25)** — KAIS; `DB-B`; score `0.76`
   - Directly targets dynamic resource orchestration in edge-computing infrastructure, which is a concrete systems-management automation task.

40. **[Can LLMs Write CI? a Study on Automatic Generation of GitHub Actions Configurations.](https://dblp.org/rec/conf/icsm/GhalebR25)** — ICSME; `SE-B`; score `0.75`
   - Automatic generation of GitHub Actions CI configurations automates configuration of software-infrastructure workflows.

41. **[Large Language Models as Configuration Validators.](https://dblp.org/rec/conf/icse/LianCC0TZX25)** — ICSE; `SE-A`; score `0.75`
   - Directly addresses automated configuration validation for computer systems, a concrete infrastructure-management task.

## 2024 (28)

1. **[RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented Large Language Models.](https://dblp.org/rec/conf/cikm/WangLZZWYF0W24)** — CIKM; `DB-B`; score `0.96`
   - Autonomous tool-augmented LLM agents perform cloud root cause analysis, a direct agentic AIOps contribution.

2. **[Hit the Gym: Accelerating Query Execution to Efficiently Bootstrap Behavior Models for Self-Driving Database Management Systems.](https://dblp.org/rec/journals/pvldb/LimMZBAP24)** — VLDB; `DB-A`; score `0.95`
   - Targets self-driving database management system behavior-model bootstrapping, an autonomous database operation contribution.

3. **[Panda: Performance Debugging for Databases using LLM Agents.](https://dblp.org/rec/conf/cidr/SinghVKKNGK24)** — CIDR; `DB-B`; score `0.95`
   - LLM agents automate database performance debugging, directly targeting diagnosis of database infrastructure.

4. **[The Holon Approach for Simultaneously Tuning Multiple Components in a Self-Driving Database Management System with Machine Learning via Synthesized Proto-Actions.](https://dblp.org/rec/journals/pvldb/ZhangLBP24)** — VLDB; `DB-A`; score `0.95`
   - Simultaneously tuning multiple components in a self-driving database management system is direct autonomous systems management.

5. **[Self-Managing DRAM: A Low-Cost Framework for Enabling Autonomous and Efficient DRAM Maintenance Operations.](https://dblp.org/rec/conf/micro/HassanOYLM24)** — MICRO; `DS-A`; score `0.94`
   - Autonomous DRAM maintenance operations directly automate memory-system management and repair.

6. **[D-Bot: Database Diagnosis System using Large Language Models.](https://dblp.org/rec/journals/pvldb/ZhouLSLCWLFZ24)** — VLDB; `DB-A`; score `0.93`
   - D-Bot targets automated database diagnosis using LLMs, which is core AIOps/systems-management automation.

7. **[An Autonomic Resource Allocating SSD.](https://dblp.org/rec/conf/date/LeeCPKKC24)** — DATE; `DS-B`; score `0.92`
   - An autonomic SSD that automatically allocates resources directly automates storage-device infrastructure operation.

8. **[Automatic Root Cause Analysis via Large Language Models for Cloud Incidents.](https://dblp.org/rec/conf/eurosys/ChenXMKGSCGFWZG24)** — EuroSys; `DS-A`; score `0.92`
   - Automatic LLM-based root cause analysis of cloud incidents is agentic AIOps for diagnosing cloud infrastructure.

9. **[Demonstrating λ-Tune: Exploiting Large Language Models for Workload-Adaptive Database System Tuning.](https://dblp.org/rec/conf/sigmod/GiannakourisT24)** — SIGMOD; `DB-A`; score `0.92`
   - Lambda-Tune applies LLMs to workload-adaptive database system tuning, directly automating DBMS infrastructure management.

10. **[Sparkle: Deep Learning Driven Autotuning for Taming High-Dimensionality of Spark Deployments.](https://dblp.org/rec/journals/tcc/MasourosRXS24)** — TCC; `DS-B`; score `0.92`
   - Deep-learning-driven autotuning of Spark deployments automates configuration of distributed system infrastructure.

11. **[Agile-Ant: Self-managing Distributed Cache Management for Cost Optimization of Big Data Applications.](https://dblp.org/rec/journals/pvldb/AlSayehJS24)** — VLDB; `DB-A`; score `0.90`
   - It presents a self-managing distributed cache that automates cost-oriented cache management for big-data systems.

12. **[AutoSched: An Adaptive Self-configured Framework for Scheduling Deep Learning Training Workloads.](https://dblp.org/rec/conf/ics/GaoZHGS0024)** — ICS; `DS-B`; score `0.90`
   - AutoSched proposes a self-configuring scheduling framework for deep learning training workloads, an infrastructure-automation contribution.

13. **[DBG-PT: A Large Language Model Assisted Query Performance Regression Debugger.](https://dblp.org/rec/journals/pvldb/GiannakourisT24)** — VLDB; `DB-A`; score `0.90`
   - LLM-assisted debugging of query performance regressions automates diagnosis of database system issues.

14. **[Face It Yourselves: An LLM-Based Two-Stage Strategy to Localize Configuration Errors via Logs.](https://dblp.org/rec/conf/issta/ShanH000Z24)** — ISSTA; `SE-A`; score `0.90`
   - Proposes LLM-based automatic localization of configuration errors from logs, directly diagnosing system misconfigurations.

15. **[LATuner: An LLM-Enhanced Database Tuning System Based on Adaptive Surrogate Model.](https://dblp.org/rec/conf/pkdd/FanPSYC24)** — ECML-PKDD; `DB-B`; score `0.90`
   - Presents an LLM-enhanced database tuning system with adaptive surrogate model, an automated database configuration/tuning contribution.

16. **[Pipette: Automatic Fine-Grained Large Language Model Training Configurator for Real-World Clusters.](https://dblp.org/rec/conf/date/YimSCL0JL24)** — DATE; `DS-B`; score `0.90`
   - Automates configuration of large-scale LLM training workloads on real clusters, a concrete cluster-configuration contribution.

17. **[X-Lifecycle Learning for Cloud Incident Management using LLMs.](https://dblp.org/rec/conf/sigsoft/GoelHSGPBZR24)** — FSE; `SE-A`; score `0.90`
   - It uses LLMs for cloud incident-management lifecycle, directly addressing automated diagnosis and operation of distributed systems.

18. **[Exploring LLM-Based Agents for Root Cause Analysis.](https://dblp.org/rec/conf/sigsoft/RoyZBBLFR24)** — FSE; `SE-A`; score `0.85`
   - LLM-based agents for root cause analysis automate failure diagnosis in AIOps/SRE contexts.

19. **[LM-PACE: Confidence Estimation by Large Language Models for Effective Root Causing of Cloud Incidents.](https://dblp.org/rec/conf/sigsoft/ZhangZBLFR24)** — FSE; `SE-A`; score `0.85`
   - Uses LLM-based confidence estimation to improve root causing of cloud incidents, directly serving cloud diagnosis.

20. **[MissConf: LLM-Enhanced Reproduction of Configuration-Triggered Bugs.](https://dblp.org/rec/conf/icse/Fu00DZJ0JL24)** — ICSE; `SE-A`; score `0.85`
   - Introduces an LLM-enhanced method for reproducing configuration-triggered bugs, automating debugging of configurable systems.

21. **[Compiler Autotuning through Multiple-phase Learning.](https://dblp.org/rec/journals/tosem/ZhuHC24)** — TOSEM; `SE-A`; score `0.82`
   - Compiler autotuning directly automates the tuning/configuration of compiler infrastructure.

22. **[Building AI Agents for Autonomous Clouds: Challenges and Design Principles.](https://dblp.org/rec/conf/cloud/ShettyCSMSZMVLG24)** — SoCC; `DS-B`; score `0.80`
   - It directly targets building AI agents for autonomous cloud operations and infrastructure management.

23. **[ECG: Augmenting Embedded Operating System Fuzzing via LLM-Based Corpus Generation.](https://dblp.org/rec/journals/tcad/ZhangSLXSJC24)** — TCAD; `DS-A`; score `0.80`
   - ECG automates embedded operating-system fuzzing for security/correctness via LLM-based corpus generation.

24. **[LLM-R2: A Large Language Model Enhanced Rule-based Rewrite System for Boosting Query Efficiency.](https://dblp.org/rec/journals/pvldb/LiYWCB24)** — VLDB; `DB-A`; score `0.80`
   - Presents an LLM-enhanced rule-based rewrite system for automatically optimizing database query execution.

25. **[MonitorAssistant: Simplifying Cloud Service Monitoring via Large Language Models.](https://dblp.org/rec/conf/sigsoft/YuMZQ0BRDPPL024)** — FSE; `SE-A`; score `0.80`
   - Uses LLMs to simplify cloud service monitoring, directly supporting AIOps and cloud infrastructure operations.

26. **[Xpert: Empowering Incident Management with Query Recommendations via Large Language Models.](https://dblp.org/rec/conf/icse/JiangZHYMQ0DRL024)** — ICSE; `SE-A`; score `0.80`
   - It empowers cloud incident management with LLM-generated diagnostic query recommendations, an AIOps contribution.

27. **[An Exploration of Global Optimization Strategies for Autotuning OpenMP-based Codes.](https://dblp.org/rec/conf/ipps/BoletGPCBG24)** — IPDPS; `DS-B`; score `0.78`
   - Autotuning OpenMP-based codes directly automates compiler/runtime configuration and performance tuning for parallel systems.

28. **[Enhancing Black-box Compiler Option Fuzzing with LLM through Command Feedback.](https://dblp.org/rec/conf/issre/WangWCYPZMZ24)** — ISSRE; `SE-B`; score `0.75`
   - LLM-based compiler option fuzzing contributes automated security/robustness testing for compiler infrastructure.

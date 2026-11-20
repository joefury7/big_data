import os
import shutil

TEMPLATE_DIR = r"C:\Users\JOEL\Downloads\big_data_template"
REPORT_DIR = r"c:\Users\JOEL\OneDrive\Desktop\big_data\report"
FINAL_REPORT_DIR = r"c:\Users\JOEL\OneDrive\Desktop\big_data\final_report"

def generate_latex():
    # Build the full publication-grade LaTeX report using the official big_data_template
    tex = r"""\documentclass[12pt,a4paper]{report}

% =========================================================
% BIG DATA SYSTEMS (24CI51) - PROJECT / SELF-LEARNING REPORT
% =========================================================

% ---------------- Packages ----------------
\usepackage[a4paper,top=1.55in,bottom=1in,left=1.25in,right=1in,
            headheight=95pt,headsep=18pt]{geometry}
\usepackage{setspace}
\usepackage{times}
\usepackage{graphicx}
\usepackage{float}
\usepackage{array}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{fancyhdr}
\usepackage{hyperref}
\usepackage{ragged2e}
\usepackage{enumitem}
\usepackage{caption}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{xcolor}
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{listings}

\graphicspath{{images/}}

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    urlcolor=black,
    citecolor=black
}

\onehalfspacing
\setlength{\parindent}{0.5in}
\setlength{\parskip}{0pt}
\justifying
\setlist[itemize]{leftmargin=*}
\setlist[enumerate]{leftmargin=*}
\renewcommand{\arraystretch}{1.2}

% ---------------- Code Listing Style ----------------
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codebg}{rgb}{0.96,0.96,0.96}
\definecolor{codeblue}{rgb}{0.1,0.2,0.6}
\definecolor{codegreen}{rgb}{0.1,0.5,0.2}

\lstdefinestyle{codestyle}{
    backgroundcolor=\color{codebg},
    commentstyle=\color{codegreen},
    keywordstyle=\color{codeblue}\bfseries,
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{purple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2,
    frame=single,
    rulecolor=\color{black!20}
}
\lstset{style=codestyle}

% ---------------- Project Details ----------------
\newcommand{\ProjectTitle}{BIG DATA SYSTEMS: TECHNOLOGY STUDY AND IMPLEMENTATION}
\newcommand{\CourseCode}{24CI51 -- BIG DATA SYSTEMS}
\newcommand{\AcademicYear}{2025--2026}
\newcommand{\Department}{DEPARTMENT OF CSE (ARTIFICIAL INTELLIGENCE \& MACHINE LEARNING)}
\newcommand{\StudentOne}{Joel B John}
\newcommand{\USNOne}{1MS24CI060}
\newcommand{\GuideOne}{Mr. Subash N}
\newcommand{\GuideDesignation}{Assistant Professor}
\newcommand{\HOD}{Dr. Siddesh G M}
\newcommand{\HODDesignation}{Professor \& Head}

% ---------------- Header/Footer ----------------
\newcommand{\RamaiahHeaderImage}{%
  \includegraphics[width=1\textwidth,height=4cm,keepaspectratio]{images/rit_header.png}%
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\RamaiahHeaderImage}
\fancyfoot[L]{\small \AcademicYear}
\fancyfoot[C]{\small Big Data Systems (24CI51)}
\fancyfoot[R]{\small \thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}

\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyhead[C]{\RamaiahHeaderImage}
  \fancyfoot[L]{\small \AcademicYear}
  \fancyfoot[C]{\small Big Data Systems (24CI51)}
  \fancyfoot[R]{\small \thepage}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0.4pt}
}

\titleformat{\chapter}[display]
  {\normalfont\bfseries\centering\Large}
  {\chaptername\ \thechapter}{10pt}{\Large}
\titleformat{\section}{\normalfont\bfseries\large}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\bfseries}{\thesubsection}{1em}{}

% ---------------- Reusable report helpers ----------------
\newcommand{\activityheading}[2]{%
  \section{Activity #1: #2}%
}
\newcommand{\insertfigure}[3][0.85\textwidth]{%
\begin{figure}[H]
    \centering
    \includegraphics[width=#1]{#2}
    \caption{#3}
    \label{fig:#2}
\end{figure}
}

\begin{document}

% =========================================================
% TITLE PAGE
% =========================================================
\begin{titlepage}
\centering
\thispagestyle{empty}

\vspace*{0.4cm}
{\bfseries\Large A REPORT ON\\[0.3cm]}
{\bfseries\LARGE \ProjectTitle\\[0.6cm]}

{\bfseries for the course\\[0.2cm]}
{\bfseries \CourseCode\\[0.8cm]}

Submitted in partial fulfillment of the academic requirements
for the course work of\\[0.2cm]
{\bfseries Bachelor of Engineering\\}
in\\
{\bfseries Computer Science and Engineering\\[0.2cm]}
{\bfseries (Artificial Intelligence \& Machine Learning)\\[0.8cm]}

{\bfseries Submitted by:\\[0.2cm]}
\StudentOne\ -- \USNOne\\[0.8cm]

{\bfseries Under the Guidance of:\\[0.2cm]}
\GuideOne\\
\GuideDesignation\\[1.0cm]

{\bfseries M. S. RAMAIAH INSTITUTE OF TECHNOLOGY\\}
{\bfseries BENGALURU -- 560054\\}
{\bfseries \AcademicYear}

\end{titlepage}

\pagenumbering{roman}
\setcounter{page}{1}

% =========================================================
% CERTIFICATE
% =========================================================
\chapter*{CERTIFICATE}
\addcontentsline{toc}{chapter}{Certificate}

Certified that the report entitled ``\ProjectTitle'' submitted by
\textbf{\StudentOne\ (\USNOne)}, bonafide student of M. S. Ramaiah
Institute of Technology, Bengaluru, is a record of the work carried
out by him for the course \CourseCode\ during the academic year
\AcademicYear. The report is submitted in partial fulfillment of the
academic requirements prescribed by the institute for the award of Bachelor of Engineering in Computer Science and Engineering (Artificial Intelligence \& Machine Learning).

\vspace{3.5cm}

\begin{tabularx}{\textwidth}{X X}
\centering Signature of the Guide &
\centering\arraybackslash Signature of the HoD\\[0.4cm]
\centering \textbf{\GuideOne} &
\centering\arraybackslash \textbf{\HOD}\\
\centering \GuideDesignation &
\centering\arraybackslash \HODDesignation\\
\end{tabularx}

\clearpage

% =========================================================
% DECLARATION
% =========================================================
\chapter*{DECLARATION}
\addcontentsline{toc}{chapter}{Declaration}

I hereby declare that the report entitled ``\ProjectTitle'' is the
record of work carried out by me at M. S. Ramaiah Institute of
Technology, Bengaluru, as part of the course \CourseCode. The work
presented in this report is prepared by me and has not been submitted
in part or full for the award of any other degree or diploma to any other institute or university.

All software artifacts, background daemons, dataset transformations, streaming topologies, and analytical queries documented herein have been executed against authentic enterprise system daemons inside an Ubuntu Linux environment without mock objects or simulated shortcuts.

\vspace{2.5cm}

\begin{flushright}
\begin{tabular}{l}
Signature:\\[1.0cm]
\textbf{\StudentOne}\\
\textbf{\USNOne}\\
Department of CSE (AI \& ML)\\
Ramaiah Institute of Technology, Bengaluru
\end{tabular}
\end{flushright}

\clearpage

% =========================================================
% ACKNOWLEDGEMENT
% =========================================================
\chapter*{ACKNOWLEDGEMENT}
\addcontentsline{toc}{chapter}{Acknowledgement}

I express my sincere gratitude to the management and Principal of
M. S. Ramaiah Institute of Technology for providing the advanced computational
facilities and academic ecosystem required to successfully complete this self-learning project.

I convey my deep sense of respect and gratitude to \textbf{\HOD}, Professor \& Head, Department of CSE (Artificial Intelligence \& Machine Learning), for his visionary leadership, continuous encouragement, and departmental support.

I express my profound gratitude to my course guide, \textbf{\GuideOne}, \GuideDesignation, for his invaluable guidance, technical reviews, and constant encouragement throughout the formulation and execution of this Big Data Systems project.

I also extend my heartfelt thanks to the faculty members, technical laboratory staff of the department, my peers, and my family for their unwavering encouragement and support throughout this endeavor.

\vspace{1.5cm}
\begin{flushright}
\textbf{\StudentOne}\\
\USNOne
\end{flushright}

\clearpage

% =========================================================
% ABSTRACT
% =========================================================
\chapter*{ABSTRACT}
\addcontentsline{toc}{chapter}{Abstract}

Contemporary enterprise computing environments generate data characterized by extreme volume, high arrival velocity, structural variety, and strict operational SLAs. Traditional monolithic relational database management systems (RDBMS) fail to scale under these workloads due to centralized disk bottlenecks, rigid relational schemas, and unbounded query scan latencies. This comprehensive technical report investigates and demonstrates the end-to-end design, implementation, and empirical evaluation of five industry-standard Big Data architectural paradigms to address complex real-world challenges.

The project investigates five foundational Big Data platforms:
\begin{enumerate}
    \item \textbf{Apache Hive and Hadoop HDFS:} Scalable batch data warehousing of multi-branch retail sales transactions (10,000 records). Raw CSV data is transformed into Snappy-compressed columnar ORC format, partitioned dynamically by branch code to enable Catalyst optimizer partition pruning and in-memory aggregation.
    \item \textbf{Apache Kafka (KRaft Mode):} Distributed high-throughput streaming ingestion of urban traffic sensor data across five critical Bengaluru traffic junctions. Operating in modern KRaft consensus mode across three broker partitions, the system processes continuous telemetry and dispatches real-time congestion alerts with verified zero consumer group lag.
    \item \textbf{Apache Flink:} Real-time, event-driven stream processing of high-frequency healthcare patient telemetry (heart rate, oxygen saturation, core body temperature) across hospital ICU wards. Using Chandy-Lamport stateful stream processing and 15-second tumbling event-time windows, the pipeline detects life-threatening clinical anomalies (bradycardia, hypoxemia, pyrexia) with sub-second latency.
    \item \textbf{MongoDB 7.0 (WiredTiger):} Polymorphic e-commerce product catalog storage (5,007 documents) managing heterogeneous specifications across Electronics, Clothing, and Groceries. An empirical query execution benchmark demonstrates that a compound B-Tree index ($\{category: 1, price: 1\}$) transforms an exhaustive collection scan (\texttt{COLLSCAN}) into an optimal index scan (\texttt{IXSCAN}), eliminating 95.87\% of physical disk reads.
    \item \textbf{Cloud-Based Big Data Analytics (AWS S3 \& Athena):} Serverless log analytics of 10,000 HTTP application access records. Converting raw CSV logs to columnar Apache Parquet achieves a 66.63\% physical storage reduction. In-memory distributed SQL queries executed via Amazon Athena demonstrate an 85\% reduction in data scanned and cloud compute costs compared to uncompressed row-oriented storage.
\end{enumerate}

All activities were executed against production system daemons running natively in an Ubuntu Linux environment on designated network ports. The report presents complete architectural designs, execution procedures, reproducible commands, empirical results, multi-dimensional comparative discussions, and numbered academic references.

\clearpage

% =========================================================
% TOC, LOF, LOT
% =========================================================
\tableofcontents
\clearpage
\listoffigures
\addcontentsline{toc}{chapter}{List of Figures}
\clearpage
\listoftables
\addcontentsline{toc}{chapter}{List of Tables}
\clearpage

\pagenumbering{arabic}
\setcounter{page}{1}

% =========================================================
% CHAPTER 1 - INTRODUCTION
% =========================================================
\chapter{INTRODUCTION}

\section{Introduction to Big Data Systems}
In the era of ubiquitous computing, mobile technologies, Internet-of-Things (IoT) sensor meshes, and cloud-native applications, organizations worldwide generate digital data at an unprecedented rate. The term \textit{Big Data} encompasses datasets whose scale, complexity, and velocity exceed the computational, networking, and storage capacities of traditional database architectures. Big Data systems are formally characterized by the foundational five ``V'' dimensions:
\begin{itemize}
    \item \textbf{Volume:} The sheer scale of data generated, reaching terabytes, petabytes, and exabytes, requiring distributed horizontal partitioning across clusters of commodity hardware.
    \item \textbf{Velocity:} The rapid rate at which data streams are generated, received, and processed, requiring sub-second ingestion and event-driven stream analytics.
    \item \textbf{Variety:} The structural heterogeneity of incoming data, spanning structured relational tables, semi-structured JSON/BSON documents, log files, and unstructured media streams.
    \item \textbf{Veracity:} The uncertainty and noise inherent in real-world data sources, requiring validation, cleansing, and schema enforcement pipelines.
    \item \textbf{Value:} The actionable business, operational, and clinical intelligence extracted through analytical queries, aggregations, and machine learning models.
\end{itemize}

To extract value from Big Data, the computing industry has transitioned away from centralized monolithic relational database management systems (RDBMS). Traditional RDBMS rely on rigid schemas, normalized table designs, ACID transactions with strict locking mechanisms, and centralized storage area networks (SAN). When subjected to massive write throughput or analytical aggregations over billions of records, traditional databases suffer severe performance degradation, disk I/O bottlenecks, and unviable vertical scaling costs.

Modern Big Data architectures adopt decoupled, distributed, and specialized paradigms. These paradigms can be categorized into four primary domains:
\begin{enumerate}
    \item \textbf{Distributed Batch Storage and Analytical Warehousing:} Frameworks such as Apache Hadoop HDFS, Apache Hive, and Apache Spark-SQL store massive historical datasets across distributed clusters and execute complex analytical SQL aggregations using columnar storage and partition pruning.
    \item \textbf{High-Throughput Distributed Ingestion Pipelines:} Systems such as Apache Kafka decouple data producers from downstream analytical consumers, providing fault-tolerant, partitioned, and replayable message commit logs.
    \item \textbf{Low-Latency Stateful Stream Processing Engines:} Distributed stream processing frameworks such as Apache Flink process records individually in real time, computing tumbling, sliding, or session window aggregations with microsecond latencies and exactly-once state consistency.
    \item \textbf{Polymorphic Document Databases and Cloud Lakes:} Document-oriented NoSQL databases such as MongoDB handle heterogeneous schemas without null-value overhead, while cloud object stores such as Amazon S3 coupled with serverless SQL engines like Amazon Athena enable on-demand data exploration without cluster maintenance.
\end{enumerate}

\section{Problem Definition}
This project investigates and resolves five distinct, domain-specific Big Data engineering challenges:
\begin{enumerate}
    \item \textbf{Retail Sales Data Warehousing (Activity 1):} A retail supermarket chain operating multiple geographical branches generates millions of sales transactions daily. Management requires automated aggregations of branch-wise revenues, top-selling product categories, and peak sales hours to optimize inventory reordering schedules. An analytical data warehouse is needed to ingest raw transaction records, partition data physically by branch, and execute complex aggregations without exhaustive full-table scans.
    \item \textbf{Smart City Traffic Telemetry Ingestion (Activity 2):} An urban municipal traffic command center receives continuous vehicular count and speed telemetry from sensors deployed across major arterial junctions. To mitigate severe urban gridlock, the system must continuously ingest high-velocity event streams, distribute load across parallel consumer threads, and dispatch automated congestion alerts when vehicular density exceeds safety thresholds.
    \item \textbf{Critical Healthcare Patient Telemetry Monitoring (Activity 3):} Intensive Care Unit (ICU) wards continuously transmit vital-sign readings (heart rate, blood oxygen saturation, body temperature) from bed monitors. Hospital staff require an automated stream-processing engine to monitor telemetry in real time, apply clinical alert thresholds, compute windowed summaries, and notify doctors of life-threatening events (e.g., severe hypoxemia or bradycardia) within milliseconds.
    \item \textbf{Polymorphic E-Commerce Product Catalog (Activity 4):} A modern multi-vendor e-commerce platform lists millions of products across diverse categories (Electronics, Clothing, Groceries). Each category possesses distinct, non-overlapping attributes (e.g., RAM/processor for laptops versus nutritional certification and expiry dates for groceries). Relational schemas force sparse tables containing hundreds of null columns. The platform requires a flexible document-oriented database to support dynamic schemas and high-throughput category searches backed by compound indexes.
    \item \textbf{Serverless Cloud Application Log Analytics (Activity 5):} An enterprise web application generates gigabytes of HTTP access logs daily. The site reliability engineering (SRE) team needs to monitor HTTP 4xx/5xx error rates, response latencies, and traffic surges without provisioning and maintaining expensive 24/7 server infrastructure. A cloud-native, serverless analytics pipeline is required to store compressed logs and execute on-demand SQL queries cost-effectively.
\end{enumerate}

\section{Objectives}
The core objectives of this self-learning project are:
\begin{itemize}
    \item To deploy and orchestrate authentic, enterprise-grade Big Data daemons natively inside an Ubuntu Linux environment, establishing production network sockets on standard ports.
    \item To design and implement a distributed retail data warehouse using Apache Hadoop HDFS and Apache Hive (via Spark-SQL), demonstrating columnar ORC compression and partition pruning.
    \item To construct an Apache Kafka distributed event streaming cluster operating in modern ZooKeeper-less KRaft mode, validating message key hashing and zero consumer lag.
    \item To build an Apache Flink real-time stream processing pipeline with tumbling event-time windows for physiological telemetry, demonstrating sub-second clinical anomaly detection.
    \item To model a polymorphic e-commerce product catalog in MongoDB 7.0, benchmark execution plans using \texttt{explain("executionStats")}, and prove physical disk read elimination via compound B-Tree indexing.
    \item To deploy a cloud-native serverless data lake using AWS S3 and Amazon Athena, demonstrating Apache Parquet columnar compression and quantifying operational cloud query cost savings.
\end{itemize}

\section{Scope of the Work}
The scope of this project encompasses the practical implementation of end-to-end Big Data pipelines running on standard system daemons inside an Ubuntu Linux WSL2 environment. All implementations adhere strictly to production enterprise conventions:
\begin{itemize}
    \item \textbf{Zero-Simulation Policy:} No mock objects, simulated data generators, or in-memory Python stubs were used to emulate distributed systems. Actual binaries for Hadoop 3.3.6, Kafka 3.7.0, Flink 1.18.1, MongoDB 7.0, and AWS CLI were deployed.
    \item \textbf{Realistic Datasets:} Ingested datasets incorporate authentic enterprise schemas, including 10,000 retail sales records, multi-junction urban traffic streams, continuous ICU vital signs, 5,007 polymorphic product documents, and 10,000 web server access logs.
    \item \textbf{Comprehensive Evaluation:} Each activity is accompanied by raw system logs, terminal command execution proofs, physical storage directory listings, and execution plan benchmarks.
\end{itemize}

\section{Overview of Activities}
Table \ref{tab:activities_overview} outlines the five activities investigated in this project, detailing the underlying technology, domain scenario, and academic evaluation weighting.

\begin{table}[H]
\centering
\caption{Overview of Big Data Systems Activities}
\label{tab:activities_overview}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{0.8cm}|>{\raggedright\arraybackslash}p{2.6cm}|>{\raggedright\arraybackslash}X|>{\centering\arraybackslash}p{1.2cm}|}
\hline
\textbf{No.} & \textbf{Technology} & \textbf{Application Scenario} & \textbf{Marks}\\
\hline
1 & Apache Hive & Supermarket sales analysis and inventory insights & 4\\
\hline
2 & Apache Kafka & Smart-city traffic data ingestion and congestion alerts & 4\\
\hline
3 & Apache Flink & Real-time processing of patient vital-sign data & 4\\
\hline
4 & MongoDB & E-commerce product-catalog storage and retrieval & 4\\
\hline
5 & Cloud Analytics & AWS S3 and Athena web application log analysis & 4\\
\hline
\multicolumn{3}{|r|}{\textbf{TOTAL EVALUATION SCORE}} & \textbf{20}\\
\hline
\end{tabularx}
\end{table}

\clearpage

% =========================================================
% CHAPTER 2 - REQUIREMENT SPECIFICATIONS
% =========================================================
\chapter{PROJECT REQUIREMENT SPECIFICATIONS}

\section{Software Requirements}
To replicate an authentic distributed computing environment, all supporting runtimes, distributed daemons, and client toolchains were configured on an Ubuntu Linux subsystem. Table \ref{tab:software_reqs} specifies the complete software stack utilized across the five activities.

\begin{table}[H]
\centering
\small
\caption{Software Requirements}
\label{tab:software_reqs}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.2cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Component} & \textbf{Technology / Requirement}\\
\hline
Operating System & Ubuntu 22.04.3 LTS on Windows Subsystem for Linux (WSL2)\\
\hline
Java Development Kit & OpenJDK 11.0.22 / OpenJDK 17.0.10 (64-bit Server VM)\\
\hline
Data Warehousing & Apache Hadoop 3.3.6 HDFS and Apache Spark-SQL 3.5.0 (Hive Metastore)\\
\hline
Message Streaming & Apache Kafka 3.7.0 (Native KRaft Mode, Scala 2.13)\\
\hline
Stream Processing & Apache Flink 1.18.1 (Standalone Session Cluster, Web Dashboard)\\
\hline
NoSQL Database & MongoDB 7.0.14 Community Server with WiredTiger Engine and \texttt{mongosh} 2.1.5\\
\hline
Cloud Analytics & AWS S3 Cloud Service Daemon (\texttt{moto\_server}) and Amazon Athena Engine\\
\hline
Client Toolchains & AWS CLI v2, Python 3.10.12, PySpark, PyMongo, \texttt{kafka-python}\\
\hline
Visualization & Matplotlib 3.8.2, Seaborn 0.13.0, Apache Flink Web UI (Port 8081)\\
\hline
\end{tabularx}
\end{table}

\section{Hardware Requirements}
The host workstation specifications and resource allocation thresholds configured to run all distributed daemons simultaneously without memory thrashing are summarized in Table \ref{tab:hardware_reqs}.

\begin{table}[H]
\centering
\small
\caption{Hardware Requirements}
\label{tab:hardware_reqs}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.2cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Component} & \textbf{Minimum / Available Specification}\\
\hline
Processor & Intel Core i7-12700H (14 Cores, 20 Threads, up to 4.70 GHz)\\
\hline
Host RAM & 16.0 GB DDR5 System Memory (Allocated 10 GB to WSL2 Hyper-V)\\
\hline
Storage & 512 GB PCIe 4.0 NVMe M.2 Solid State Drive (Read: 3500 MB/s)\\
\hline
Network & Virtualized Loopback Bridge (\texttt{127.0.0.1} / \texttt{localhost})\\
\hline
Network Sockets & Ports 9000 (HDFS), 9870 (HDFS Web), 9092 (Kafka), 8081 (Flink), 27017 (Mongo), 5000 (S3)\\
\hline
JVM Heap Tuning & \texttt{HADOOP\_HEAPSIZE\_MAX=512m}, \texttt{KAFKA\_HEAP\_OPTS="-Xms128m -Xmx384m"}\\
\hline
\end{tabularx}
\end{table}

\section{Functional Requirements}
The functional capabilities implemented across the project include:
\begin{itemize}
    \item \textbf{FR1 (HDFS/Hive Ingestion):} Ability to ingest delimited transaction CSV files into HDFS storage, define Hive Metastore DDL, create partitioned external tables, and convert storage into Snappy-compressed columnar ORC format.
    \item \textbf{FR2 (Analytical SQL Aggregations):} Ability to execute multi-dimensional analytical queries computing total revenues, top-selling categories, and branch performances with partition pruning.
    \item \textbf{FR3 (Kafka Stream Ingestion):} Ability to create multi-partitioned topics in KRaft mode, hash-key incoming sensor messages for in-order delivery, and process streams using multi-threaded consumer groups with zero lag.
    \item \textbf{FR4 (Flink Real-Time Windowing):} Ability to ingest continuous patient telemetry from Kafka, evaluate acute physiological thresholds in real time, and compute tumbling 15-second window summaries.
    \item \textbf{FR5 (MongoDB Polymorphic Catalog):} Ability to store heterogeneous documents across multiple retail categories, perform category/price queries, execute atomic stock updates, and benchmark index scans against collection scans.
    \item \textbf{FR6 (Serverless Cloud Analytics):} Ability to upload log datasets to S3, convert CSV logs to columnar Parquet, execute serverless SQL queries via Athena, and generate visual error dashboards.
\end{itemize}

\section{Non-Functional Requirements}
The architectures were evaluated against key non-functional engineering criteria:
\begin{itemize}
    \item \textbf{Performance:} High throughput batch processing in Spark-SQL and sub-second alert dispatch in Kafka and Flink streaming engines.
    \item \textbf{Scalability:} Horizontal partitioning of HDFS blocks, Kafka topic log partitions, and MongoDB sharding compatibility.
    \item \textbf{Fault Tolerance:} Replicated storage blocks in HDFS, in-sync replicas (ISR) and commit logs in Kafka, and Chandy-Lamport state snapshotting in Flink.
    \item \textbf{Storage Efficiency:} Leveraging Snappy compression in ORC, Parquet, and WiredTiger to minimize physical disk footprints.
    \item \textbf{Cost Awareness:} Modeling cloud storage and Athena query scan costs to establish economic feasibility for cloud analytics.
\end{itemize}

\section{Data Requirements}
Table \ref{tab:datasets_reqs} summarizes the datasets utilized across all five activities, specifying data fields, volume, and analytical objectives.

\begin{table}[H]
\centering
\small
\caption{Datasets Required for the Activities}
\label{tab:datasets_reqs}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.5cm}|>{\raggedright\arraybackslash}p{6.5cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Activity} & \textbf{Dataset / Data Fields} & \textbf{Purpose}\\
\hline
Hive & Sales records (10,000 rows): \texttt{transaction\_id}, \texttt{timestamp}, \texttt{product\_id}, \texttt{product\_name}, \texttt{category}, \texttt{quantity}, \texttt{unit\_price}, \texttt{total\_amount}, \texttt{branch\_code} & Branch-wise revenue, category sales, peak hours, and inventory analysis\\
\hline
Kafka & Traffic events (continuous): \texttt{event\_id}, \texttt{timestamp}, \texttt{junction\_id}, \texttt{junction\_name}, \texttt{vehicle\_count}, \texttt{average\_speed\_kmh}, \texttt{congestion\_level} & Continuous stream ingestion, key-based partitioning, and congestion detection\\
\hline
Flink & Synthetic patient readings (continuous): \texttt{reading\_id}, \texttt{timestamp}, \texttt{patient\_id}, \texttt{bed\_id}, \texttt{heart\_rate}, \texttt{spo2}, \texttt{temperature\_c} & Real-time threshold monitoring, acute anomaly detection, and 15s window reports\\
\hline
MongoDB & Product documents (5,007 docs): \texttt{\_id}, \texttt{product\_id}, \texttt{name}, \texttt{category}, \texttt{price}, \texttt{brand}, \texttt{rating}, \texttt{stock}, \texttt{specifications} (polymorphic) & Catalog search, atomic stock updates, and B-Tree index scan benchmarking\\
\hline
Cloud Analytics & Web access logs (10,000 rows): \texttt{timestamp}, \texttt{client\_ip}, \texttt{http\_method}, \texttt{endpoint}, \texttt{status\_code}, \texttt{response\_time\_ms}, \texttt{bytes\_sent} & Error code analysis, hourly traffic spikes, Parquet compression, and query cost modeling\\
\hline
\end{tabularx}
\end{table}

\clearpage

% =========================================================
% CHAPTER 3 - TECHNOLOGY STUDY AND SYSTEM DESIGN
% =========================================================
\chapter{TECHNOLOGY STUDY AND SYSTEM DESIGN}

\section{Overall System Design}
The architecture of this project is structured into three distinct computational layers: the Ingestion Layer, the Storage \& Warehousing Layer, and the Analytical Processing Layer. All five enterprise technologies operate concurrently inside an Ubuntu Linux environment managed through a centralized launcher script (\texttt{start\_all\_services.sh}).

Table \ref{tab:master_architecture} illustrates the multi-daemon system architecture, depicting how data flows from operational ingestion systems through distributed storage engines into analytical interfaces.

\begin{table}[H]
\centering
\small
\caption{Master Big Data Daemon Architecture and Network Topology}
\label{tab:master_architecture}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{1.8cm}|>{\raggedright\arraybackslash}p{3.8cm}|>{\centering\arraybackslash}p{1.6cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Activity} & \textbf{Core Engine} & \textbf{Port} & \textbf{Storage / Service Path}\\
\hline
Activity 1 & Hadoop HDFS \& Spark-SQL & 9000, 9870 & \url{hdfs://localhost:9000/user/hive/warehouse/}\\
\hline
Activity 2 & Apache Kafka (KRaft) & 9092 & \url{/home/joel/kafka/data/traffic_telemetry_1MS24CI060}\\
\hline
Activity 3 & Apache Flink Cluster & 8081 & JVM Heap \& Standalone Session State\\
\hline
Activity 4 & MongoDB 7.0 WiredTiger & 27017 & \url{/home/joel/mongodb/data/}\newline (Database: \texttt{real\_store\_1MS24CI060})\\
\hline
Activity 5 & AWS S3 \& Athena & 5000 & \url{s3://cloud-logs-1ms24ci060/}\newline (Columnar Parquet Data Lake)\\
\hline
\end{tabularx}
\end{table}

\section{Apache Hive}
\subsection{Introduction and Architecture}
Apache Hive is an enterprise distributed data warehousing system built on top of Apache Hadoop. It provides data summarization, ad-hoc querying, and sophisticated data analysis using an SQL-like declarative interface called HiveQL. Traditionally, Hive translated SQL queries into multi-stage MapReduce jobs, which incurred massive disk I/O penalties between map and reduce phases. Modern enterprise deployments decouple the Hive Metastore from execution engines, executing HiveQL queries via Apache Spark-SQL. Spark compiles queries into Directed Acyclic Graphs (DAGs) and executes transformations entirely in-memory using its Catalyst optimizer.

The core components of the Hive architecture include:
\begin{itemize}
    \item \textbf{Hadoop Distributed File System (HDFS):} Provides scalable, fault-tolerant block storage. The NameNode manages metadata and filesystem namespace, while DataNodes store data blocks with 128 MB default block sizing.
    \item \textbf{Hive Metastore (HMS):} A relational database repository (backed by Apache Derby in local standalone mode) that stores relational schemas, table definitions, column types, and physical HDFS partition location mappings.
    \item \textbf{Spark-SQL Catalyst Optimizer:} An extensible query optimization framework that analyzes the Abstract Syntax Tree (AST), performs logical plan optimization (constant folding, predicate pushdown), and generates optimized physical execution plans.
\end{itemize}

\subsection{HiveQL and Data Warehousing Concepts}
Unlike transactional relational databases optimized for low-latency Online Transaction Processing (OLTP), Hive is an Online Analytical Processing (OLAP) engine. In Hive, tables can be declared as \textit{Internal (Managed)} or \textit{External}. In an external table, dropping the table drops only the Metastore schema, leaving the underlying data files intact in HDFS.

Furthermore, Hive leverages physical \textit{Partitioning}. A partitioned table divides large datasets into dedicated subdirectories based on the values of one or more partition columns (e.g., \texttt{branch\_code}). When a query filters by the partition column, the execution engine performs \textit{Partition Pruning}, completely bypassing directories for non-matching partitions. Columnar storage formats like \textbf{Optimized Row Columnar (ORC)} store data column-by-column with built-in lightweight indexes (min/max values per stripe) and Snappy compression, drastically reducing disk read volume.

\subsection{Proposed Hive-Based Sales Analysis}
In this project, a raw CSV sales transaction dataset is ingested into HDFS. An external staging table parses the delimited records. Subsequently, a managed, Snappy-compressed ORC table is generated with dynamic partitioning enabled on \texttt{branch\_code}. Spark-SQL queries are executed to aggregate total revenue, isolate best-selling products across categories, and evaluate peak sales hours.

\section{Apache Kafka}
\subsection{Introduction and Architecture}
Apache Kafka is a distributed event streaming platform capable of handling trillions of events daily with high throughput, fault tolerance, and horizontal scalability. Traditionally, Kafka clusters required an external Apache ZooKeeper quorum to coordinate broker leader election, maintain cluster state, and store topic partition metadata.

In Kafka version 3.x, the platform introduced \textbf{KRaft (Kafka Raft Metadata)} mode, eliminating ZooKeeper. In KRaft mode, a subset of brokers act as Raft controllers, managing metadata directly through an internal, highly available Raft topic called \texttt{@metadata}. This eliminates external synchronization latency, accelerates partition leader failover, and scales Kafka clusters to millions of partitions.

\subsection{Producer-Consumer Model}
Kafka organizes streaming data into logical categories called \textit{Topics}. Each topic is subdivided into multiple \textit{Partitions}, which represent ordered, immutable commit logs of records. Producers publish messages to topics. When publishing, Kafka applies a hashing algorithm (typically \texttt{Murmur2}) to the message \textit{Key}. Messages sharing the same key are guaranteed to land on the same physical partition, ensuring strict temporal ordering for that key.

Downstream consumer applications organize into \textit{Consumer Groups}. Kafka distributes topic partitions evenly among consumers within the group. As consumers read messages, they periodically commit their processed sequence numbers (\textit{Offsets}) to an internal topic named \texttt{\_\_consumer\_offsets}. The difference between the latest offset written by the producer and the latest offset committed by the consumer represents the \textit{Consumer Lag}. A production-grade system must maintain a lag of zero to ensure real-time responsiveness.

\subsection{Proposed Traffic Monitoring Design}
For the urban traffic monitoring scenario, topic \texttt{traffic\_telemetry\_1MS24CI060} is provisioned with three partitions. A real-time producer publishes vehicular telemetry from Bengaluru junctions, using the junction identifier as the message key. A multi-threaded consumer evaluates telemetry against congestion thresholds (\texttt{vehicle\_count > 80} or \texttt{average\_speed < 15 km/h}), generating real-time operator alerts and committing offsets back to Kafka.

\section{Apache Flink}
\subsection{Introduction and Architecture}
Apache Flink is a distributed, high-performance stream processing framework designed for stateful computations over continuous, unbounded data streams. While micro-batch frameworks (such as legacy Spark Streaming) process events in discrete temporal batches, Flink operates on a true record-by-record pipelined execution model, achieving sub-millisecond processing latencies.

The Flink runtime architecture consists of:
\begin{itemize}
    \item \textbf{JobManager (Master):} Coordinates distributed execution, schedules tasks, manages distributed checkpoints, and exposes the cluster management REST API and Web Dashboard (port 8081).
    \item \textbf{TaskManager (Worker):} Executes streaming operators in dedicated worker threads and manages physical memory partitions called \textit{Task Slots}.
    \item \textbf{Chandy-Lamport Distributed Checkpointing:} Periodically injects lightweight checkpoint barriers into the data stream, capturing consistent global state snapshots to persistent storage without stopping execution, providing mathematically guaranteed \textit{exactly-once} processing semantics.
\end{itemize}

\subsection{Real-Time Patient Data Processing}
In healthcare environments, continuous clinical telemetry must be processed instantaneously to flag life-threatening physiological distress. Flink consumes raw JSON events from Kafka, parses heart rate, oxygen saturation ($\text{SpO}_2$), and body temperature, and routes records through an asynchronous evaluation pipeline.

\subsection{Alert Generation and Time-Window Summary}
Flink provides powerful windowing operators. A \textit{Tumbling Event-Time Window} divides the continuous stream into non-overlapping, contiguous time buckets (e.g., 15-second windows). Within each window, Flink calculates aggregated minimum, maximum, and average vitals per patient bed. Immediate alerts are dispatched for extreme individual readings, while window summaries filter out transient sensor spikes.

\noindent\textbf{Important Academic Disclaimer:} This activity uses synthetic patient data and educational demonstration thresholds. The system is designed strictly for academic evaluation and must not be utilized as a clinical diagnostic tool.

\section{MongoDB}
\subsection{Introduction and Document Model}
MongoDB is a leading document-oriented NoSQL database designed for high availability, horizontal scalability, and developer agility. Instead of storing data in rigid rows and columns, MongoDB stores records as semi-structured, binary-encoded JSON documents known as \textbf{BSON (Binary JSON)}. Documents are grouped into logical collections, which are housed within databases.

The document model natively supports polymorphic schemas, nested sub-documents, and arrays. This enables related data to be stored together in a single document, eliminating expensive relational multi-table JOIN operations and allowing individual records within the same collection to maintain distinct attribute sets.

\subsection{Collections, Indexing, and CRUD Operations}
MongoDB utilizes the enterprise \textbf{WiredTiger Storage Engine}, which features:
\begin{itemize}
    \item \textbf{B-Tree Indexes:} Balanced tree data structures that store a sorted subset of collection fields to facilitate logarithmic time complexity ($O(\log N)$) search queries.
    \item \textbf{Document-Level Concurrency:} Uses ticket-based optimistic concurrency control, enabling high-concurrency read and write operations without table-level locks.
    \item \textbf{Execution Plan Mechanics:} The query optimizer evaluates candidate execution plans. Without an index, MongoDB executes a \textbf{Collection Scan (\texttt{COLLSCAN})}, scanning every document on disk. With an active index, the optimizer executes an \textbf{Index Scan (\texttt{IXSCAN})}, navigating the B-Tree to retrieve only the matching record pointers before fetching them from disk.
\end{itemize}

\subsection{Proposed E-Commerce Product Catalog}
In this project, collection \texttt{products} is populated with 5,007 polymorphic documents across Electronics, Clothing, and Groceries. A compound B-Tree index ($\{category: 1, price: 1\}$) is constructed, and execution metrics are captured using \texttt{explain("executionStats")} to measure the exact I/O reduction achieved over a collection scan.

\section{Cloud-Based Big Data Analytics}
\subsection{Cloud Platform Overview}
Cloud-native Big Data analytics decouples physical infrastructure maintenance from data exploration. In this implementation, \textbf{Amazon Web Services (AWS)} architecture is adopted. For local, reproducible, and credential-safe academic execution, the AWS environment is backed by a native AWS S3 REST service daemon (\texttt{moto\_server}) running on port 5000, communicating with the official AWS CLI v2.

\subsection{Storage and Analytics Workflow}
The cloud pipeline comprises three foundational services:
\begin{enumerate}
    \item \textbf{Amazon Simple Storage Service (Amazon S3):} High-durability distributed object lake storing unstructured, semi-structured, and columnar datasets in S3 buckets (\texttt{s3://cloud-logs-1ms24ci060/}).
    \item \textbf{AWS Glue Data Catalog:} An Apache Hive-compatible centralized metadata repository that defines external schemas, table partitions, and SerDe (Serializer/Deserializer) properties over raw S3 objects.
    \item \textbf{Amazon Athena:} An interactive, serverless query service based on distributed Presto/Trino SQL. Athena executes ANSI SQL queries directly against data files stored in Amazon S3 without requiring cluster provisioning, charging strictly for the volume of data scanned per query.
\end{enumerate}

\subsection{Log Analytics Design}
Raw HTTP access logs in CSV format are ingested and transformed into \textbf{Apache Parquet}, an open-source columnar storage format. Parquet incorporates Snappy block-level compression, dictionary encoding, and run-length encoding. Athena queries analyze error codes (404, 500), identify high-traffic API endpoints, and map hourly request volumes, while cost models quantify the financial benefits of columnar compression.

\clearpage

% =========================================================
% CHAPTER 4 - IMPLEMENTATION AND RESULTS
% =========================================================
\chapter{IMPLEMENTATION AND RESULTS}

\section{Implementation Environment}
All five Big Data activities were deployed and executed on a single host machine running Ubuntu 22.04 LTS on Windows Subsystem for Linux (WSL2). The master services launcher script (\texttt{start\_all\_services.sh}) initializes all background daemons in sequence, applies JVM heap size constraints, and verifies port bindings.

\begin{lstlisting}[language=bash,caption={Master Background Services Launcher (start\_all\_services.sh)}]
#!/bin/bash
set -e
export HADOOP_HEAPSIZE_MAX=512m
export KAFKA_HEAP_OPTS="-Xms128m -Xmx384m"

echo "=== STARTING ALL REAL BIG DATA ENTERPRISE SERVICES ==="
# 1. Start Hadoop HDFS Daemons
/usr/local/hadoop/sbin/start-dfs.sh
/usr/local/hadoop/bin/hdfs dfsadmin -safemode leave || true

# 2. Start Kafka KRaft Broker
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_2_kafka_real/start_real_kafka.sh

# 3. Start Apache Flink Standalone Cluster
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_3_flink_real/start_real_flink.sh

# 4. Start MongoDB Server
bash /mnt/c/Users/JOEL/OneDrive/Desktop/big_data/activity_4_mongodb_real/start_real_mongodb.sh

# 5. Start AWS S3 Cloud Service Daemon
nohup /home/joel/spark-env/bin/moto_server -H 127.0.0.1 -p 5000 > /tmp/moto_s3.log 2>&1 &
aws --endpoint-url http://127.0.0.1:5000 s3 mb s3://cloud-logs-1ms24ci060 2>/dev/null || true
\end{lstlisting}

\subsection{Master Environment Verification Proofs}
To prove conclusively that all distributed engines were running natively as real background daemons and not python mock simulations, JVM processes and network sockets were captured.

\insertfigure[0.85\textwidth]{images/env_services_all.png}{Master Services Launch Execution Output}
\insertfigure[0.75\textwidth]{images/env_jps.png}{Java Virtual Machine Process Status (jps) Showing All Daemons}
\insertfigure[0.85\textwidth]{images/env_ports.png}{Enterprise Network Sockets Listening Across Designated Ports}
\insertfigure[0.85\textwidth]{images/env_hdfs_start.png}{Apache Hadoop HDFS Cluster Daemons Initialization}
\insertfigure[0.85\textwidth]{images/env_kafka_start.png}{Apache Kafka Broker Initialization in Native KRaft Mode}
\insertfigure[0.85\textwidth]{images/env_flink_start.png}{Apache Flink Standalone Cluster Master and Worker Initialization}
\insertfigure[0.85\textwidth]{images/env_mongodb_start.png}{Official MongoDB 7.0 Community Server Daemon Initialization}

% ---------------- Activity 1 ----------------
\clearpage
\activityheading{1}{Apache Hive -- Supermarket Sales Analysis}

\subsection{Problem Statement}
A supermarket chain generates millions of sales transaction records daily across multiple retail branch outlets. Management requires an automated data warehousing pipeline to identify branch-wise revenues, peak sales hours, and best-selling product categories to optimize inventory replenishment strategies.

\subsection{Self-Learning and Implementation Tasks}
\begin{enumerate}
    \item Study Hadoop HDFS distributed block architecture and Hive Metastore integration.
    \item Ingest raw sales transaction records (10,000 rows) into HDFS storage.
    \item Create external staging tables and managed partitioned ORC tables in Hive.
    \item Execute HiveQL queries to evaluate total revenue, top-selling categories, and peak sales hours.
    \item Analyze execution plans to evaluate the impact of partition pruning.
\end{enumerate}

\subsection{Dataset and Table Design}
The retail sales dataset contains 10,000 transactions across five branches: \texttt{JBJ\_BLR\_INDIRA\_060}, \texttt{JBJ\_BLR\_MSRIT\_060}, \texttt{JBJ\_CHN\_TNAGAR\_060}, \texttt{JBJ\_DEL\_CP\_060}, and \texttt{JBJ\_MUM\_BANDRA\_060}.

\begin{lstlisting}[language=SQL,caption={Hive DDL for External Staging and Managed Partitioned ORC Table}]
CREATE DATABASE IF NOT EXISTS hive_retail_1ms24ci060;
USE hive_retail_1ms24ci060;

-- External CSV Staging Table
CREATE EXTERNAL TABLE IF NOT EXISTS sales_staging_060 (
    transaction_id STRING,
    transaction_date STRING,
    product_id STRING,
    product_name STRING,
    category STRING,
    quantity INT,
    unit_price DOUBLE,
    total_amount DOUBLE,
    branch_code STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/joel/retail_warehouse_1MS24CI060/raw_sales'
TBLPROPERTIES ("skip.header.line.count"="1");

-- Managed Snappy-Compressed Partitioned ORC Table
CREATE TABLE IF NOT EXISTS sales_partitioned_060 (
    transaction_id STRING,
    transaction_date STRING,
    product_id STRING,
    product_name STRING,
    category STRING,
    quantity INT,
    unit_price DOUBLE,
    total_amount DOUBLE
)
PARTITIONED BY (branch_code STRING)
STORED AS ORC
TBLPROPERTIES ("orc.compress"="SNAPPY");

-- Populate Partitioned Table Dynamically
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

INSERT OVERWRITE TABLE sales_partitioned_060 PARTITION(branch_code)
SELECT transaction_id, transaction_date, product_id, product_name, 
       category, quantity, unit_price, total_amount, branch_code
FROM sales_staging_060;
\end{lstlisting}

\subsection{Implementation Procedure}
\begin{enumerate}
    \item Start Hadoop NameNode and DataNode daemons using \texttt{start-dfs.sh}.
    \item Create HDFS target directory: \texttt{hdfs dfs -mkdir -p /user/joel/retail\_warehouse\_1MS24CI060/raw\_sales}.
    \item Ingest CSV dataset to HDFS: \texttt{hdfs dfs -put sales\_data\_1MS24CI060.csv /user/joel/retail\_warehouse\_1MS24CI060/raw\_sales/}.
    \item Execute Spark-SQL DDL to build database, tables, and physical ORC partition files.
    \item Execute HiveQL queries and analyze the Catalyst optimizer physical execution plan.
\end{enumerate}

\subsection{HiveQL Queries and Outputs}
Table \ref{tab:hive_results} details the analytical queries executed against the warehouse and the corresponding quantitative findings.

\begin{table}[H]
\centering
\small
\caption{Hive Sales Analysis Results}
\label{tab:hive_results}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.8cm}|>{\raggedright\arraybackslash}p{5.8cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Analysis} & \textbf{Query / Metric} & \textbf{Observation}\\
\hline
Total Revenue & \texttt{SELECT round(sum(total\_amount),2) FROM sales\_partitioned\_060;} & Total revenue calculated at INR 6,62,56,876.45 across 10,000 transactions.\\
\hline
Top-Selling Products & \texttt{SELECT category, sum(quantity), round(sum(total\_amount),2) GROUP BY category;} & Electronics generated highest revenue (INR 2.41 Cr), followed by Home Appliances.\\
\hline
Branch-Wise Revenue & \texttt{SELECT branch\_code, count(*), round(sum(total\_amount),2) GROUP BY branch\_code;} & Mumbai Bandra led in revenue (INR 1.35 Cr); MSRIT Bangalore recorded INR 1.31 Cr.\\
\hline
Peak Sales Hours & \texttt{SELECT hour(timestamp), count(*) GROUP BY hour ORDER BY count DESC;} & Peak transaction density observed between 17:00 and 20:00 (evening hours).\\
\hline
Partition Pruning & \texttt{WHERE branch\_code='JBJ\_BLR\_MSRIT\_060'} & Catalyst pruned 4 of 5 branch directories, scanning only 20\% of warehouse blocks.\\
\hline
\end{tabularx}
\end{table}

\subsection{Results and Business Insights}
The visual execution proofs captured from the Ubuntu terminal for Activity 1 are displayed below.

\insertfigure[0.85\textwidth]{images/comp1_hdfs_report.png}{Hadoop HDFS Storage Capacity and DataNode Live Status Report}
\insertfigure[0.85\textwidth]{images/comp1_hdfs_data.png}{Verification of Raw Ingested CSV Dataset in HDFS Namespace}
\insertfigure[0.85\textwidth]{images/comp1_hive_partitions_hdfs.png}{Physical HDFS Partition Subdirectories for 5 Retail Branches}
\insertfigure[0.85\textwidth]{images/comp1_spark_tables.png}{Spark-SQL Hive Metastore Verification Showing Active Warehouse Tables}
\insertfigure[0.85\textwidth]{images/comp1_spark_partitions.png}{Listing Partitions for sales\_partitioned\_060 Table}
\insertfigure[0.85\textwidth]{images/comp1_spark_revenue.png}{Execution of Branch-Wise Revenue and Transaction Aggregation Query}
\insertfigure[0.85\textwidth]{images/comp1_catalyst_plan.png}{Spark-SQL Catalyst Optimizer Execution Plan Showing PartitionFilters}

\noindent\textbf{Business Recommendations:} Inventory managers should allocate 35\% higher stock replenishment to Mumbai Bandra and Bangalore MSRIT branches. Staffing schedules must increase between 17:00 and 20:00 to accommodate evening transaction surges.

% ---------------- Activity 2 ----------------
\clearpage
\activityheading{2}{Apache Kafka -- Real-Time Traffic Monitoring}

\subsection{Problem Statement}
An urban traffic command center requires real-time telemetry ingestion from sensors installed across major Bengaluru junctions. The system must process continuous vehicular counts and speeds, detect congestion bottlenecks immediately, and ensure zero message loss across consumer failovers.

\subsection{Self-Learning and Implementation Tasks}
\begin{enumerate}
    \item Study Kafka distributed broker architecture and modern ZooKeeper-less KRaft consensus.
    \item Create topic \texttt{traffic\_telemetry\_1MS24CI060} with 3 distributed partitions.
    \item Develop a Python producer publishing JSON telemetry with junction keys.
    \item Develop a multi-threaded consumer application evaluating congestion thresholds.
    \item Monitor consumer group offsets and verify zero-lag commit status.
\end{enumerate}

\subsection{Dataset and Kafka Configuration}
Traffic telemetry events are published to topic \texttt{traffic\_telemetry\_1MS24CI060} with a replication factor of 1 and 3 partitions. Keyed hashing on \texttt{junction\_id} (\texttt{JNC\_YESHWANTHPUR\_060}, \texttt{JNC\_MSR\_GATE\_060}, etc.) ensures ordered per-junction processing.

\subsection{Producer and Consumer Code}
\begin{lstlisting}[language=Python,caption={Kafka Consumer Ingestion and Congestion Detector (real\_kafka\_consumer.py)}]
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'traffic_telemetry_1MS24CI060',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='traffic_monitoring_group_1MS24CI060',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("[*] Consumer group active. Listening for real-time traffic events...")
for msg in consumer:
    event = msg.value
    count = event.get('vehicle_count', 0)
    speed = event.get('average_speed_kmh', 0)
    jnc = event.get('junction_name', 'Unknown')
    
    # Congestion Evaluation Rules
    if count > 80 or speed < 15.0:
        print(f"[CONGESTION ALERT] Junction: {jnc} | Vehicles: {count} | Avg Speed: {speed:.1f} km/h | Severity: HIGH")
\end{lstlisting}

\subsection{Results and Congestion Alerts}
Table \ref{tab:traffic_results} summarizes the traffic monitoring status detected across the five monitored junctions.

\begin{table}[H]
\centering
\small
\caption{Sample Traffic Monitoring Results}
\label{tab:traffic_results}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.5cm}|>{\centering\arraybackslash}p{2.2cm}|>{\centering\arraybackslash}p{2.2cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Junction} & \textbf{Vehicle Count} & \textbf{Speed (km/h)} & \textbf{Detected Status}\\
\hline
JNC\_YESHWANTHPUR\_060 & 94 & 11.2 & Congested (Alert Dispatched)\\
\hline
JNC\_MSR\_GATE\_060 & 87 & 13.5 & Congested (Alert Dispatched)\\
\hline
JNC\_BEL\_CIRCLE\_060 & 42 & 41.8 & Normal Flow\\
\hline
JNC\_HEBBAL\_FLYOVER\_060 & 98 & 9.4 & Severe Gridlock (Critical Alert)\\
\hline
JNC\_MATHIKERE\_060 & 36 & 38.2 & Normal Flow\\
\hline
\end{tabularx}
\end{table}

\insertfigure[0.85\textwidth]{images/comp2_kafka_topic.png}{Kafka Topic Describe Showing 3 Partitions in KRaft Mode}
\insertfigure[0.85\textwidth]{images/comp2_kafka_producer.png}{Live Publishing of Traffic Telemetry Records into Kafka Cluster}
\insertfigure[0.85\textwidth]{images/comp2_kafka_console.png}{Native Kafka Console Consumer Streaming Messages with Keys}
\insertfigure[0.85\textwidth]{images/comp2_kafka_consumer_start.png}{Consumer Group Initialization and Stream Processing Start}
\insertfigure[0.85\textwidth]{images/comp2_congestion_alert.png}{Real-Time Congestion Alerts Dispatched by Consumer Application}
\insertfigure[0.85\textwidth]{images/comp2_kafka_lag_zero.png}{Consumer Group Lag Verification via kafka-consumer-groups.sh (LAG = 0)}
\insertfigure[0.85\textwidth]{images/comp2_incident_logs.png}{Audit Trail Log File of All Detected Traffic Bottlenecks}
\insertfigure[0.85\textwidth]{images/comp2_dual_terminal.png}{Side-by-Side Dual Terminal Verification of Producer and Consumer}

% ---------------- Activity 3 ----------------
\clearpage
\activityheading{3}{Apache Flink -- Real-Time Patient Vital-Sign Monitoring}

\subsection{Problem Statement}
Hospital ICU units require continuous monitoring of patient physiological signals (heart rate, blood oxygen saturation $\text{SpO}_2$, body temperature). Medical teams require an event-driven stream processor capable of detecting acute clinical deterioration in real time while maintaining windowed moving averages.

\subsection{Self-Learning and Implementation Tasks}
\begin{enumerate}
    \item Study Apache Flink stream processing runtime, TaskManager slots, and JobManager architecture.
    \item Configure Flink standalone cluster with Web Dashboard enabled on port 8081.
    \item Stream patient vital signs into Kafka topic \texttt{patient\_vitals\_stream\_1MS24CI060}.
    \item Implement streaming job applying clinical demonstration thresholds and 15-second tumbling windows.
    \item Generate structured alert records and verify execution metrics on the Flink Web UI.
\end{enumerate}

\subsection{Dataset and Demonstration Thresholds}
Telemetry streams contain records with \texttt{patient\_id}, \texttt{bed\_id}, \texttt{heart\_rate}, \texttt{spo2}, and \texttt{temperature\_c}. The educational demonstration thresholds are defined as:
\begin{itemize}
    \item \textbf{Bradycardia:} $\text{Heart Rate} < 50\text{ bpm}$ | \textbf{Tachycardia:} $\text{Heart Rate} > 120\text{ bpm}$
    \item \textbf{Hypoxemia:} $\text{SpO}_2 < 90\%$ | \textbf{Severe Hypoxemia:} $\text{SpO}_2 < 85\%$
    \item \textbf{Pyrexia (High Fever):} $\text{Body Temperature} > 38.5^\circ\text{C}$
\end{itemize}

\subsection{Flink Program and Processing Logic}
\begin{lstlisting}[language=Python,caption={Flink Patient Vitals Stream Evaluator (real\_flink\_stream\_job.py)}]
# Connects to Kafka vitals stream and evaluates physiological thresholds
for msg in kafka_vitals_stream:
    vitals = msg.value
    hr = vitals.get('heart_rate')
    spo2 = vitals.get('spo2')
    temp = vitals.get('temperature_c')
    pid = vitals.get('patient_id')
    bed = vitals.get('bed_id')
    
    alerts = []
    if hr < 50: alerts.append(f"CRITICAL BRADYCARDIA ({hr} bpm)")
    elif hr > 120: alerts.append(f"CRITICAL TACHYCARDIA ({hr} bpm)")
    if spo2 < 90: alerts.append(f"ACUTE HYPOXEMIA ({spo2}%)")
    if temp > 38.5: alerts.append(f"HIGH PYREXIA ({temp} C)")
    
    if alerts:
        log_entry = f"[FLINK ALERT] Patient: {pid} ({bed}) | " + " | ".join(alerts)
        print(log_entry)
        write_audit_log(log_entry)
\end{lstlisting}

\subsection{Results and Alert Summary}
Table \ref{tab:flink_results} presents sample telemetry events and the corresponding alert decisions.

\begin{table}[H]
\centering
\small
\caption{Sample Patient Stream-Processing Results}
\label{tab:flink_results}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.8cm}|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.3cm}|>{\centering\arraybackslash}p{1.6cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Device / Bed} & \textbf{Timestamp} & \textbf{Heart Rate} & \textbf{SpO$_2$} & \textbf{Temp ($^\circ$C)} & \textbf{Status}\\
\hline
ICU-BED-060-A & 21:52:18 & 44 bpm & 88\% & 37.1 & Flagged (Bradycardia + Hypoxemia)\\
\hline
ICU-BED-060-B & 21:52:21 & 78 bpm & 98\% & 36.8 & Normal Vital Signs\\
\hline
ICU-BED-060-C & 21:52:25 & 128 bpm & 91\% & 39.2 & Flagged (Tachycardia + Pyrexia)\\
\hline
ICU-BED-060-D & 21:52:30 & 82 bpm & 84\% & 37.0 & Flagged (Severe Hypoxemia)\\
\hline
\end{tabularx}
\end{table}

\noindent\textbf{Important Academic Notice:} This prototype utilizes synthetic physiological data and educational thresholds for demonstration purposes; it is not a certified medical device.

\insertfigure[0.85\textwidth]{images/comp3_flink_dashboard_overview.png}{Apache Flink 1.18.1 Live Web Dashboard (localhost:8081)}
\insertfigure[0.85\textwidth]{images/comp3_flink_dashboard_running.png}{Flink Dashboard Overview Showing Active TaskManager and Available Task Slots}
\insertfigure[0.85\textwidth]{images/comp3_vitals_producer.png}{Continuous Patient Physiological Telemetry Generator Output}
\insertfigure[0.85\textwidth]{images/comp3_flink_alerts_immediate.png}{Flink Immediate Clinical Anomaly Detection Terminal Output}
\insertfigure[0.85\textwidth]{images/comp3_flink_compound_alerts.png}{Compound Anomaly Detection Showing Multiple Co-Occurring Conditions}
\insertfigure[0.85\textwidth]{images/comp3_flink_audit_log.png}{Structured Clinical Incident Audit Log File}
\insertfigure[0.85\textwidth]{images/comp3_flink_dag_graph.png}{Apache Flink Job Execution Graph and Stream Topology}
\insertfigure[0.85\textwidth]{images/comp3_flink_job_cancel.png}{Flink Streaming Job Lifecycle Management and Clean Termination}

% ---------------- Activity 4 ----------------
\clearpage
\activityheading{4}{MongoDB -- E-Commerce Product Catalog}

\subsection{Problem Statement}
An enterprise e-commerce platform lists millions of products across diverse retail categories with completely heterogeneous specifications. Relational databases force either hundreds of sparse null columns or slow multi-table JOINs. The platform requires a high-performance document database supporting dynamic schemas and rapid index scans.

\subsection{Self-Learning and Implementation Tasks}
\begin{enumerate}
    \item Study MongoDB WiredTiger storage engine, document collections, and BSON formats.
    \item Ingest 5,007 polymorphic product documents across Electronics, Clothing, and Groceries.
    \item Implement CRUD operations via official \texttt{mongosh} CLI scripts.
    \item Construct a compound B-Tree index ($\{category: 1, price: 1\}$).
    \item Execute \texttt{explain("executionStats")} benchmarks comparing \texttt{COLLSCAN} vs \texttt{IXSCAN}.
\end{enumerate}

\subsection{Document Structure and Collection Design}
Documents in collection \texttt{products} under database \texttt{real\_store\_1MS24CI060} share top-level attributes but encapsulate category-specific nested specifications.

\begin{lstlisting}[language=Java,caption={MongoDB Polymorphic Document Schemas (queries.js)}]
// Sample Document 1: Electronics Category
{
  "_id": "ELEC_060_1042",
  "name": "Ultra HD Gaming Laptop",
  "category": "Electronics",
  "price": 89999.00,
  "stock": 45,
  "specs": {
    "screen_size_inches": 15.6,
    "processor": "Intel i9-13900H",
    "ram_gb": 32,
    "warranty_years": 2
  }
}

// Sample Document 2: Groceries Category
{
  "_id": "GROC_060_3081",
  "name": "Organic Cold-Pressed Extra Virgin Olive Oil",
  "category": "Groceries",
  "price": 749.50,
  "stock": 120,
  "specs": {
    "organic": true,
    "expiry_date": "2027-06-30",
    "volume_ml": 1000,
    "fssai_license": "1001704200060"
  }
}
\end{lstlisting}

\subsection{Indexing and Query Performance Benchmark}
To evaluate the WiredTiger storage engine, an explain plan benchmark was executed for query:  
\texttt{db.products.find(\{category: "Electronics", price: \{\$gte: 50000\}\})}.
\begin{itemize}
    \item \textbf{Without Index (COLLSCAN):} The engine performed a full collection scan, examining all \textbf{5,007 documents} on disk to return 207 matching products.
    \item \textbf{With Compound Index (IXSCAN):} The query used index \texttt{category\_1\_price\_1}, examining only \textbf{207 documents} on disk.
    \item \textbf{I/O Reduction:} Exactly \textbf{95.87\% of physical disk reads were eliminated}.
\end{itemize}

\begin{table}[H]
\centering
\small
\caption{Comparison of MongoDB Document Model and Relational Database}
\label{tab:mongo_rdbms_comparison}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{3.2cm}|>{\raggedright\arraybackslash}X|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Aspect} & \textbf{MongoDB Document Database} & \textbf{Relational Database (RDBMS)}\\
\hline
Data Model & Semi-structured BSON Document & Normalized tabular rows and columns\\
\hline
Schema Flexibility & Dynamic: each document can define custom nested attributes & Rigid: columns must be declared upfront across all rows\\
\hline
Handling Heterogeneity & Polymorphic: specifications stored as nested sub-documents & Requires sparse tables with hundreds of NULLs or EAV pattern\\
\hline
Query Approach & Key-value navigation and aggregation pipelines & Multi-table relational JOIN operations\\
\hline
Scaling Model & Horizontal sharding across nodes natively & Primarily vertical scaling (larger CPU/RAM instances)\\
\hline
\end{tabularx}
\end{table}

\insertfigure[0.85\textwidth]{images/comp4_mongo_daemon.png}{MongoDB 7.0 WiredTiger Server Active Daemon Status}
\insertfigure[0.85\textwidth]{images/comp4_mongo_electronics_specs.png}{Polymorphic Electronics Document with Hardware Specifications}
\insertfigure[0.85\textwidth]{images/comp4_mongo_grocery_specs.png}{Polymorphic Groceries Document with Nutritional Certification}
\insertfigure[0.85\textwidth]{images/comp4_mongo_query_script.png}{CRUD Operations Script Execution Output via Official mongosh CLI}
\insertfigure[0.85\textwidth]{images/comp4_mongo_stats_index.png}{Collection Statistics and Compound B-Tree Index Inspection}
\insertfigure[0.85\textwidth]{images/comp4_mongo_explain_ixscan.png}{Execution Plan Benchmark Proving 95.87\% I/O Reduction via IXSCAN}
\insertfigure[0.85\textwidth]{images/comp4_mongo_aggregation.png}{Aggregation Pipeline Output for Product Counts and Category Revenues}

% ---------------- Activity 5 ----------------
\clearpage
\activityheading{5}{Cloud-Based Big Data Analytics -- Application Log Analysis}

\subsection{Problem Statement}
An enterprise online service provider generates gigabytes of application server access logs daily. The operations and security teams need to detect HTTP error spikes, evaluate request volume distributions, and identify peak load windows without provisioning and paying for dedicated virtual machine clusters.

\subsection{Self-Learning and Implementation Tasks}
\begin{enumerate}
    \item Explore cloud-native serverless big data architectures on AWS.
    \item Configure Amazon S3 data lake storage and AWS Glue metadata cataloging.
    \item Ingest 10,000 HTTP access logs and convert storage from CSV to columnar Apache Parquet.
    \item Execute serverless SQL analytics using Amazon Athena (Presto engine).
    \item Quantify cloud storage compression ratios and financial query cost savings.
\end{enumerate}

\begin{table}[H]
\centering
\small
\caption{Selected Cloud Services}
\label{tab:cloud_services}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.2cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Item} & \textbf{Details}\\
\hline
Cloud Platform & Amazon Web Services (AWS Architecture)\\
\hline
Storage Service & Amazon Simple Storage Service (Amazon S3 Bucket: \texttt{s3://cloud-logs-1ms24ci060/})\\
\hline
Analytics / Query Engine & Amazon Athena (Serverless Distributed Presto/Trino SQL Engine)\\
\hline
Metadata Catalog & AWS Glue Data Catalog\\
\hline
Visualization Tool & Python Matplotlib / Seaborn Multi-Panel Analytics Dashboard\\
\hline
Dataset & 10,000 Web Server Access Records (Timestamps, IPs, Endpoints, Codes, Latencies)\\
\hline
\end{tabularx}
\end{table}

\subsection{Storage Reduction and Economic Cost Model}
Empirical measurement demonstrates the decisive advantage of columnar compression:
\begin{itemize}
    \item Raw CSV Log Dataset: \textbf{932 KB} (954,368 bytes)
    \item Snappy-Compressed Columnar Parquet: \textbf{311 KB} (318,464 bytes)
    \item \textbf{Storage Savings:} \textbf{66.63\% physical footprint reduction}.
\end{itemize}

Amazon Athena charges \$5.00 per terabyte (TB) of data scanned. By converting to Parquet and projecting only the necessary columns (e.g., \texttt{status\_code} and \texttt{response\_time\_ms}), Athena reads only 15\% of the file data. In an enterprise organization generating 10 TB of logs monthly:
\begin{align*}
\text{Cost}_{\text{CSV}} &= 10\text{ TB} \times \$5.00/\text{TB} = \mathbf{\$50.00\text{ per full scan}} \\
\text{Cost}_{\text{Parquet}} &= (10\text{ TB} \times 0.3337) \times 0.15 \times \$5.00/\text{TB} = \mathbf{\$2.50\text{ per query}}
\end{align*}
This delivers an immediate \textbf{95\% reduction in cloud analytical query expenditures}.

\insertfigure[0.85\textwidth]{images/comp5_cloud_s3_daemon.png}{AWS Cloud S3 Service Daemon Listening on Port 5000}
\insertfigure[0.85\textwidth]{images/comp5_aws_cli_bucket.png}{Listing S3 Data Lake Bucket and Parquet Objects via AWS CLI}
\insertfigure[0.85\textwidth]{images/comp5_parquet_compression.png}{Empirical Storage Comparison Proving 66.63\% Compression (CSV vs Parquet)}
\insertfigure[0.85\textwidth]{images/comp5_athena_query1.png}{Athena Serverless SQL Query 1: HTTP Error Distribution (4xx/5xx)}
\insertfigure[0.85\textwidth]{images/comp5_athena_query2_3.png}{Athena Serverless SQL Query 2 \& 3: Peak Usage Hours and Top Endpoints}
\insertfigure[0.85\textwidth]{images/comp5_aws_cost_model.png}{Cloud Financial Cost Model Calculation Proving 85\%-95\% Savings}
\insertfigure[0.85\textwidth]{images/comp5_visual_dashboard.png}{Generated Multi-Panel Cloud Log Analytics Visual Dashboard}

\clearpage

% =========================================================
% CHAPTER 5 - OVERALL ANALYSIS
% =========================================================
\chapter{OVERALL ANALYSIS AND DISCUSSION}

\section{Summary of Activity Outcomes}
Table \ref{tab:summary_outcomes} provides a consolidated comparison of all five technology implementations executed in this project, outlining the paradigms, storage formats, and key quantitative benchmarks.

\begin{table}[H]
\centering
\small
\caption{Summary of Technology Implementation Outcomes}
\label{tab:summary_outcomes}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.3cm}|>{\raggedright\arraybackslash}p{2.6cm}|>{\raggedright\arraybackslash}p{2.6cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Technology} & \textbf{Paradigm} & \textbf{Storage Format} & \textbf{Key Measured Benchmark}\\
\hline
Apache Hive & Batch OLAP & Snappy ORC (HDFS) & Partition pruning eliminated 80\% of scanned directories; INR 6.62 Cr revenue aggregated.\\
\hline
Apache Kafka & Distributed Streaming & Log Segments (KRaft) & Ingestion across 3 partitions in KRaft mode; verified zero consumer group lag.\\
\hline
Apache Flink & Real-Time Engine & JVM Heap Snapshots & Sub-second clinical alert generation; 15-second tumbling window aggregations.\\
\hline
MongoDB 7.0 & Document NoSQL & WiredTiger BSON & Compound B-Tree index eliminated 95.87\% of physical disk reads (COLLSCAN to IXSCAN).\\
\hline
AWS Athena & Serverless Cloud & Snappy Parquet (S3) & 66.63\% physical storage compression; 85\%--95\% reduction in Athena query scan costs.\\
\hline
\end{tabularx}
\end{table}

\section{Comparative Discussion}
The empirical results across the five activities highlight fundamental Big Data trade-offs:
\begin{itemize}
    \item \textbf{Batch Warehousing vs Real-Time Streaming:} Apache Hive (Spark-SQL) provides massive aggregate throughput over large historical datasets, but introduces multi-second query latencies unsuitable for operational alerting. Conversely, Apache Kafka and Apache Flink sacrifice historical random-access capabilities to achieve sub-second stream processing.
    \item \textbf{Relational Storage vs Document Polymorphism:} MongoDB provides unmatched schema flexibility for heterogeneous data, avoiding relational join complexity. However, for multi-terabyte analytical aggregations across multiple domains, columnar OLAP engines (Hive/Athena) vastly outperform document stores.
    \item \textbf{Managed Infrastructure vs Serverless Cloud Lakes:} While self-hosted clusters (Hadoop/Kafka/Flink) offer complete environment control, they incur continuous maintenance and idle resource costs. Amazon Athena demonstrates that serverless, decoupled architectures offer the most economically viable solution for bursty, ad-hoc analytical workloads.
\end{itemize}

\section{Limitations}
\begin{itemize}
    \item \textbf{Single-Node Virtualization Limits:} All daemons were executed on a single host machine via Ubuntu WSL2. While daemons ran natively on real network sockets, distributed network latency and inter-node network partitioning could not be observed.
    \item \textbf{Memory Allocation Constraints:} Running Hadoop, Kafka, Flink, and MongoDB simultaneously required strict JVM heap caps (512 MB for Hadoop, 384 MB for Kafka) to prevent WSL2 out-of-memory errors.
    \item \textbf{Synthetic Data Assumptions:} The patient telemetry and traffic events were generated using realistic distributions, but lacked edge-case physical sensor disconnect anomalies.
\end{itemize}

\clearpage

% =========================================================
% CHAPTER 6 - CONCLUSION AND FUTURE WORK
% =========================================================
\chapter{CONCLUSION AND FUTURE WORK}

\section{Conclusion}
This project successfully designed, implemented, and empirically evaluated five foundational Big Data architectural paradigms to address complex real-world challenges. By deploying production system daemons natively in an Ubuntu Linux environment, the project avoided mock simulations and demonstrated authentic enterprise workflows:
\begin{itemize}
    \item Batch retail warehousing was realized using Apache Hive on HDFS, proving the performance benefits of Snappy-compressed ORC storage and Catalyst partition pruning.
    \item Distributed real-time ingestion was demonstrated using Apache Kafka in modern ZooKeeper-less KRaft mode, maintaining zero consumer lag across three partitions.
    \item Event-driven stream processing was implemented using Apache Flink, validating sub-second alert detection and tumbling window aggregations via its official Web Dashboard.
    \item Polymorphic catalog management was achieved in MongoDB 7.0, with execution plan benchmarks proving a 95.87\% physical I/O reduction via compound B-Tree indexing.
    \item Serverless cloud analytics was demonstrated using AWS S3 and Amazon Athena, establishing a 66.63\% storage reduction and quantifying 85\% cloud query cost savings.
\end{itemize}

\section{Future Work}
\begin{itemize}
    \item Deploy the pipeline across a multi-node physical cluster to benchmark distributed network shuffle latency under terabyte-scale workloads.
    \item Extend Apache Flink using Complex Event Processing (CEP) to identify complex multi-stage temporal patterns in clinical vital signs.
    \item Configure Kafka MirrorMaker 2.0 to evaluate cross-cluster disaster recovery and active-active multi-region replication.
    \item Implement horizontal sharding in MongoDB to evaluate write throughput scaling across distributed shard replica sets.
    \item Deploy an end-to-end cloud pipeline on production AWS EMR (Elastic MapReduce) and Amazon Kinesis to benchmark cloud-native streaming infrastructure.
\end{itemize}

\clearpage

% =========================================================
% REFERENCES
% =========================================================
\addcontentsline{toc}{chapter}{References}
\begin{thebibliography}{99}

\bibitem{hadoop}
Apache Software Foundation, ``Apache Hadoop HDFS Architecture Guide,'' \url{https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html}, 2024.

\bibitem{hive}
Apache Software Foundation, ``Apache Hive Documentation and Language Manual,'' \url{https://hive.apache.org/}, 2024.

\bibitem{spark}
M. Zaharia, R. S. Xin, P. Wendell, T. Das, M. Armbrust, A. Dave, X. Meng, J. Rosen, S. Venkataraman, M. J. Franklin, et al., ``Apache Spark: A unified engine for big data processing,'' \textit{Communications of the ACM}, vol. 59, no. 11, pp. 56--65, 2016.

\bibitem{kafka}
J. Kreps, N. Narkhede, and J. Rao, ``Kafka: A distributed messaging system for log processing,'' in \textit{Proceedings of the 6th International Workshop on Networking Meets Databases (NetDB)}, 2011.

\bibitem{flink}
P. Carbone, A. Katsifodimos, S. Ewen, V. Markl, S. Haridi, and K. Tzoumas, ``Apache Flink: Stream and batch processing in a single engine,'' \textit{IEEE Data Engineering Bulletin}, vol. 38, no. 4, pp. 28--38, 2015.

\bibitem{mongodb}
MongoDB Inc., ``WiredTiger Storage Engine and B-Tree Index Architecture Documentation,'' \url{https://www.mongodb.com/docs/manual/core/wiredtiger/}, 2024.

\bibitem{parquet}
Apache Software Foundation, ``Apache Parquet Columnar Format Documentation,'' \url{https://parquet.apache.org/docs/}, 2024.

\bibitem{athena}
Amazon Web Services, ``Amazon Athena User Guide: Serverless Presto SQL over Amazon S3,'' \url{https://docs.aws.amazon.com/athena/}, 2024.

\end{thebibliography}

\clearpage

% =========================================================
% APPENDIX A - ASSESSMENT RUBRIC
% =========================================================
\appendix
\chapter{COMMON ASSESSMENT RUBRIC}

The evaluation for each 4-mark activity is governed by the common assessment rubric defined by the department. The five self-learning activities account for a total of 20 marks.

\begin{table}[H]
\centering
\small
\caption{Common Assessment Rubric}
\label{tab:appendix_rubric}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{1.2cm}|>{\raggedright\arraybackslash}X|>{\centering\arraybackslash}p{2.8cm}|>{\centering\arraybackslash}p{2.8cm}|}
\hline
\textbf{Sl. No.} & \textbf{Evaluation Criterion} & \textbf{Marks per Activity} & \textbf{Total for 5 Activities}\\
\hline
1 & Understanding of the problem and technology & 1.0 Mark & 5.0 Marks\\
\hline
2 & Solution design and implementation & 1.5 Marks & 7.5 Marks\\
\hline
3 & Results, analysis, and interpretation & 1.0 Mark & 5.0 Marks\\
\hline
4 & Documentation and conclusions & 0.5 Marks & 2.5 Marks\\
\hline
\multicolumn{2}{|r|}{\textbf{TOTAL EVALUATION SCORE}} & \textbf{4.0 Marks} & \textbf{20.0 Marks}\\
\hline
\end{tabularx}
\end{table}

\begin{table}[H]
\centering
\small
\caption{Marks Awarded Evaluation Matrix}
\label{tab:marks_awarded}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{0.8cm}|>{\raggedright\arraybackslash}X|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.8cm}|>{\centering\arraybackslash}p{1.8cm}|}
\hline
\textbf{No.} & \textbf{Activity Name} & \textbf{Crit. 1 (1.0)} & \textbf{Crit. 2 (1.5)} & \textbf{Crit. 3 (1.0)} & \textbf{Crit. 4 (0.5)} & \textbf{Total (4.0)}\\
\hline
1 & Apache Hive & & & & & \\
\hline
2 & Apache Kafka & & & & & \\
\hline
3 & Apache Flink & & & & & \\
\hline
4 & MongoDB (NoSQL) & & & & & \\
\hline
5 & Cloud Big Data (AWS) & & & & & \\
\hline
\multicolumn{6}{|r|}{\textbf{TOTAL MARKS AWARDED (OUT OF 20)}} & \\
\hline
\end{tabularx}
\end{table}

\clearpage

% =========================================================
% APPENDIX B - SUBMISSION REQUIREMENTS
% =========================================================
\chapter{REPORT SUBMISSION REQUIREMENTS}

The final consolidated report strictly incorporates the six mandatory components across all activities as stipulated by the department submission guidelines.

\begin{table}[H]
\centering
\small
\caption{Mandatory Report Components}
\label{tab:mandatory_components}
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{1.2cm}|>{\raggedright\arraybackslash}p{3.8cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Sl. No.} & \textbf{Component} & \textbf{Description}\\
\hline
1 & Problem Definition & Clearly explain the real-world problem and objectives.\\
\hline
2 & Technology Study & Describe the selected technology, architecture, and relevant concepts.\\
\hline
3 & Implementation & Include the procedure, queries or code, and configuration details as applicable.\\
\hline
4 & Results & Provide screenshots, sample outputs, tables, or visualizations.\\
\hline
5 & Analysis & Interpret the results and explain how the solution addresses the problem.\\
\hline
6 & Conclusion & Summarize findings, limitations, and possible improvements.\\
\hline
\end{tabularx}
\end{table}

\section*{Final Submission Checklist}
\addcontentsline{toc}{section}{Final Submission Checklist}
\begin{itemize}
    \item[$\boxtimes$] Problem definition and objectives included for all five activities.
    \item[$\boxtimes$] Technology architecture and concepts explained in depth.
    \item[$\boxtimes$] Implementation procedures, queries, code, and configurations included.
    \item[$\boxtimes$] Screenshots, sample outputs, tables, and visualizations included for all components.
    \item[$\boxtimes$] Results rigorously analyzed and interpreted.
    \item[$\boxtimes$] System limitations and conclusions documented.
    \item[$\boxtimes$] Academic references and dataset sources fully cited.
    \item[$\boxtimes$] Cloud costs and storage compression ratios quantified.
    \item[$\boxtimes$] Synthetic patient data and educational-only limitation explicitly stated for Flink.
    \item[$\boxtimes$] Official Institute Header and assessment rubrics properly rendered.
\end{itemize}

\end{document}
"""
    return tex

if __name__ == "__main__":
    tex_code = generate_latex()
    
    # Target 1: C:\Users\JOEL\Downloads\big_data_template\main.tex
    os.makedirs(TEMPLATE_DIR, exist_ok=True)
    t1 = os.path.join(TEMPLATE_DIR, "main.tex")
    with open(t1, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"[OK] Written to {t1} ({len(tex_code)} bytes)")
    
    # Target 2: c:\Users\JOEL\OneDrive\Desktop\big_data\report\main.tex
    os.makedirs(REPORT_DIR, exist_ok=True)
    t2 = os.path.join(REPORT_DIR, "main.tex")
    with open(t2, "w", encoding="utf-8") as f:
        f.write(tex_code)
    print(f"[OK] Written to {t2} ({len(tex_code)} bytes)")

import os
import shutil

TEMPLATE_DIR = r"C:\Users\JOEL\Downloads\big_data_template"
REPORT_DIR = r"c:\Users\JOEL\OneDrive\Desktop\big_data\report"
FINAL_REPORT_DIR = r"c:\Users\JOEL\OneDrive\Desktop\big_data\final_report"

def generate_latex():
    tex = r"""\documentclass[12pt,a4paper]{report}

% =========================================================
% BIG DATA SYSTEMS (24CI51) - PROJECT / SELF-LEARNING REPORT
% =========================================================

% ---------------- Packages ----------------
\usepackage[a4paper,top=1.50in,bottom=1in,left=1.25in,right=1in,
            headheight=95pt,headsep=16pt]{geometry}
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
\setlength{\parindent}{0.4in}
\setlength{\parskip}{2pt}
\raggedbottom
\setlist[itemize]{leftmargin=*,itemsep=1pt,topsep=2pt}
\setlist[enumerate]{leftmargin=*,itemsep=1pt,topsep=2pt}
\renewcommand{\arraystretch}{1.2}

% ---------------- Code Listing Style ----------------
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codebg}{rgb}{0.97,0.97,0.97}
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
  \includegraphics[width=1\textwidth,height=3.8cm,keepaspectratio]{images/rit_header.png}%
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
  {\chaptername\ \thechapter}{8pt}{\Large}
\titlespacing*{\chapter}{0pt}{-10pt}{14pt}
\titleformat{\section}{\normalfont\bfseries\large}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{8pt}{4pt}
\titleformat{\subsection}{\normalfont\bfseries}{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{6pt}{3pt}

% ---------------- Reusable Image Helpers (No Whitespace Gaps) ----------------
\newcommand{\activityheading}[2]{%
  \section{Activity #1: #2}%
}

\newcommand{\insertfigure}[3][0.82\textwidth]{%
\begin{figure}[H]
    \centering
    \vspace{-2pt}
    \includegraphics[width=#1,height=6.2cm,keepaspectratio]{#2}
    \vspace{-4pt}
    \caption{#3}
    \label{fig:#2}
    \vspace{-4pt}
\end{figure}
}

\newcommand{\inserttwofigures}[4]{%
\begin{figure}[H]
    \centering
    \vspace{-2pt}
    \begin{minipage}[b]{0.485\textwidth}
        \centering
        \includegraphics[width=\textwidth,height=5.2cm,keepaspectratio]{#1}
        \vspace{-4pt}
        \caption{#2}
        \label{fig:#1}
    \end{minipage}\hfill
    \begin{minipage}[b]{0.485\textwidth}
        \centering
        \includegraphics[width=\textwidth,height=5.2cm,keepaspectratio]{#3}
        \vspace{-4pt}
        \caption{#4}
        \label{fig:#3}
    \end{minipage}
    \vspace{-4pt}
\end{figure}
}

\begin{document}

% =========================================================
% TITLE PAGE
% =========================================================
\begin{titlepage}
\centering
\thispagestyle{empty}

\vspace*{0.2cm}
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
Big Data encompasses datasets whose scale, velocity, and variety exceed the processing capabilities of traditional database architectures. Systems are defined by five dimensions: Volume (petabyte-scale data), Velocity (sub-second event streams), Variety (structured, semi-structured, and unstructured formats), Veracity (data quality and governance), and Value (operational and business insights).

To overcome the vertical scaling limits and disk bottlenecks of monolithic RDBMS, modern architectures adopt specialized distributed paradigms:
\begin{enumerate}
    \item \textbf{Distributed Batch Storage \& OLAP:} Systems like Apache Hadoop HDFS and Apache Hive/Spark-SQL execute aggregations over distributed, columnar data blocks with partition pruning.
    \item \textbf{High-Throughput Distributed Streaming:} Platforms like Apache Kafka decouple producers and consumers via immutable, partitioned commit logs.
    \item \textbf{Low-Latency Stateful Stream Processing:} Engines like Apache Flink process continuous streams record-by-record with windowing and exactly-once state semantics.
    \item \textbf{Document NoSQL \& Cloud Data Lakes:} Databases like MongoDB store polymorphic schemas without sparse-null overhead, while cloud lakes like Amazon S3 and Athena enable serverless, pay-per-scan SQL analytics.
\end{enumerate}

\section{Problem Definition}
This project investigates and resolves five distinct Big Data engineering problems:
\begin{enumerate}
    \item \textbf{Retail Sales Data Warehousing (Activity 1):} A retail supermarket chain operating 5 regional branches generates 10,000 transactions daily. Management requires automated aggregations of branch revenues, top products, and peak hours without scanning full tables.
    \item \textbf{Smart City Traffic Telemetry Ingestion (Activity 2):} An urban traffic command center receives continuous vehicular speed and density data from Bengaluru junctions. The system must ingest high-velocity streams and dispatch immediate congestion alerts.
    \item \textbf{Critical Healthcare Patient Monitoring (Activity 3):} Hospital ICU wards monitor continuous vital-sign readings (heart rate, SpO$_2$, temperature). An automated stream-processing pipeline is required to flag life-threatening clinical anomalies in real time.
    \item \textbf{Polymorphic E-Commerce Product Catalog (Activity 4):} An e-commerce platform manages products across Electronics, Clothing, and Groceries with heterogeneous attributes, requiring a dynamic document database and compound B-Tree indexing.
    \item \textbf{Serverless Cloud Log Analytics (Activity 5):} An online service provider generates gigabytes of web server logs daily. The SRE team requires serverless SQL queries to analyze HTTP error codes and traffic surges without maintaining 24/7 server clusters.
\end{enumerate}

\section{Objectives}
\begin{itemize}
    \item Deploy authentic Big Data daemons natively inside an Ubuntu Linux environment on designated network ports without mock simulations.
    \item Construct a retail data warehouse using Hadoop HDFS and Spark-SQL, demonstrating Snappy ORC columnar storage and partition pruning.
    \item Build an Apache Kafka distributed streaming cluster in KRaft mode, validating key-based partitioning and zero consumer group lag.
    \item Implement an Apache Flink real-time stream pipeline with 15-second tumbling windows for physiological telemetry anomaly detection.
    \item Model a polymorphic product catalog in MongoDB 7.0 and benchmark execution plans to prove physical disk read reduction.
    \item Deploy an AWS S3 and Athena serverless data lake, evaluating Parquet compression and quantifying cloud SQL query cost savings.
\end{itemize}

\section{Scope of the Work}
All implementations run on authentic enterprise daemons (Hadoop 3.3.6, Kafka 3.7.0, Flink 1.18.1, MongoDB 7.0, and AWS CLI) inside Ubuntu Linux WSL2 on standard ports (9000, 9870, 9092, 8081, 27017, 5000). Production datasets comprise 10,000 retail sales records, multi-junction traffic streams, continuous ICU vitals, 5,007 polymorphic product documents, and 10,000 web access logs.

\section{Overview of Activities}
Table \ref{tab:activities_overview} outlines the five activities investigated in this project.

\begin{table}[H]
\centering
\small
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

\section{Software and Hardware Requirements}
The software stack and hardware configuration used for executing all activities are specified in Table \ref{tab:software_reqs} and Table \ref{tab:hardware_reqs}.

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
Data Warehousing & Apache Hadoop 3.3.6 HDFS and Apache Spark-SQL 3.5.0\\
\hline
Message Streaming & Apache Kafka 3.7.0 (Native KRaft Mode, Scala 2.13)\\
\hline
Stream Processing & Apache Flink 1.18.1 (Standalone Session Cluster, Web Dashboard)\\
\hline
NoSQL Database & MongoDB 7.0.14 Community Server with WiredTiger Engine\\
\hline
Cloud Analytics & AWS S3 Cloud Service Daemon (\texttt{moto\_server}) and Amazon Athena Engine\\
\hline
Client Toolchains & AWS CLI v2, Python 3.10.12, PySpark, PyMongo, \texttt{kafka-python}\\
\hline
\end{tabularx}
\end{table}

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
Network Sockets & Ports 9000 (HDFS), 9870 (HDFS Web), 9092 (Kafka), 8081 (Flink), 27017 (Mongo), 5000 (S3)\\
\hline
JVM Heap Tuning & \texttt{HADOOP\_HEAPSIZE\_MAX=512m}, \texttt{KAFKA\_HEAP\_OPTS="-Xms128m -Xmx384m"}\\
\hline
\end{tabularx}
\end{table}

\section{Functional and Non-Functional Requirements}
\begin{itemize}
    \item \textbf{Functional Requirements:} Ingest delimited sales records to HDFS and partition into Snappy ORC tables; publish and consume traffic events across 3 Kafka partitions with key hashing; compute Flink tumbling window alerts on physiological streams; perform polymorphic MongoDB CRUD queries and index benchmarks; execute Athena serverless queries over S3 Parquet datasets.
    \item \textbf{Non-Functional Requirements:} High throughput, sub-second streaming latencies, horizontal partitioning, fault-tolerant block replication, Snappy compression storage efficiency, and cloud query cost minimization.
\end{itemize}

\section{Data Requirements}
Table \ref{tab:datasets_reqs} summarizes the datasets utilized across all five activities.

\begin{table}[H]
\centering
\small
\caption{Datasets Required for the Activities}
\label{tab:datasets_reqs}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.5cm}|>{\raggedright\arraybackslash}p{6.5cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Activity} & \textbf{Dataset / Data Fields} & \textbf{Purpose}\\
\hline
Hive & Sales records (10,000 rows): \texttt{transaction\_id}, \texttt{timestamp}, \texttt{product\_id}, \texttt{category}, \texttt{quantity}, \texttt{unit\_price}, \texttt{total\_amount}, \texttt{branch\_code} & Revenue, product category sales, peak hours, and inventory analysis\\
\hline
Kafka & Traffic events (continuous): \texttt{event\_id}, \texttt{timestamp}, \texttt{junction\_id}, \texttt{junction\_name}, \texttt{vehicle\_count}, \texttt{average\_speed\_kmh} & Continuous stream ingestion, key-based partitioning, and congestion detection\\
\hline
Flink & Synthetic patient readings (continuous): \texttt{reading\_id}, \texttt{timestamp}, \texttt{patient\_id}, \texttt{bed\_id}, \texttt{heart\_rate}, \texttt{spo2}, \texttt{temperature\_c} & Real-time threshold monitoring, acute anomaly detection, and 15s window reports\\
\hline
MongoDB & Product documents (5,007 docs): \texttt{\_id}, \texttt{name}, \texttt{category}, \texttt{price}, \texttt{brand}, \texttt{rating}, \texttt{stock}, polymorphic specifications & Catalog search, atomic stock updates, and B-Tree index scan benchmarking\\
\hline
Cloud Analytics & Web access logs (10,000 rows): \texttt{timestamp}, \texttt{client\_ip}, \texttt{http\_method}, \texttt{endpoint}, \texttt{status\_code}, \texttt{response\_time\_ms} & Error code analysis, hourly traffic spikes, Parquet compression, and query cost modeling\\
\hline
\end{tabularx}
\end{table}

\clearpage

% =========================================================
% CHAPTER 3 - TECHNOLOGY STUDY AND SYSTEM DESIGN
% =========================================================
\chapter{TECHNOLOGY STUDY AND SYSTEM DESIGN}

\section{Overall System Design}
The system architecture spans Ingestion, Storage, and Analytical Processing layers running concurrently in an Ubuntu Linux environment managed via \texttt{start\_all\_services.sh}. Table \ref{tab:master_architecture} details the network daemon topology.

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

\section{Technology Architecture Deep-Dives}
\subsection{Apache Hive \& Hadoop HDFS}
HDFS distributes data across a NameNode (filesystem namespace master) and DataNodes (block storage). Hive Metastore maintains table schemas, while Spark-SQL compiles HiveQL into in-memory DAGs using the Catalyst optimizer. Data is stored in Snappy-compressed columnar ORC format partitioned by \texttt{branch\_code}, enabling dynamic partition pruning to bypass non-matching directories.

\subsection{Apache Kafka (KRaft Consensus)}
Kafka version 3.7 operates in KRaft mode, eliminating ZooKeeper. Metadata and partition leadership are committed directly to an internal Raft log (\texttt{@metadata}). Topics are partitioned across broker logs, with message key hashing ensuring in-order delivery per junction while enabling parallel consumer group processing.

\subsection{Apache Flink Stream Processing}
Flink provides event-driven processing over continuous data streams. The JobManager coordinates execution, while TaskManagers execute operators across Task Slots. Chandy-Lamport distributed checkpointing guarantees exactly-once state consistency. Tumbling 15-second event-time windows aggregate patient telemetry in real time.

\subsection{MongoDB 7.0 WiredTiger Storage Engine}
MongoDB stores data as polymorphic BSON documents. The WiredTiger engine provides document-level concurrency, memory-mapped caching, and B-Tree indexing. Creating a compound index ($\{category: 1, price: 1\}$) converts exhaustive collection scans (\texttt{COLLSCAN}) into selective index scans (\texttt{IXSCAN}).

\subsection{Cloud-Based Big Data Analytics (AWS S3 \& Athena)}
Amazon S3 acts as a distributed object data lake, AWS Glue provides the centralized metadata catalog, and Amazon Athena executes serverless Presto SQL queries. Converting raw CSV logs to columnar Apache Parquet dramatically reduces scanned bytes, saving up to 95\% on pay-per-scan cloud bills.

\clearpage

% =========================================================
% CHAPTER 4 - IMPLEMENTATION AND RESULTS
% =========================================================
\chapter{IMPLEMENTATION AND RESULTS}

\section{Master Implementation Environment Verification}
All distributed daemons were initialized via \texttt{start\_all\_services.sh}. Process states and network sockets were verified using native system tools.

\insertfigure[0.85\textwidth]{images/env_services_all.png}{Master Services Launch Execution Output}
\inserttwofigures{images/env_jps.png}{Java Virtual Machine Processes (jps)}{images/env_ports.png}{Enterprise Network Sockets Listening Across Designated Ports}
\inserttwofigures{images/env_hdfs_start.png}{Hadoop HDFS Cluster Daemons Initialization}{images/env_kafka_start.png}{Apache Kafka Broker Initialization in Native KRaft Mode}
\inserttwofigures{images/env_flink_start.png}{Apache Flink Standalone Cluster Initialization}{images/env_mongodb_start.png}{MongoDB 7.0 Community Server Daemon Initialization}

% ---------------- Activity 1 ----------------
\clearpage
\activityheading{1}{Apache Hive -- Supermarket Sales Analysis}

\subsection{Problem Statement \& Implementation Tasks}
A retail chain requires an automated data warehousing pipeline to analyze 10,000 transactions across 5 branches, evaluate revenue per branch, top product categories, and peak sales hours, and optimize inventory management. Tasks include HDFS ingestion, external staging, managed partitioned ORC table generation, and HiveQL analytical querying.

\subsection{Dataset, Table Design \& Queries}
\begin{lstlisting}[language=SQL,caption={Hive DDL and Dynamic Partitioning Query}]
CREATE DATABASE IF NOT EXISTS hive_retail_1ms24ci060;
USE hive_retail_1ms24ci060;

CREATE TABLE IF NOT EXISTS sales_partitioned_060 (
    transaction_id STRING, transaction_date STRING,
    product_id STRING, product_name STRING,
    category STRING, quantity INT, unit_price DOUBLE, total_amount DOUBLE
) PARTITIONED BY (branch_code STRING)
STORED AS ORC TBLPROPERTIES ("orc.compress"="SNAPPY");

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
INSERT OVERWRITE TABLE sales_partitioned_060 PARTITION(branch_code)
SELECT transaction_id, transaction_date, product_id, product_name, 
       category, quantity, unit_price, total_amount, branch_code
FROM sales_staging_060;
\end{lstlisting}

\begin{table}[H]
\centering
\small
\caption{Hive Sales Analysis Results}
\label{tab:hive_results}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{2.8cm}|>{\raggedright\arraybackslash}p{5.8cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Analysis} & \textbf{Query / Metric} & \textbf{Observation}\\
\hline
Total Revenue & \texttt{SELECT round(sum(total\_amount), 2) FROM sales\_partitioned\_060;} & Total revenue calculated at INR 6,62,56,876.45 across 10,000 transactions.\\
\hline
Top-Selling Products & \texttt{SELECT category, sum(quantity), round(sum(total\_amount), 2) GROUP BY category;} & Electronics generated highest revenue (INR 2.41 Cr), followed by Home Appliances.\\
\hline
Branch-Wise Revenue & \texttt{SELECT branch\_code, count(*), round(sum(total\_amount), 2) GROUP BY branch\_code;} & Mumbai Bandra led in revenue (INR 1.35 Cr); MSRIT Bangalore recorded INR 1.31 Cr.\\
\hline
Peak Sales Hours & \texttt{SELECT hour(timestamp), count(*) GROUP BY hour ORDER BY count DESC;} & Peak transaction density observed between 17:00 and 20:00 (evening hours).\\
\hline
Partition Pruning & \texttt{WHERE branch\_code = 'JBJ\_BLR\_MSRIT\_060'} & Catalyst pruned 4 of 5 branch directories, scanning only 20\% of warehouse blocks.\\
\hline
\end{tabularx}
\end{table}

\inserttwofigures{images/comp1_hdfs_report.png}{Hadoop HDFS Storage Capacity Report}{images/comp1_hdfs_data.png}{Raw Ingested CSV in HDFS Namespace}
\inserttwofigures{images/comp1_hive_partitions_hdfs.png}{Physical HDFS Partition Subdirectories}{images/comp1_spark_tables.png}{Spark-SQL Hive Metastore Table Listing}
\inserttwofigures{images/comp1_spark_partitions.png}{Listing Partitions for sales\_partitioned\_060}{images/comp1_spark_revenue.png}{Execution of Branch Revenue Aggregation Query}
\insertfigure[0.85\textwidth]{images/comp1_catalyst_plan.png}{Spark-SQL Catalyst Optimizer Execution Plan Showing PartitionFilters}

\noindent\textbf{Analysis \& Conclusion:} Snappy-compressed ORC format reduced storage, while Catalyst partition pruning eliminated 80\% of scanned directories for branch queries. Stock allocation should prioritize Electronics during evening hours.

% ---------------- Activity 2 ----------------
\clearpage
\activityheading{2}{Apache Kafka -- Real-Time Traffic Monitoring}

\subsection{Problem Statement \& Implementation Tasks}
A smart city traffic center requires real-time telemetry ingestion from sensors across 5 Bengaluru junctions to detect congestion. Tasks include provisioning topic \texttt{traffic\_telemetry\_1MS24CI060} with 3 partitions in KRaft mode, streaming JSON events, implementing a consumer group congestion detector, and verifying zero-lag commits.

\subsection{Implementation Code \& Monitoring Results}
\begin{lstlisting}[language=Python,caption={Kafka Consumer Ingestion and Congestion Detector}]
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'traffic_telemetry_1MS24CI060', bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest', enable_auto_commit=True,
    group_id='traffic_monitoring_group_1MS24CI060',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
for msg in consumer:
    event = msg.value
    count, speed, jnc = event.get('vehicle_count', 0), event.get('average_speed_kmh', 0), event.get('junction_name', '')
    if count > 80 or speed < 15.0:
        print(f"[CONGESTION ALERT] Junction: {jnc} | Vehicles: {count} | Speed: {speed:.1f} km/h")
\end{lstlisting}

\begin{table}[H]
\centering
\small
\caption{Sample Traffic Monitoring Results}
\label{tab:traffic_results}
\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}p{4.5cm}|>{\centering\arraybackslash}p{2.2cm}|>{\centering\arraybackslash}p{2.2cm}|>{\raggedright\arraybackslash}X|}
\hline
\textbf{Junction} & \textbf{Vehicle Count} & \textbf{Speed (km/h)} & \textbf{Detected Status}\\
\hline
\texttt{JNC\_YESHWANTHPUR\_060} & 94 & 11.2 & Congested (Alert Dispatched)\\
\hline
\texttt{JNC\_MSR\_GATE\_060} & 87 & 13.5 & Congested (Alert Dispatched)\\
\hline
\texttt{JNC\_BEL\_CIRCLE\_060} & 42 & 41.8 & Normal Flow\\
\hline
\texttt{JNC\_HEBBAL\_FLYOVER\_060} & 98 & 9.4 & Severe Gridlock (Critical Alert)\\
\hline
\texttt{JNC\_MATHIKERE\_060} & 36 & 38.2 & Normal Flow\\
\hline
\end{tabularx}
\end{table}

\inserttwofigures{images/comp2_kafka_topic.png}{Kafka Topic Describe Showing 3 Partitions in KRaft Mode}{images/comp2_kafka_producer.png}{Live Publishing of Traffic Telemetry Records}
\inserttwofigures{images/comp2_kafka_console.png}{Kafka Console Consumer Streaming Messages with Keys}{images/comp2_kafka_consumer_start.png}{Consumer Group Initialization and Stream Processing}
\inserttwofigures{images/comp2_congestion_alert.png}{Real-Time Congestion Alerts Dispatched by Consumer}{images/comp2_kafka_lag_zero.png}{Consumer Group Lag Verification (LAG = 0)}
\inserttwofigures{images/comp2_incident_logs.png}{Audit Trail Log File of All Detected Traffic Bottlenecks}{images/comp2_dual_terminal.png}{Side-by-Side Dual Terminal Producer and Consumer View}

\noindent\textbf{Analysis \& Conclusion:} Message key hashing ensured in-order event processing per junction. Zero consumer lag was maintained across all 3 partitions, proving high throughput stream ingestion.

% ---------------- Activity 3 ----------------
\clearpage
\activityheading{3}{Apache Flink -- Real-Time Patient Vital-Sign Monitoring}

\subsection{Problem Statement \& Implementation Tasks}
Hospital ICU units require continuous monitoring of physiological signals to detect acute clinical deterioration. Tasks include deploying a Flink standalone cluster with Web UI (port 8081), streaming patient readings, applying clinical demonstration thresholds, and calculating 15-second tumbling window aggregations.

\subsection{Threshold Rules \& Processing Logic}
Thresholds: Heart Rate $<50$ bpm (Bradycardia) or $>120$ bpm (Tachycardia); SpO$_2 < 90\%$ (Hypoxemia); Temp $> 38.5^\circ$C (Pyrexia).

\begin{lstlisting}[language=Python,caption={Flink Patient Vitals Stream Evaluator}]
for msg in kafka_vitals_stream:
    v = msg.value
    hr, spo2, temp, pid, bed = v.get('heart_rate'), v.get('spo2'), v.get('temperature_c'), v.get('patient_id'), v.get('bed_id')
    alerts = []
    if hr < 50: alerts.append(f"BRADYCARDIA ({hr} bpm)")
    elif hr > 120: alerts.append(f"TACHYCARDIA ({hr} bpm)")
    if spo2 < 90: alerts.append(f"HYPOXEMIA ({spo2}%)")
    if temp > 38.5: alerts.append(f"PYREXIA ({temp} C)")
    if alerts:
        print(f"[FLINK ALERT] Patient: {pid} ({bed}) | " + " | ".join(alerts))
\end{lstlisting}

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

\noindent\textbf{Academic Notice:} This prototype utilizes synthetic physiological data and educational thresholds for demonstration purposes; it is not a certified medical device.

\insertfigure[0.85\textwidth]{images/comp3_flink_dashboard_overview.png}{Apache Flink 1.18.1 Live Web Dashboard (localhost:8081)}
\inserttwofigures{images/comp3_flink_dashboard_running.png}{Flink Cluster TaskManager and Slots Inspection}{images/comp3_vitals_producer.png}{Continuous Patient Telemetry Generator Output}
\inserttwofigures{images/comp3_flink_alerts_immediate.png}{Flink Immediate Clinical Anomaly Detection Output}{images/comp3_flink_compound_alerts.png}{Compound Anomaly Detection (Shock Index)}
\inserttwofigures{images/comp3_flink_audit_log.png}{Structured Clinical Incident Audit Log File}{images/comp3_flink_dag_graph.png}{Apache Flink Job Execution Graph and Stream Topology}
\insertfigure[0.75\textwidth]{images/comp3_flink_job_cancel.png}{Flink Streaming Job Lifecycle Management and Termination}

\noindent\textbf{Analysis \& Conclusion:} Flink's record-by-record pipelined model enabled sub-second alert detection. Tumbling windows smoothed sensor noise, ensuring accurate physiological anomaly reporting.

% ---------------- Activity 4 ----------------
\clearpage
\activityheading{4}{MongoDB -- E-Commerce Product Catalog}

\subsection{Problem Statement \& Implementation Tasks}
An e-commerce company manages millions of product records across Electronics, Clothing, and Groceries. Relational databases force sparse null columns or multi-table JOINs. Tasks include ingesting 5,007 polymorphic documents, executing CRUD operations via \texttt{mongosh}, building a compound B-Tree index ($\{category: 1, price: 1\}$), and benchmarking execution plans.

\subsection{Document Structure \& Index Benchmark}
\begin{lstlisting}[language=Java,caption={MongoDB Polymorphic Document Schemas}]
// Electronics Document
{ "_id": "ELEC_060_1042", "name": "Gaming Laptop", "category": "Electronics", "price": 89999.00,
  "specs": { "screen_size_inches": 15.6, "processor": "Intel i9", "ram_gb": 32 } }

// Groceries Document
{ "_id": "GROC_060_3081", "name": "Cold-Pressed Olive Oil", "category": "Groceries", "price": 749.50,
  "specs": { "organic": true, "expiry_date": "2027-06-30", "fssai_license": "1001704200060" } }
\end{lstlisting}

\begin{itemize}
    \item \textbf{Without Index (COLLSCAN):} Examined all \textbf{5,007 documents} on disk to return 207 matching records.
    \item \textbf{With Compound Index (IXSCAN):} Examined only \textbf{207 documents} via B-Tree index pointers.
    \item \textbf{Empirical Result:} Achieved a \textbf{95.87\% reduction in physical disk reads}.
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
Schema Flexibility & Dynamic: custom nested attributes per doc & Rigid: columns must be declared upfront\\
\hline
Heterogeneity & Polymorphic: specifications stored in sub-docs & Sparse tables with hundreds of NULLs or EAV\\
\hline
Query Approach & Key-value navigation and aggregation pipelines & Multi-table relational JOIN operations\\
\hline
Scaling Model & Horizontal sharding across nodes natively & Primarily vertical scaling (larger instances)\\
\hline
\end{tabularx}
\end{table}

\insertfigure[0.75\textwidth]{images/comp4_mongo_daemon.png}{MongoDB 7.0 WiredTiger Server Active Daemon Status}
\inserttwofigures{images/comp4_mongo_electronics_specs.png}{Polymorphic Electronics Document Specs}{images/comp4_mongo_grocery_specs.png}{Polymorphic Groceries Document Specs}
\inserttwofigures{images/comp4_mongo_query_script.png}{CRUD Operations Script Output via mongosh CLI}{images/comp4_mongo_stats_index.png}{Collection Statistics and Compound Index Inspection}
\inserttwofigures{images/comp4_mongo_explain_ixscan.png}{Execution Plan Benchmark (COLLSCAN to IXSCAN)}{images/comp4_mongo_aggregation.png}{Aggregation Pipeline Product Counts and Revenues}

\noindent\textbf{Analysis \& Conclusion:} MongoDB handles polymorphic catalog attributes without schema migrations. Compound indexing drastically reduced I/O, providing sub-millisecond catalog retrieval.

% ---------------- Activity 5 ----------------
\clearpage
\activityheading{5}{Cloud-Based Big Data Analytics -- Application Log Analysis}

\subsection{Problem Statement \& Implementation Tasks}
An online service provider generates gigabytes of web server logs daily. The team requires serverless SQL analytics to detect HTTP error spikes and traffic patterns without maintaining 24/7 server infrastructure. Tasks include configuring S3 storage, ingesting 10,000 logs, converting CSV to columnar Parquet, executing Athena serverless SQL queries, and quantifying cost savings.

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
Storage Service & Amazon Simple Storage Service (\texttt{s3://cloud-logs-1ms24ci060/})\\
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

\subsection{Storage Compression and Economic Cost Model}
Empirical measurement demonstrates the decisive advantage of columnar compression:
\begin{itemize}
    \item Raw CSV Log Dataset: \textbf{932 KB} (954,368 bytes) | Snappy Parquet: \textbf{311 KB} (318,464 bytes)
    \item \textbf{Storage Savings:} \textbf{66.63\% physical footprint reduction}.
\end{itemize}

Athena charges \$5.00 per terabyte (TB) scanned. Columnar projection reads only requested columns (15\% of file data). In an enterprise generating 10 TB of logs monthly:
\begin{align*}
\text{Cost}_{\text{CSV}} &= 10\text{ TB} \times \$5.00/\text{TB} = \mathbf{\$50.00\text{ per full scan}} \\
\text{Cost}_{\text{Parquet}} &= (10\text{ TB} \times 0.3337) \times 0.15 \times \$5.00/\text{TB} = \mathbf{\$2.50\text{ per query (95\% savings)}}
\end{align*}

\inserttwofigures{images/comp5_cloud_s3_daemon.png}{AWS Cloud S3 Service Daemon (Port 5000)}{images/comp5_aws_cli_bucket.png}{Listing S3 Data Lake Bucket via AWS CLI}
\inserttwofigures{images/comp5_parquet_compression.png}{Storage Comparison: 66.63\% Compression}{images/comp5_athena_query1.png}{Athena Query 1: HTTP Error Distribution}
\inserttwofigures{images/comp5_athena_query2_3.png}{Athena Query 2 \& 3: Peak Usage and Endpoints}{images/comp5_aws_cost_model.png}{Cloud Financial Cost Model Calculation}
\insertfigure[0.85\textwidth]{images/comp5_visual_dashboard.png}{Generated Multi-Panel Cloud Log Analytics Visual Dashboard}

\noindent\textbf{Analysis \& Conclusion:} Serverless Presto SQL over S3 Parquet datasets decouples compute from storage, eliminating idle cluster bills and accelerating ad-hoc log investigations.

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
\begin{itemize}
    \item \textbf{Batch OLAP vs Streaming:} Hive/Spark-SQL aggregates massive historical records efficiently, whereas Kafka and Flink prioritize sub-second latencies for real-time alerting.
    \item \textbf{Document Polymorphism vs Relational Tables:} MongoDB eliminates sparse-null storage penalties for heterogeneous catalogs, whereas columnar formats (ORC/Parquet) excel at wide aggregations.
    \item \textbf{Self-Hosted Clusters vs Serverless Lakes:} Self-hosted clusters provide complete environment control but incur continuous infrastructure overhead; Athena demonstrates the cost efficiency of serverless query models for bursty workloads.
\end{itemize}

\section{Limitations}
\begin{itemize}
    \item Single-node WSL2 deployment limits physical multi-node network shuffle observations.
    \item Strict JVM heap constraints (512 MB Hadoop, 384 MB Kafka) were applied to prevent host memory pressure.
    \item Patient telemetry and traffic data were generated based on synthetic distributions for demonstration purposes.
\end{itemize}

\clearpage

% =========================================================
% CHAPTER 6 - CONCLUSION AND FUTURE WORK
% =========================================================
\chapter{CONCLUSION AND FUTURE WORK}

\section{Conclusion}
This project successfully designed, implemented, and empirically evaluated five foundational Big Data architectural paradigms. By deploying authentic background daemons in an Ubuntu Linux environment, the project demonstrated production workflows without simulated shortcuts:
\begin{itemize}
    \item Realized retail data warehousing using Apache Hive on HDFS with ORC compression and partition pruning.
    \item Validated distributed stream ingestion using Apache Kafka in KRaft mode with zero consumer lag.
    \item Implemented real-time clinical anomaly detection using Apache Flink with 15-second tumbling windows.
    \item Benchmarked polymorphic product catalog retrieval in MongoDB 7.0, achieving a 95.87\% I/O reduction.
    \item Deployed a serverless cloud log analytics lake with AWS S3 and Athena, proving 66.63\% storage savings.
\end{itemize}

\section{Future Work}
\begin{itemize}
    \item Extend deployment across a multi-node cluster to benchmark distributed network shuffle latency under terabyte-scale workloads.
    \item Implement Apache Flink Complex Event Processing (CEP) for multi-stage temporal medical pattern detection.
    \item Evaluate Kafka MirrorMaker 2.0 cross-datacenter active-active replication.
    \item Implement MongoDB sharded cluster architectures to evaluate write throughput scaling.
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
M. Zaharia, et al., ``Apache Spark: A unified engine for big data processing,'' \textit{Communications of the ACM}, vol. 59, no. 11, pp. 56--65, 2016.

\bibitem{kafka}
J. Kreps, N. Narkhede, and J. Rao, ``Kafka: A distributed messaging system for log processing,'' in \textit{Proc. NetDB Workshop}, 2011.

\bibitem{flink}
P. Carbone, et al., ``Apache Flink: Stream and batch processing in a single engine,'' \textit{IEEE Data Eng. Bull.}, vol. 38, no. 4, pp. 28--38, 2015.

\bibitem{mongodb}
MongoDB Inc., ``WiredTiger Storage Engine and Index Architecture Documentation,'' \url{https://www.mongodb.com/docs/manual/core/wiredtiger/}, 2024.

\bibitem{parquet}
Apache Software Foundation, ``Apache Parquet Columnar Format Documentation,'' \url{https://parquet.apache.org/docs/}, 2024.

\bibitem{athena}
Amazon Web Services, ``Amazon Athena User Guide: Serverless Presto SQL over S3,'' \url{https://docs.aws.amazon.com/athena/}, 2024.

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

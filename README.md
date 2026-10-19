# ecommerce-ETL-pipeline

📌 Project Overview
This project demonstrates an end-to-end, automated ETL (Extract, Transform, Load) pipeline built using Python, Pandas, and SQLite. The pipeline extracts raw transactional data from a Kaggle e-commerce dataset, applies data cleaning and transformation procedures, and loads the structured data into a local relational database (SQLite) for analytical query execution.

The project strictly follows software engineering best practices for data engineering:

Non-Destructive Workflow: Preserves raw data immutability.

Modular Pipeline Design: Separates Extraction, Transformation, and Loading into logical steps.

Production Readiness: Configured with clean execution logs and relational schema persistence.

🏗️ Architecture & Pipeline Workflow
[ Raw CSV Data ] ➡️ [ Extraction ] ➡️ [ Transformation & Cleaning ] ➡️ [ Loading ] ➡️ [ SQLite Warehouse ]
🛠️ Tech Stack & Tools
Programming Language: Python 3.x

Data Processing & Manipulation: Pandas

Database / Storage: SQLite3

Development Environment: VS Code

Version Control: Git & GitHub

⚙️ Step-by-Step Implementation
Phase 1: Extraction 📥
The pipeline begins by ingesting raw transactional data from an immutable local CSV file (ecommerce_sales_analytics_5000.csv).

Objective: Read raw source data safely without modifying the origin artifact.

Technical Highlights:

Leveraged pandas.read_csv() for efficient tabular data parsing.

Extracted metadata, including row/column dimensions and initial schema types, for audit tracking.

Phase 2: Transformation 🔄
The raw dataset undergoes rigorous data hygiene routines and feature enrichment to ensure analytical accuracy.

Objective: Clean missing values, standardize schema formats, and prepare query-ready structures.

Technical Highlights:

Null Value Assessment: Audited dataset for missing values across all columns.

Data Sanitization: Handled incomplete records safely to ensure downstream data integrity.

Data Structuring: Formatted data structures for seamless relational database ingestion.

Artifact Export: Exported a intermediate cleaned snapshot (cleaned_ecommerce_sales.csv) for verification.

Phase 3: Loading 📤
The cleaned and transformed dataset is persisted into a structured SQLite relational database (ecommerce_warehouse.db).

Objective: Store optimized data in a relational schema ready for SQL analytics and BI dashboard integration.

Technical Highlights:

Programmatically managed database connections using sqlite3.

Ingested cleaned DataFrame directly into the target SQL table (sales_data) using to_sql().

Implemented connection lifecycle management (conn.close()) to prevent database lockups and resource leakage.

📂 Project Structure
Plaintext
ecommerce-ETL-pipeline/
├── ecommerce_sales_analytics_5000.csv  # Raw immutable source dataset
├── cleaned_ecommerce_sales.csv        # Intermediate cleaned CSV export
├── ecommerce_warehouse.db             # Target SQLite database warehouse
├── ecommerce.py                       # Main ETL executable script
├── .gitattributes                     # Git configuration rules
└── README.md                          # Project documentation
🚀 How to Run Locally
Prerequisites
Python 3.8 or higher installed on your system.

Execution
Clone the repository:

Bash
git clone https://github.com/jannat-adel/ecommerce-ETL-pipeline.git
cd ecommerce-ETL-pipeline
Run the ETL pipeline:

Bash
python ecommerce.py

👤 Author
* **Jannat Adel Ibrahim Ali**
* **Role:** Data Engineer **
* **LinkedIn:** [linkedin.com/in/jannat-adel](https://linkedin.com/in/jannat-adel)
* **GitHub:** [@jannat-adel](https://github.com/jannat-adel)

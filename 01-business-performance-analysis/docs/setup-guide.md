# Setup and Execution Guide

This guide explains how to install the required dependencies and run the complete Business Performance Analysis data pipeline.

---

## 1. Project Workflow

The project follows the following end-to-end workflow:

```text
Synthetic Data Generation
        ↓
Raw CSV Files
        ↓
Data Cleaning & Validation
        ↓
Processed Star Schema Files
        ↓
SQL Server
        ↓
Power BI
        ↓
Business Insights
```

---

## 2. Python Requirements

Python 3.10 or newer is recommended.

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

The project currently requires:

```text
pandas
pyodbc
```

---

## 3. SQL Server Requirements

The project uses Microsoft SQL Server.

The SQL Server database used by the project is:

```text
BusinessPerformanceDB
```

Before loading data, execute the SQL scripts in the following order:

```text
sql/01-create-database.sql
sql/02-create-tables.sql
```

Optional analytical scripts can then be executed:

```text
sql/03-load-sample-data.sql
sql/04-analysis-queries.sql
sql/05-data-quality-checks.sql
sql/06-reporting-views.sql
```

---

## 4. SQL Server Connection

The Python SQL loader reads connection information from environment variables.

Supported variables:

```text
SQL_SERVER
SQL_DATABASE
SQL_USERNAME
SQL_PASSWORD
SQL_DRIVER
```

Example configuration:

```bash
export SQL_SERVER="localhost"
export SQL_DATABASE="BusinessPerformanceDB"
export SQL_USERNAME="your_username"
export SQL_PASSWORD="your_password"
export SQL_DRIVER="ODBC Driver 18 for SQL Server"
```

Do not store real usernames or passwords in the GitHub repository.

---

## 5. Generate Raw Data

Run:

```bash
python python/generate_sample_data.py
```

This generates synthetic datasets in:

```text
data/raw/
```

Generated files:

```text
customers.csv
products.csv
regions.csv
dates.csv
sales.csv
```

---

## 6. Prepare and Validate Data

Run:

```bash
python python/prepare_data.py
```

This process:

- removes duplicate records
- validates required columns
- checks missing values
- validates foreign keys
- recalculates financial metrics
- generates DateID
- prepares fact and dimension tables

Processed files are written to:

```text
data/processed/
```

Generated analytical files:

```text
DimCustomer.csv
DimProduct.csv
DimRegion.csv
DimDate.csv
FactSales.csv
```

---

## 7. Load Data into SQL Server

After SQL Server is configured and the database tables exist, run:

```bash
python python/load_to_sql.py
```

The script loads the processed datasets into:

```text
DimCustomer
DimProduct
DimRegion
DimDate
FactSales
```

The operation runs inside a database transaction.

If an error occurs, the transaction is rolled back.

---

## 8. Run the Complete Pipeline

The complete workflow can be executed with one command:

```bash
python python/run_pipeline.py
```

This automatically runs:

```text
1. generate_sample_data.py
2. prepare_data.py
3. load_to_sql.py
```

---

## 9. Run Without SQL Server

The generation and transformation stages can be tested without SQL Server.

Run:

```bash
python python/run_pipeline.py --skip-sql
```

This executes:

```text
Generate Raw Data
        ↓
Clean and Transform Data
        ↓
Create Processed CSV Files
```

SQL Server loading is skipped.

---

## 10. SQL Analysis

After loading the database, analytical SQL queries are available in:

```text
sql/04-analysis-queries.sql
```

The queries cover:

- revenue analysis
- profitability analysis
- customer performance
- product performance
- regional performance
- monthly trends
- rankings
- running totals
- month-over-month growth

---

## 11. Data Quality Validation

Run:

```text
sql/05-data-quality-checks.sql
```

The script validates:

- duplicate records
- missing values
- invalid quantities
- negative financial values
- revenue calculations
- cost calculations
- profit calculations
- foreign key integrity
- dimension duplicates

---

## 12. Reporting Views

Reusable reporting views are created through:

```text
sql/06-reporting-views.sql
```

Views include:

```text
vw_SalesDetails
vw_MonthlyPerformance
vw_ProductPerformance
vw_CustomerPerformance
vw_RegionalPerformance
vw_ExecutiveKPIs
```

These views can be used as reporting sources for Power BI.

---

## 13. Power BI

The Power BI reporting layer is documented in:

```text
powerbi/README.md
```

DAX measures are documented in:

```text
powerbi/dax-measures.md
```

The analytical model follows a Star Schema:

```text
                 DimCustomer
                      |
                      |
DimProduct -------- FactSales -------- DimRegion
                      |
                      |
                   DimDate
```

---

## 14. Recommended Execution Order

For a complete fresh setup:

```text
1. Install Python dependencies
2. Configure SQL Server
3. Run 01-create-database.sql
4. Run 02-create-tables.sql
5. Configure SQL environment variables
6. Run run_pipeline.py
7. Run 05-data-quality-checks.sql
8. Run 06-reporting-views.sql
9. Connect Power BI
10. Build and validate dashboards
```

---

## 15. Security

Never commit:

```text
Passwords
Database credentials
API keys
Connection secrets
Private company data
Personal customer data
```

This repository uses synthetic business data for demonstration and portfolio purposes.

---

## 16. Pipeline Summary

```text
Python
  │
  ├── generate_sample_data.py
  │
  ▼
data/raw
  │
  ├── prepare_data.py
  │
  ▼
data/processed
  │
  ├── load_to_sql.py
  │
  ▼
SQL Server
  │
  ├── Analysis Queries
  ├── Data Quality Checks
  ├── Reporting Views
  │
  ▼
Power BI
  │
  ▼
Business Insights
```

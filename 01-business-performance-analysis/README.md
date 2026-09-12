# Business Performance Analysis

An end-to-end Business Intelligence and Data Analytics project demonstrating the complete workflow from raw data generation and ETL to SQL analysis, dimensional modeling, Power BI reporting, and business insights.

## Project Overview

This project simulates a real-world business analytics environment and demonstrates how raw transactional data can be transformed into reliable management information.

The solution combines:

- SQL Server
- Advanced SQL
- Python
- ETL
- Data Quality Validation
- Star Schema Modeling
- Power BI
- DAX
- KPI Development
- Business Intelligence
- Management Reporting

---

## Business Objectives

The project is designed to answer key management questions such as:

- How much revenue and profit is the business generating?
- Which products generate the highest revenue?
- Which products generate the highest profit?
- Who are the highest-value customers?
- Which customer segments perform best?
- Which regions contribute the most revenue?
- How is business performance changing over time?
- What is the current profit margin?
- What is the average order value?
- Which areas require management attention?

---

## Technology Stack

| Technology | Purpose |
|---|---|
| SQL Server | Analytical database |
| SQL | Data analysis and reporting |
| Python | Data generation and ETL |
| Pandas | Data preparation and validation |
| PyODBC | SQL Server connectivity |
| Power BI | Interactive reporting |
| DAX | KPI and analytical measures |
| Power Query | Data transformation |
| GitHub | Version control and documentation |

---

## Project Architecture

```text
Synthetic Business Data
        ↓
Python Data Generation
        ↓
data/raw
        ↓
Python ETL & Validation
        ↓
data/processed
        ↓
SQL Server
        ↓
Star Schema
        ↓
SQL Analysis & Reporting Views
        ↓
Power BI
        ↓
DAX Measures
        ↓
Interactive Dashboard
        ↓
Business Insights
```

---

## Repository Structure

```text
01-business-performance-analysis/
│
├── data/
│   └── README.md
│
├── docs/
│   ├── business-requirements.md
│   ├── data-dictionary.md
│   ├── data-model.md
│   ├── insights.md
│   └── setup-guide.md
│
├── powerbi/
│   ├── README.md
│   └── dax-measures.md
│
├── python/
│   ├── generate_sample_data.py
│   ├── prepare_data.py
│   ├── load_to_sql.py
│   └── run_pipeline.py
│
├── sql/
│   ├── 01-create-database.sql
│   ├── 02-create-tables.sql
│   ├── 03-load-sample-data.sql
│   ├── 04-analysis-queries.sql
│   ├── 05-data-quality-checks.sql
│   └── 06-reporting-views.sql
│
├── .env.example
├── requirements.txt
└── README.md
```

---

# Data Model

The analytical model follows a Star Schema.

```text
                 DimCustomer
                      |
                      |
DimProduct -------- FactSales -------- DimRegion
                      |
                      |
                   DimDate
```

### Fact Table

`FactSales`

Contains transactional measures including:

- Quantity
- Revenue
- Cost
- Profit
- Unit Price
- Unit Cost

### Dimension Tables

- `DimCustomer`
- `DimProduct`
- `DimRegion`
- `DimDate`

---

# SQL Development

The SQL layer demonstrates practical analytical SQL skills.

## Database Creation

```text
sql/01-create-database.sql
```

Creates:

`BusinessPerformanceDB`

---

## Star Schema Tables

```text
sql/02-create-tables.sql
```

Creates:

- DimCustomer
- DimProduct
- DimRegion
- DimDate
- FactSales

---

## Sample SQL Data

```text
sql/03-load-sample-data.sql
```

Provides a small demonstration dataset for quick SQL testing.

---

## Advanced SQL Analysis

```text
sql/04-analysis-queries.sql
```

Includes:

- Revenue analysis
- Profitability analysis
- Customer performance
- Product performance
- Regional analysis
- Monthly trends
- CTEs
- Window functions
- RANK
- DENSE_RANK
- LAG
- Running totals
- Revenue contribution
- Month-over-month growth

---

## Data Quality Validation

```text
sql/05-data-quality-checks.sql
```

Checks:

- Duplicate records
- Missing values
- Invalid quantities
- Negative values
- Revenue calculations
- Cost calculations
- Profit calculations
- Foreign key integrity
- Dimension consistency

---

## Reporting Views

```text
sql/06-reporting-views.sql
```

Creates reusable reporting views:

- `vw_SalesDetails`
- `vw_MonthlyPerformance`
- `vw_ProductPerformance`
- `vw_CustomerPerformance`
- `vw_RegionalPerformance`
- `vw_ExecutiveKPIs`

These views can be used as reporting sources for Power BI.

---

# Python Data Pipeline

## Step 1 — Generate Data

```text
python/generate_sample_data.py
```

Generates synthetic business data including:

- 200 customers
- 10 products
- 4 regions
- Daily calendar data
- 5,000 sales transactions

Raw datasets are written to:

```text
data/raw/
```

---

## Step 2 — Data Preparation

```text
python/prepare_data.py
```

Performs:

- Column validation
- Duplicate removal
- Missing-value checks
- Data-type conversion
- Financial metric recalculation
- Foreign-key validation
- Fact table preparation
- Dimension table preparation

Processed datasets are written to:

```text
data/processed/
```

---

## Step 3 — SQL Server Load

```text
python/load_to_sql.py
```

Loads the processed analytical datasets into SQL Server.

The operation uses database transactions and automatically rolls back if an error occurs.

---

## Step 4 — End-to-End Pipeline

```text
python/run_pipeline.py
```

Runs:

```text
Generate Data
      ↓
Prepare Data
      ↓
Validate Data
      ↓
Load SQL Server
```

The pipeline can also run without SQL Server:

```bash
python python/run_pipeline.py --skip-sql
```

---

# Key Performance Indicators

The analytical solution includes:

- Total Revenue
- Total Cost
- Total Profit
- Profit Margin %
- Total Orders
- Total Customers
- Total Units Sold
- Average Order Value
- Average Revenue per Customer
- Revenue per Unit
- Previous Month Revenue
- Month-over-Month Revenue Growth %
- Previous Year Revenue
- Year-over-Year Revenue Growth %
- Revenue YTD
- Profit YTD

---

# Power BI

The Power BI reporting layer is designed around four main pages.

## Executive Overview

Management-level overview of:

- Revenue
- Profit
- Margin
- Orders
- Customers
- Growth
- Top Products
- Regional Performance

## Sales Performance

Analysis of:

- Monthly Revenue
- Monthly Profit
- Product Performance
- Category Performance
- Units Sold
- Revenue Contribution
- Sales Growth

## Customer Analysis

Analysis of:

- Customer Revenue
- Customer Profitability
- Customer Segments
- Customer Rankings
- High-Value Customers

## Regional Performance

Analysis of:

- Regional Revenue
- Regional Profit
- Regional Orders
- Regional Rankings
- Revenue Contribution

---

# DAX

DAX measures are documented in:

```text
powerbi/dax-measures.md
```

The project demonstrates:

- Aggregation measures
- Ratio measures
- Time intelligence
- Ranking
- YTD calculations
- MoM growth
- YoY growth
- Revenue contribution

---

# Documentation

Detailed documentation is available in:

```text
docs/business-requirements.md
docs/data-dictionary.md
docs/data-model.md
docs/insights.md
docs/setup-guide.md
```

---

# Quick Start

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Generate and prepare the data without SQL Server:

```bash
python python/run_pipeline.py --skip-sql
```

For the complete SQL Server pipeline:

```bash
python python/run_pipeline.py
```

---

# Security

Database credentials are never stored directly in the source code.

Example environment configuration is provided in:

```text
.env.example
```

Real `.env` files, credentials, generated datasets, caches, and local development files are excluded through `.gitignore`.

---

# Skills Demonstrated

This project demonstrates practical experience with:

`SQL`  
`SQL Server`  
`Power BI`  
`DAX`  
`Python`  
`Pandas`  
`ETL`  
`Data Cleaning`  
`Data Validation`  
`Data Modeling`  
`Star Schema`  
`Business Intelligence`  
`KPI Development`  
`Window Functions`  
`CTEs`  
`Data Quality`  
`Management Reporting`  
`Git`  
`GitHub`

---

# Project Status

Core data architecture, SQL analytics, Python ETL pipeline, data-quality framework, Power BI model documentation, and DAX measures are implemented.

The interactive Power BI dashboard is the next reporting deliverable.

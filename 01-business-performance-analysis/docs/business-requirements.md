# Business Requirements

This document defines the main business questions, analytical requirements, and reporting objectives for the Business Performance Analysis project.

---

## Business Goal

The objective of this project is to provide management with a clear and measurable view of business performance.

The analytical solution should help decision-makers understand:

- Revenue performance
- Profitability
- Customer contribution
- Product performance
- Regional performance
- Sales trends
- Business growth

---

## Key Business Questions

### Overall Performance

- What is the total revenue?
- What is the total profit?
- What is the current profit margin?
- How many orders have been completed?
- How many units have been sold?
- What is the average order value?
- How many active customers are represented in the data?

---

### Revenue Analysis

- How is revenue changing over time?
- Which months generate the highest revenue?
- What is the month-over-month revenue growth?
- What is the year-over-year revenue growth?
- What percentage of total revenue comes from each product?

---

### Profitability Analysis

- Which products generate the most profit?
- Which product categories have the highest profit margin?
- Which regions are most profitable?
- Are high-revenue products also high-profit products?
- How does profitability change over time?

---

### Customer Analysis

- Who are the highest-value customers?
- Which customer segments generate the most revenue?
- Which customers generate the most profit?
- What is the average revenue per customer?
- How are customers distributed across regions and cities?

---

### Product Analysis

- Which products generate the highest revenue?
- Which products generate the highest profit?
- Which products have the highest sales volume?
- Which product categories perform best?
- What percentage of total revenue does each product contribute?

---

### Regional Analysis

- Which regions generate the highest revenue?
- Which regions generate the highest profit?
- How many orders are generated in each region?
- What percentage of total revenue comes from each region?
- Which regions show weaker business performance?

---

## Key Performance Indicators

The dashboard should provide the following KPIs:

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
- Month-over-Month Revenue Growth %
- Year-over-Year Revenue Growth %
- Revenue YTD
- Profit YTD

---

## Dashboard Requirements

The Power BI dashboard should contain four main reporting pages.

### Executive Overview

Designed for management-level monitoring.

Required elements:

- Total Revenue
- Total Profit
- Profit Margin %
- Total Orders
- Total Customers
- Average Order Value
- Revenue Trend
- Revenue Growth
- Top Products
- Top Regions

---

### Sales Performance

Required analysis:

- Revenue by month
- Profit by month
- Revenue by product
- Revenue by category
- Units sold
- Product rankings
- Revenue contribution
- Growth trends

---

### Customer Analysis

Required analysis:

- Revenue by customer
- Profit by customer
- Customer segment performance
- Customer ranking
- Average revenue per customer
- Top customers

---

### Regional Performance

Required analysis:

- Revenue by region
- Profit by region
- Orders by region
- Units sold by region
- Regional ranking
- Revenue contribution by region

---

## Filtering Requirements

Users should be able to filter the dashboard by:

- Year
- Quarter
- Month
- Customer
- Customer Segment
- Product
- Product Category
- Region
- City

---

## Data Model Requirements

The analytical solution should use a Star Schema.

The central fact table:

`FactSales`

Dimension tables:

- `DimCustomer`
- `DimProduct`
- `DimRegion`
- `DimDate`

Relationships should follow a one-to-many structure from each dimension to the fact table.

---

## Technical Requirements

The project uses:

- SQL Server for relational data storage and analysis
- SQL for data transformation and analytical queries
- Python for synthetic data generation
- Power BI for reporting and visualization
- Power Query for data preparation
- DAX for KPI calculations
- GitHub for version control and project documentation

---

## Expected Outcome

The final solution should allow a business user to move from a high-level management overview to detailed customer, product, regional, and time-based analysis.

The dashboard should support data-driven decision-making by highlighting:

- Performance trends
- Growth opportunities
- High-value customers
- High-performing products
- Regional differences
- Profitability drivers
- Potential areas requiring management attention

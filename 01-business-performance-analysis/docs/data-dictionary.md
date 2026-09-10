# Data Dictionary

This document describes the main tables and fields used in the Business Performance Analysis project.

---

## FactSales

The central fact table containing sales transaction data.

| Column | Data Type | Description |
|---|---|---|
| SalesID | INT | Unique identifier for each sales record |
| OrderID | NVARCHAR(50) | Unique business order identifier |
| DateID | INT | Foreign key to DimDate |
| CustomerID | INT | Foreign key to DimCustomer |
| ProductID | INT | Foreign key to DimProduct |
| RegionID | INT | Foreign key to DimRegion |
| Quantity | INT | Number of units sold |
| UnitPrice | DECIMAL(18,2) | Selling price per unit |
| UnitCost | DECIMAL(18,2) | Cost per unit |
| Revenue | DECIMAL(18,2) | Total sales revenue |
| Cost | DECIMAL(18,2) | Total transaction cost |
| Profit | DECIMAL(18,2) | Revenue minus cost |

## Business Logic

```text
Revenue = Quantity × UnitPrice
Cost = Quantity × UnitCost
Profit = Revenue - Cost
```

---

## DimCustomer

Contains descriptive information about customers.

| Column | Data Type | Description |
|---|---|---|
| CustomerID | INT | Unique customer identifier |
| CustomerName | NVARCHAR(150) | Customer or company name |
| CustomerSegment | NVARCHAR(100) | Customer classification |
| City | NVARCHAR(100) | Customer city |
| Country | NVARCHAR(100) | Customer country |

### Customer Segments

```text
Corporate
SME
Consumer
```

---

## DimProduct

Contains descriptive information about products.

| Column | Data Type | Description |
|---|---|---|
| ProductID | INT | Unique product identifier |
| ProductName | NVARCHAR(150) | Product name |
| Category | NVARCHAR(100) | Main product category |
| SubCategory | NVARCHAR(100) | Product subcategory |

### Example Categories

```text
Technology
Office
```

### Example Subcategories

```text
Computers
Displays
Accessories
Furniture
Equipment
```

---

## DimRegion

Contains geographic information used for regional analysis.

| Column | Data Type | Description |
|---|---|---|
| RegionID | INT | Unique region identifier |
| RegionName | NVARCHAR(100) | Business region |
| Country | NVARCHAR(100) | Country |

### Regions

```text
North
South
West
East
```

---

## DimDate

Calendar dimension used for time-series analysis and Power BI time intelligence.

| Column | Data Type | Description |
|---|---|---|
| DateID | INT | Date key in YYYYMMDD format |
| FullDate | DATE | Full calendar date |
| DayNumber | INT | Day of month |
| MonthNumber | INT | Month number from 1 to 12 |
| MonthName | NVARCHAR(20) | Month name |
| QuarterNumber | INT | Quarter number from 1 to 4 |
| YearNumber | INT | Calendar year |

### Example

```text
DateID: 20260115
FullDate: 2026-01-15
DayNumber: 15
MonthNumber: 1
MonthName: January
QuarterNumber: 1
YearNumber: 2026
```

---

# Source Dataset Files

The Python data-generation process creates the following CSV files.

## customers.csv

```text
CustomerID
CustomerName
CustomerSegment
City
Country
```

## products.csv

```text
ProductID
ProductName
Category
SubCategory
UnitPrice
UnitCost
```

## regions.csv

```text
RegionID
RegionName
Country
```

## dates.csv

```text
DateID
FullDate
DayNumber
MonthNumber
MonthName
QuarterNumber
YearNumber
```

## sales.csv

```text
SalesID
OrderID
OrderDate
CustomerID
ProductID
RegionID
Quantity
UnitPrice
UnitCost
DiscountRate
Revenue
Cost
Profit
```

---

# Source-to-Model Mapping

| Source Field | Analytical Model | Transformation |
|---|---|---|
| OrderDate | FactSales.DateID | Converted to YYYYMMDD key |
| CustomerID | FactSales.CustomerID | Direct mapping |
| ProductID | FactSales.ProductID | Direct mapping |
| RegionID | FactSales.RegionID | Direct mapping |
| Quantity | FactSales.Quantity | Direct mapping |
| UnitPrice | FactSales.UnitPrice | Direct mapping |
| UnitCost | FactSales.UnitCost | Direct mapping |
| Revenue | FactSales.Revenue | Direct mapping |
| Cost | FactSales.Cost | Direct mapping |
| Profit | FactSales.Profit | Direct mapping |
| DiscountRate | Source dataset | Available for extended analysis |

---

# Key Performance Indicators

## Total Revenue

```text
SUM(Revenue)
```

## Total Cost

```text
SUM(Cost)
```

## Total Profit

```text
SUM(Profit)
```

## Profit Margin %

```text
Total Profit / Total Revenue
```

## Total Orders

```text
Distinct Count of OrderID
```

## Total Customers

```text
Distinct Count of CustomerID
```

## Total Units Sold

```text
SUM(Quantity)
```

## Average Order Value

```text
Total Revenue / Total Orders
```

## Average Revenue per Customer

```text
Total Revenue / Total Customers
```

---

# Relationships

```text
DimCustomer[CustomerID] 1 → * FactSales[CustomerID]

DimProduct[ProductID] 1 → * FactSales[ProductID]

DimRegion[RegionID] 1 → * FactSales[RegionID]

DimDate[DateID] 1 → * FactSales[DateID]
```

---

# Data Quality Rules

- Primary keys must be unique.
- Foreign keys must match existing dimension records.
- Quantity must be greater than zero.
- UnitPrice must not be negative.
- UnitCost must not be negative.
- Revenue must not be negative.
- OrderID must not be null.
- DateID must correspond to a valid calendar date.
- CustomerID must exist in DimCustomer.
- ProductID must exist in DimProduct.
- RegionID must exist in DimRegion.

---

# Analytical Purpose

The data model supports:

- Revenue analysis
- Profitability analysis
- Customer analysis
- Product analysis
- Regional analysis
- Sales trend analysis
- KPI monitoring
- Ranking analysis
- Power BI dashboards
- SQL analytical queries
- DAX calculations
- Management reporting

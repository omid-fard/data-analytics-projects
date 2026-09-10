# Data Model

The Business Performance Analysis project uses a dimensional data model based on a Star Schema.

## Model Structure

The central fact table is:

`FactSales`

It is connected to four dimension tables:

- `DimCustomer`
- `DimProduct`
- `DimRegion`
- `DimDate`

## Star Schema

```text
                 DimCustomer
                      |
                      |
DimProduct -------- FactSales -------- DimRegion
                      |
                      |
                   DimDate
```

## FactSales

The FactSales table stores transactional sales data.

Main fields:

- SalesID
- OrderID
- DateID
- CustomerID
- ProductID
- RegionID
- Quantity
- UnitPrice
- UnitCost
- Revenue
- Cost
- Profit

## DimCustomer

Contains customer-related attributes.

Main fields:

- CustomerID
- CustomerName
- CustomerSegment
- City
- Country

## DimProduct

Contains product information.

Main fields:

- ProductID
- ProductName
- Category
- SubCategory

## DimRegion

Contains geographic information.

Main fields:

- RegionID
- RegionName
- Country

## DimDate

Contains calendar information used for time intelligence.

Main fields:

- DateID
- FullDate
- DayNumber
- MonthNumber
- MonthName
- QuarterNumber
- YearNumber

## Relationships

The model uses one-to-many relationships from each dimension table to FactSales.

```text
DimCustomer[CustomerID] → FactSales[CustomerID]

DimProduct[ProductID] → FactSales[ProductID]

DimRegion[RegionID] → FactSales[RegionID]

DimDate[DateID] → FactSales[DateID]
```

## Purpose

This model is designed to support:

- Power BI reporting
- DAX calculations
- KPI analysis
- Customer analysis
- Product analysis
- Regional analysis
- Time-series analysis
- Business performance monitoring

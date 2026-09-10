# DAX Measures

This file documents the main DAX measures used in the Business Performance Analysis Power BI dashboard.

---

## Total Revenue

```DAX
Total Revenue =
SUM(FactSales[Revenue])
```

## Total Cost

```DAX
Total Cost =
SUM(FactSales[Cost])
```

## Total Profit

```DAX
Total Profit =
SUM(FactSales[Profit])
```

## Profit Margin %

```DAX
Profit Margin % =
DIVIDE(
    [Total Profit],
    [Total Revenue],
    0
)
```

## Total Orders

```DAX
Total Orders =
DISTINCTCOUNT(FactSales[OrderID])
```

## Total Units Sold

```DAX
Total Units Sold =
SUM(FactSales[Quantity])
```

## Total Customers

```DAX
Total Customers =
DISTINCTCOUNT(FactSales[CustomerID])
```

## Average Order Value

```DAX
Average Order Value =
DIVIDE(
    [Total Revenue],
    [Total Orders],
    0
)
```

## Average Revenue per Customer

```DAX
Average Revenue per Customer =
DIVIDE(
    [Total Revenue],
    [Total Customers],
    0
)
```

## Revenue per Unit

```DAX
Revenue per Unit =
DIVIDE(
    [Total Revenue],
    [Total Units Sold],
    0
)
```

## Previous Month Revenue

```DAX
Previous Month Revenue =
CALCULATE(
    [Total Revenue],
    DATEADD(
        DimDate[FullDate],
        -1,
        MONTH
    )
)
```

## Month-over-Month Revenue Growth %

```DAX
MoM Revenue Growth % =
VAR PreviousRevenue =
    [Previous Month Revenue]

RETURN
DIVIDE(
    [Total Revenue] - PreviousRevenue,
    PreviousRevenue,
    0
)
```

## Previous Year Revenue

```DAX
Previous Year Revenue =
CALCULATE(
    [Total Revenue],
    DATEADD(
        DimDate[FullDate],
        -1,
        YEAR
    )
)
```

## Year-over-Year Revenue Growth %

```DAX
YoY Revenue Growth % =
VAR PreviousRevenue =
    [Previous Year Revenue]

RETURN
DIVIDE(
    [Total Revenue] - PreviousRevenue,
    PreviousRevenue,
    0
)
```

## Revenue YTD

```DAX
Revenue YTD =
TOTALYTD(
    [Total Revenue],
    DimDate[FullDate]
)
```

## Profit YTD

```DAX
Profit YTD =
TOTALYTD(
    [Total Profit],
    DimDate[FullDate]
)
```

## Product Revenue Rank

```DAX
Product Revenue Rank =
RANKX(
    ALL(DimProduct[ProductName]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)
```

## Customer Revenue Rank

```DAX
Customer Revenue Rank =
RANKX(
    ALL(DimCustomer[CustomerName]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)
```

## Region Revenue Rank

```DAX
Region Revenue Rank =
RANKX(
    ALL(DimRegion[RegionName]),
    [Total Revenue],
    ,
    DESC,
    DENSE
)
```

## Revenue Contribution %

```DAX
Revenue Contribution % =
DIVIDE(
    [Total Revenue],
    CALCULATE(
        [Total Revenue],
        ALL(DimProduct)
    ),
    0
)
```

---

## Usage

These measures are designed for use in KPI cards, tables, charts, trend analysis, rankings, and interactive Power BI dashboards.

Time-intelligence measures require `DimDate` to contain a complete continuous calendar and to be configured as the Power BI date table.

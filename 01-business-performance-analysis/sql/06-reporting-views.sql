-- =====================================================
-- Project: Business Performance Analysis
-- File: 06-reporting-views.sql
-- Purpose: Create reusable reporting views for Power BI
-- Database: SQL Server
-- =====================================================

USE BusinessPerformanceDB;
GO


-- =====================================================
-- 1. Detailed Sales View
-- =====================================================

CREATE OR ALTER VIEW vw_SalesDetails
AS
SELECT
    f.SalesID,
    f.OrderID,
    d.FullDate,
    d.DayNumber,
    d.MonthNumber,
    d.MonthName,
    d.QuarterNumber,
    d.YearNumber,

    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment,
    c.City AS CustomerCity,
    c.Country AS CustomerCountry,

    p.ProductID,
    p.ProductName,
    p.Category,
    p.SubCategory,

    r.RegionID,
    r.RegionName,

    f.Quantity,
    f.UnitPrice,
    f.UnitCost,
    f.Revenue,
    f.Cost,
    f.Profit,

    CASE
        WHEN f.Revenue = 0 THEN 0
        ELSE ROUND(
            f.Profit * 100.0 / f.Revenue,
            2
        )
    END AS ProfitMarginPercentage

FROM FactSales f

INNER JOIN DimDate d
    ON f.DateID = d.DateID

INNER JOIN DimCustomer c
    ON f.CustomerID = c.CustomerID

INNER JOIN DimProduct p
    ON f.ProductID = p.ProductID

INNER JOIN DimRegion r
    ON f.RegionID = r.RegionID;
GO


-- =====================================================
-- 2. Monthly Performance View
-- =====================================================

CREATE OR ALTER VIEW vw_MonthlyPerformance
AS
SELECT
    d.YearNumber,
    d.MonthNumber,
    d.MonthName,

    COUNT(DISTINCT f.OrderID) AS TotalOrders,
    COUNT(DISTINCT f.CustomerID) AS TotalCustomers,
    SUM(f.Quantity) AS TotalUnitsSold,

    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Cost) AS TotalCost,
    SUM(f.Profit) AS TotalProfit,

    ROUND(
        SUM(f.Profit) * 100.0 /
        NULLIF(SUM(f.Revenue), 0),
        2
    ) AS ProfitMarginPercentage,

    ROUND(
        SUM(f.Revenue) * 1.0 /
        NULLIF(COUNT(DISTINCT f.OrderID), 0),
        2
    ) AS AverageOrderValue

FROM FactSales f

INNER JOIN DimDate d
    ON f.DateID = d.DateID

GROUP BY
    d.YearNumber,
    d.MonthNumber,
    d.MonthName;
GO


-- =====================================================
-- 3. Product Performance View
-- =====================================================

CREATE OR ALTER VIEW vw_ProductPerformance
AS
SELECT
    p.ProductID,
    p.ProductName,
    p.Category,
    p.SubCategory,

    COUNT(DISTINCT f.OrderID) AS TotalOrders,
    SUM(f.Quantity) AS TotalUnitsSold,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Cost) AS TotalCost,
    SUM(f.Profit) AS TotalProfit,

    ROUND(
        SUM(f.Profit) * 100.0 /
        NULLIF(SUM(f.Revenue), 0),
        2
    ) AS ProfitMarginPercentage

FROM FactSales f

INNER JOIN DimProduct p
    ON f.ProductID = p.ProductID

GROUP BY
    p.ProductID,
    p.ProductName,
    p.Category,
    p.SubCategory;
GO


-- =====================================================
-- 4. Customer Performance View
-- =====================================================

CREATE OR ALTER VIEW vw_CustomerPerformance
AS
SELECT
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment,
    c.City,
    c.Country,

    COUNT(DISTINCT f.OrderID) AS TotalOrders,
    SUM(f.Quantity) AS TotalUnitsPurchased,

    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Cost) AS TotalCost,
    SUM(f.Profit) AS TotalProfit,

    ROUND(
        SUM(f.Revenue) * 1.0 /
        NULLIF(COUNT(DISTINCT f.OrderID), 0),
        2
    ) AS AverageOrderValue

FROM FactSales f

INNER JOIN DimCustomer c
    ON f.CustomerID = c.CustomerID

GROUP BY
    c.CustomerID,
    c.CustomerName,
    c.CustomerSegment,
    c.City,
    c.Country;
GO


-- =====================================================
-- 5. Regional Performance View
-- =====================================================

CREATE OR ALTER VIEW vw_RegionalPerformance
AS
SELECT
    r.RegionID,
    r.RegionName,
    r.Country,

    COUNT(DISTINCT f.OrderID) AS TotalOrders,
    COUNT(DISTINCT f.CustomerID) AS TotalCustomers,
    SUM(f.Quantity) AS TotalUnitsSold,

    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Cost) AS TotalCost,
    SUM(f.Profit) AS TotalProfit,

    ROUND(
        SUM(f.Profit) * 100.0 /
        NULLIF(SUM(f.Revenue), 0),
        2
    ) AS ProfitMarginPercentage

FROM FactSales f

INNER JOIN DimRegion r
    ON f.RegionID = r.RegionID

GROUP BY
    r.RegionID,
    r.RegionName,
    r.Country;
GO


-- =====================================================
-- 6. Executive KPI View
-- =====================================================

CREATE OR ALTER VIEW vw_ExecutiveKPIs
AS
SELECT
    SUM(Revenue) AS TotalRevenue,
    SUM(Cost) AS TotalCost,
    SUM(Profit) AS TotalProfit,

    ROUND(
        SUM(Profit) * 100.0 /
        NULLIF(SUM(Revenue), 0),
        2
    ) AS ProfitMarginPercentage,

    COUNT(DISTINCT OrderID) AS TotalOrders,
    COUNT(DISTINCT CustomerID) AS TotalCustomers,
    COUNT(DISTINCT ProductID) AS TotalProducts,
    SUM(Quantity) AS TotalUnitsSold,

    ROUND(
        SUM(Revenue) * 1.0 /
        NULLIF(COUNT(DISTINCT OrderID), 0),
        2
    ) AS AverageOrderValue,

    ROUND(
        SUM(Revenue) * 1.0 /
        NULLIF(COUNT(DISTINCT CustomerID), 0),
        2
    ) AS AverageRevenuePerCustomer

FROM FactSales;
GO


-- =====================================================
-- 7. Test Reporting Views
-- =====================================================

SELECT *
FROM vw_ExecutiveKPIs;
GO

SELECT *
FROM vw_MonthlyPerformance
ORDER BY
    YearNumber,
    MonthNumber;
GO

SELECT *
FROM vw_ProductPerformance
ORDER BY
    TotalRevenue DESC;
GO

SELECT *
FROM vw_CustomerPerformance
ORDER BY
    TotalRevenue DESC;
GO

SELECT *
FROM vw_RegionalPerformance
ORDER BY
    TotalRevenue DESC;
GO

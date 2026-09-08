-- =====================================================
-- Project: Business Performance Analysis
-- File: 04-analysis-queries.sql
-- Purpose: Business performance analysis with SQL
-- Database: SQL Server
-- =====================================================

USE BusinessPerformanceDB;
GO


-- =====================================================
-- 1. Overall Business Performance
-- =====================================================

SELECT
    SUM(Revenue) AS TotalRevenue,
    SUM(Cost) AS TotalCost,
    SUM(Profit) AS TotalProfit,
    SUM(Quantity) AS TotalUnitsSold,
    COUNT(DISTINCT OrderID) AS TotalOrders
FROM FactSales;
GO


-- =====================================================
-- 2. Profit Margin
-- =====================================================

SELECT
    SUM(Revenue) AS TotalRevenue,
    SUM(Profit) AS TotalProfit,
    ROUND(
        SUM(Profit) * 100.0 / NULLIF(SUM(Revenue), 0),
        2
    ) AS ProfitMarginPercentage
FROM FactSales;
GO


-- =====================================================
-- 3. Average Order Value
-- =====================================================

SELECT
    ROUND(
        SUM(Revenue) * 1.0 / NULLIF(COUNT(DISTINCT OrderID), 0),
        2
    ) AS AverageOrderValue
FROM FactSales;
GO


-- =====================================================
-- 4. Revenue by Product
-- =====================================================

SELECT
    p.ProductName,
    p.Category,
    SUM(f.Quantity) AS UnitsSold,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit
FROM FactSales f
INNER JOIN DimProduct p
    ON f.ProductID = p.ProductID
GROUP BY
    p.ProductName,
    p.Category
ORDER BY
    TotalRevenue DESC;
GO


-- =====================================================
-- 5. Revenue by Product Category
-- =====================================================

SELECT
    p.Category,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit,
    SUM(f.Quantity) AS TotalUnitsSold
FROM FactSales f
INNER JOIN DimProduct p
    ON f.ProductID = p.ProductID
GROUP BY
    p.Category
ORDER BY
    TotalRevenue DESC;
GO


-- =====================================================
-- 6. Customer Performance
-- =====================================================

SELECT
    c.CustomerName,
    c.CustomerSegment,
    c.City,
    COUNT(DISTINCT f.OrderID) AS TotalOrders,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit
FROM FactSales f
INNER JOIN DimCustomer c
    ON f.CustomerID = c.CustomerID
GROUP BY
    c.CustomerName,
    c.CustomerSegment,
    c.City
ORDER BY
    TotalRevenue DESC;
GO


-- =====================================================
-- 7. Regional Performance
-- =====================================================

SELECT
    r.RegionName,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit,
    SUM(f.Quantity) AS UnitsSold,
    COUNT(DISTINCT f.OrderID) AS TotalOrders
FROM FactSales f
INNER JOIN DimRegion r
    ON f.RegionID = r.RegionID
GROUP BY
    r.RegionName
ORDER BY
    TotalRevenue DESC;
GO


-- =====================================================
-- 8. Monthly Performance
-- =====================================================

SELECT
    d.YearNumber,
    d.MonthNumber,
    d.MonthName,
    SUM(f.Revenue) AS TotalRevenue,
    SUM(f.Profit) AS TotalProfit,
    SUM(f.Quantity) AS UnitsSold
FROM FactSales f
INNER JOIN DimDate d
    ON f.DateID = d.DateID
GROUP BY
    d.YearNumber,
    d.MonthNumber,
    d.MonthName
ORDER BY
    d.YearNumber,
    d.MonthNumber;
GO


-- =====================================================
-- 9. Product Ranking by Revenue
-- =====================================================

WITH ProductRevenue AS
(
    SELECT
        p.ProductName,
        SUM(f.Revenue) AS TotalRevenue
    FROM FactSales f
    INNER JOIN DimProduct p
        ON f.ProductID = p.ProductID
    GROUP BY
        p.ProductName
)

SELECT
    ProductName,
    TotalRevenue,
    RANK() OVER (
        ORDER BY TotalRevenue DESC
    ) AS RevenueRank
FROM ProductRevenue
ORDER BY
    RevenueRank;
GO


-- =====================================================
-- 10. Customer Ranking by Revenue
-- =====================================================

WITH CustomerRevenue AS
(
    SELECT
        c.CustomerName,
        SUM(f.Revenue) AS TotalRevenue
    FROM FactSales f
    INNER JOIN DimCustomer c
        ON f.CustomerID = c.CustomerID
    GROUP BY
        c.CustomerName
)

SELECT
    CustomerName,
    TotalRevenue,
    DENSE_RANK() OVER (
        ORDER BY TotalRevenue DESC
    ) AS CustomerRank
FROM CustomerRevenue
ORDER BY
    CustomerRank;
GO


-- =====================================================
-- 11. Revenue Contribution Percentage by Product
-- =====================================================

SELECT
    p.ProductName,
    SUM(f.Revenue) AS ProductRevenue,

    ROUND(
        SUM(f.Revenue) * 100.0 /
        NULLIF(
            SUM(SUM(f.Revenue)) OVER (),
            0
        ),
        2
    ) AS RevenueContributionPercentage

FROM FactSales f
INNER JOIN DimProduct p
    ON f.ProductID = p.ProductID

GROUP BY
    p.ProductName

ORDER BY
    ProductRevenue DESC;
GO


-- =====================================================
-- 12. Running Revenue Total
-- =====================================================

WITH MonthlyRevenue AS
(
    SELECT
        d.YearNumber,
        d.MonthNumber,
        d.MonthName,
        SUM(f.Revenue) AS MonthlyRevenue

    FROM FactSales f
    INNER JOIN DimDate d
        ON f.DateID = d.DateID

    GROUP BY
        d.YearNumber,
        d.MonthNumber,
        d.MonthName
)

SELECT
    YearNumber,
    MonthNumber,
    MonthName,
    MonthlyRevenue,

    SUM(MonthlyRevenue) OVER (
        ORDER BY YearNumber, MonthNumber
    ) AS RunningRevenue

FROM MonthlyRevenue

ORDER BY
    YearNumber,
    MonthNumber;
GO


-- =====================================================
-- 13. Previous Month Revenue
-- =====================================================

WITH MonthlyRevenue AS
(
    SELECT
        d.YearNumber,
        d.MonthNumber,
        d.MonthName,
        SUM(f.Revenue) AS MonthlyRevenue

    FROM FactSales f
    INNER JOIN DimDate d
        ON f.DateID = d.DateID

    GROUP BY
        d.YearNumber,
        d.MonthNumber,
        d.MonthName
)

SELECT
    YearNumber,
    MonthNumber,
    MonthName,
    MonthlyRevenue,

    LAG(MonthlyRevenue) OVER (
        ORDER BY YearNumber, MonthNumber
    ) AS PreviousMonthRevenue

FROM MonthlyRevenue

ORDER BY
    YearNumber,
    MonthNumber;
GO


-- =====================================================
-- 14. Month-over-Month Revenue Growth
-- =====================================================

WITH MonthlyRevenue AS
(
    SELECT
        d.YearNumber,
        d.MonthNumber,
        d.MonthName,
        SUM(f.Revenue) AS MonthlyRevenue

    FROM FactSales f
    INNER JOIN DimDate d
        ON f.DateID = d.DateID

    GROUP BY
        d.YearNumber,
        d.MonthNumber,
        d.MonthName
),

RevenueComparison AS
(
    SELECT
        YearNumber,
        MonthNumber,
        MonthName,
        MonthlyRevenue,

        LAG(MonthlyRevenue) OVER (
            ORDER BY YearNumber, MonthNumber
        ) AS PreviousMonthRevenue

    FROM MonthlyRevenue
)

SELECT
    YearNumber,
    MonthNumber,
    MonthName,
    MonthlyRevenue,
    PreviousMonthRevenue,

    ROUND(
        (
            MonthlyRevenue - PreviousMonthRevenue
        ) * 100.0 /
        NULLIF(PreviousMonthRevenue, 0),
        2
    ) AS MoMRevenueGrowthPercentage

FROM RevenueComparison

ORDER BY
    YearNumber,
    MonthNumber;
GO

-- =====================================================
-- Project: Business Performance Analysis
-- File: 05-data-quality-checks.sql
-- Purpose: Validate data quality and model integrity
-- Database: SQL Server
-- =====================================================

USE BusinessPerformanceDB;
GO


-- =====================================================
-- 1. Check Duplicate Order IDs
-- =====================================================

SELECT
    OrderID,
    COUNT(*) AS DuplicateCount
FROM FactSales
GROUP BY OrderID
HAVING COUNT(*) > 1;
GO


-- =====================================================
-- 2. Check Missing Values in FactSales
-- =====================================================

SELECT
    SUM(CASE WHEN OrderID IS NULL THEN 1 ELSE 0 END) AS MissingOrderID,
    SUM(CASE WHEN DateID IS NULL THEN 1 ELSE 0 END) AS MissingDateID,
    SUM(CASE WHEN CustomerID IS NULL THEN 1 ELSE 0 END) AS MissingCustomerID,
    SUM(CASE WHEN ProductID IS NULL THEN 1 ELSE 0 END) AS MissingProductID,
    SUM(CASE WHEN RegionID IS NULL THEN 1 ELSE 0 END) AS MissingRegionID,
    SUM(CASE WHEN Quantity IS NULL THEN 1 ELSE 0 END) AS MissingQuantity,
    SUM(CASE WHEN UnitPrice IS NULL THEN 1 ELSE 0 END) AS MissingUnitPrice,
    SUM(CASE WHEN UnitCost IS NULL THEN 1 ELSE 0 END) AS MissingUnitCost
FROM FactSales;
GO


-- =====================================================
-- 3. Check Invalid Quantities
-- =====================================================

SELECT *
FROM FactSales
WHERE Quantity <= 0;
GO


-- =====================================================
-- 4. Check Negative Prices or Costs
-- =====================================================

SELECT *
FROM FactSales
WHERE
    UnitPrice < 0
    OR UnitCost < 0
    OR Revenue < 0
    OR Cost < 0;
GO


-- =====================================================
-- 5. Check Profit Calculation
-- =====================================================

SELECT
    SalesID,
    OrderID,
    Revenue,
    Cost,
    Profit,
    Revenue - Cost AS ExpectedProfit
FROM FactSales
WHERE ABS(
    Profit - (Revenue - Cost)
) > 0.01;
GO


-- =====================================================
-- 6. Check Revenue Calculation
-- =====================================================

SELECT
    SalesID,
    OrderID,
    Quantity,
    UnitPrice,
    Revenue,
    Quantity * UnitPrice AS ExpectedRevenue
FROM FactSales
WHERE ABS(
    Revenue - (Quantity * UnitPrice)
) > 0.01;
GO


-- =====================================================
-- 7. Check Cost Calculation
-- =====================================================

SELECT
    SalesID,
    OrderID,
    Quantity,
    UnitCost,
    Cost,
    Quantity * UnitCost AS ExpectedCost
FROM FactSales
WHERE ABS(
    Cost - (Quantity * UnitCost)
) > 0.01;
GO


-- =====================================================
-- 8. Check Missing Customer References
-- =====================================================

SELECT
    f.SalesID,
    f.CustomerID
FROM FactSales f
LEFT JOIN DimCustomer c
    ON f.CustomerID = c.CustomerID
WHERE c.CustomerID IS NULL;
GO


-- =====================================================
-- 9. Check Missing Product References
-- =====================================================

SELECT
    f.SalesID,
    f.ProductID
FROM FactSales f
LEFT JOIN DimProduct p
    ON f.ProductID = p.ProductID
WHERE p.ProductID IS NULL;
GO


-- =====================================================
-- 10. Check Missing Region References
-- =====================================================

SELECT
    f.SalesID,
    f.RegionID
FROM FactSales f
LEFT JOIN DimRegion r
    ON f.RegionID = r.RegionID
WHERE r.RegionID IS NULL;
GO


-- =====================================================
-- 11. Check Missing Date References
-- =====================================================

SELECT
    f.SalesID,
    f.DateID
FROM FactSales f
LEFT JOIN DimDate d
    ON f.DateID = d.DateID
WHERE d.DateID IS NULL;
GO


-- =====================================================
-- 12. Check Duplicate Customers
-- =====================================================

SELECT
    CustomerName,
    COUNT(*) AS DuplicateCount
FROM DimCustomer
GROUP BY CustomerName
HAVING COUNT(*) > 1;
GO


-- =====================================================
-- 13. Check Duplicate Products
-- =====================================================

SELECT
    ProductName,
    COUNT(*) AS DuplicateCount
FROM DimProduct
GROUP BY ProductName
HAVING COUNT(*) > 1;
GO


-- =====================================================
-- 14. Check Duplicate Dates
-- =====================================================

SELECT
    FullDate,
    COUNT(*) AS DuplicateCount
FROM DimDate
GROUP BY FullDate
HAVING COUNT(*) > 1;
GO


-- =====================================================
-- 15. Data Quality Summary
-- =====================================================

SELECT
    COUNT(*) AS TotalSalesRecords,
    COUNT(DISTINCT OrderID) AS UniqueOrders,
    COUNT(DISTINCT CustomerID) AS CustomersUsed,
    COUNT(DISTINCT ProductID) AS ProductsUsed,
    COUNT(DISTINCT RegionID) AS RegionsUsed,
    MIN(Revenue) AS MinimumRevenue,
    MAX(Revenue) AS MaximumRevenue,
    AVG(Revenue) AS AverageRevenue,
    SUM(Revenue) AS TotalRevenue,
    SUM(Profit) AS TotalProfit
FROM FactSales;
GO

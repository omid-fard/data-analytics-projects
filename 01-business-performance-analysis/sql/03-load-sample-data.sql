-- =====================================================
-- Project: Business Performance Analysis
-- File: 03-load-sample-data.sql
-- Purpose: Load sample business data
-- Database: SQL Server
-- =====================================================

USE BusinessPerformanceDB;
GO

SET NOCOUNT ON;


-- =========================
-- Load Customers
-- =========================

IF NOT EXISTS (
    SELECT 1
    FROM DimCustomer
    WHERE CustomerName = 'Nova Retail GmbH'
)
BEGIN

    INSERT INTO DimCustomer
        (CustomerName, CustomerSegment, City, Country)
    VALUES
        ('Nova Retail GmbH', 'Corporate', 'Berlin', 'Germany'),
        ('Prime Solutions GmbH', 'Corporate', 'Frankfurt', 'Germany'),
        ('Urban Market GmbH', 'SME', 'Hamburg', 'Germany'),
        ('Digital Point GmbH', 'SME', 'Munich', 'Germany'),
        ('Central Trade GmbH', 'Corporate', 'Cologne', 'Germany');

END;
GO


-- =========================
-- Load Products
-- =========================

IF NOT EXISTS (
    SELECT 1
    FROM DimProduct
    WHERE ProductName = 'Business Laptop'
)
BEGIN

    INSERT INTO DimProduct
        (ProductName, Category, SubCategory)
    VALUES
        ('Business Laptop', 'Technology', 'Computers'),
        ('Office Monitor', 'Technology', 'Displays'),
        ('Ergonomic Chair', 'Office', 'Furniture'),
        ('Office Desk', 'Office', 'Furniture'),
        ('Wireless Headset', 'Technology', 'Accessories');

END;
GO


-- =========================
-- Load Regions
-- =========================

IF NOT EXISTS (
    SELECT 1
    FROM DimRegion
    WHERE RegionName = 'North'
)
BEGIN

    INSERT INTO DimRegion
        (RegionName, Country)
    VALUES
        ('North', 'Germany'),
        ('South', 'Germany'),
        ('West', 'Germany'),
        ('East', 'Germany');

END;
GO


-- =========================
-- Load Dates
-- =========================

IF NOT EXISTS (
    SELECT 1
    FROM DimDate
    WHERE DateID = 20260115
)
BEGIN

    INSERT INTO DimDate
        (
            DateID,
            FullDate,
            DayNumber,
            MonthNumber,
            MonthName,
            QuarterNumber,
            YearNumber
        )
    VALUES
        (20260115, '2026-01-15', 15, 1, 'January', 1, 2026),
        (20260210, '2026-02-10', 10, 2, 'February', 1, 2026),
        (20260305, '2026-03-05', 5, 3, 'March', 1, 2026),
        (20260418, '2026-04-18', 18, 4, 'April', 2, 2026),
        (20260512, '2026-05-12', 12, 5, 'May', 2, 2026),
        (20260620, '2026-06-20', 20, 6, 'June', 2, 2026);

END;
GO


-- =========================
-- Load Sales Transactions
-- =========================

IF NOT EXISTS (
    SELECT 1
    FROM FactSales
    WHERE OrderID = 'ORD-1001'
)
BEGIN

    INSERT INTO FactSales
    (
        OrderID,
        DateID,
        CustomerID,
        ProductID,
        RegionID,
        Quantity,
        UnitPrice,
        UnitCost,
        Revenue,
        Cost,
        Profit
    )
    VALUES

    (
        'ORD-1001',
        20260115,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Nova Retail GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Business Laptop'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'East'),
        10,
        1200.00,
        900.00,
        12000.00,
        9000.00,
        3000.00
    ),

    (
        'ORD-1002',
        20260210,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Prime Solutions GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Office Monitor'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'West'),
        20,
        350.00,
        250.00,
        7000.00,
        5000.00,
        2000.00
    ),

    (
        'ORD-1003',
        20260305,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Urban Market GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Ergonomic Chair'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'North'),
        15,
        450.00,
        300.00,
        6750.00,
        4500.00,
        2250.00
    ),

    (
        'ORD-1004',
        20260418,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Digital Point GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Office Desk'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'South'),
        8,
        700.00,
        500.00,
        5600.00,
        4000.00,
        1600.00
    ),

    (
        'ORD-1005',
        20260512,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Central Trade GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Wireless Headset'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'West'),
        30,
        180.00,
        110.00,
        5400.00,
        3300.00,
        2100.00
    ),

    (
        'ORD-1006',
        20260620,
        (SELECT CustomerID FROM DimCustomer WHERE CustomerName = 'Nova Retail GmbH'),
        (SELECT ProductID FROM DimProduct WHERE ProductName = 'Office Monitor'),
        (SELECT RegionID FROM DimRegion WHERE RegionName = 'East'),
        25,
        350.00,
        250.00,
        8750.00,
        6250.00,
        2500.00
    );

END;
GO

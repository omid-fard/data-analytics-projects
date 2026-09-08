-- =====================================================
-- Project: Business Performance Analysis
-- File: 02-create-tables.sql
-- Purpose: Create analytical tables using a star schema
-- Database: SQL Server
-- =====================================================

USE BusinessPerformanceDB;
GO


-- =========================
-- Customer Dimension
-- =========================

CREATE TABLE DimCustomer (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerName NVARCHAR(150) NOT NULL,
    CustomerSegment NVARCHAR(100),
    City NVARCHAR(100),
    Country NVARCHAR(100)
);
GO


-- =========================
-- Product Dimension
-- =========================

CREATE TABLE DimProduct (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(150) NOT NULL,
    Category NVARCHAR(100),
    SubCategory NVARCHAR(100)
);
GO


-- =========================
-- Region Dimension
-- =========================

CREATE TABLE DimRegion (
    RegionID INT IDENTITY(1,1) PRIMARY KEY,
    RegionName NVARCHAR(100) NOT NULL,
    Country NVARCHAR(100)
);
GO


-- =========================
-- Date Dimension
-- =========================

CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    FullDate DATE NOT NULL,
    DayNumber INT,
    MonthNumber INT,
    MonthName NVARCHAR(20),
    QuarterNumber INT,
    YearNumber INT
);
GO


-- =========================
-- Sales Fact Table
-- =========================

CREATE TABLE FactSales (
    SalesID INT IDENTITY(1,1) PRIMARY KEY,

    OrderID NVARCHAR(50) NOT NULL,

    DateID INT NOT NULL,
    CustomerID INT NOT NULL,
    ProductID INT NOT NULL,
    RegionID INT NOT NULL,

    Quantity INT NOT NULL,

    UnitPrice DECIMAL(18,2) NOT NULL,
    UnitCost DECIMAL(18,2) NOT NULL,

    Revenue DECIMAL(18,2),
    Cost DECIMAL(18,2),
    Profit DECIMAL(18,2),

    CONSTRAINT FK_FactSales_Date
        FOREIGN KEY (DateID)
        REFERENCES DimDate(DateID),

    CONSTRAINT FK_FactSales_Customer
        FOREIGN KEY (CustomerID)
        REFERENCES DimCustomer(CustomerID),

    CONSTRAINT FK_FactSales_Product
        FOREIGN KEY (ProductID)
        REFERENCES DimProduct(ProductID),

    CONSTRAINT FK_FactSales_Region
        FOREIGN KEY (RegionID)
        REFERENCES DimRegion(RegionID)
);
GO

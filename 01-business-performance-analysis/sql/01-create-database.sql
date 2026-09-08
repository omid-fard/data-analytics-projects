-- =====================================================
-- Project: Business Performance Analysis
-- File: 01-create-database.sql
-- Purpose: Create the project database
-- Database: SQL Server
-- =====================================================

IF DB_ID('BusinessPerformanceDB') IS NULL
BEGIN
    CREATE DATABASE BusinessPerformanceDB;
END;
GO

USE BusinessPerformanceDB;
GO

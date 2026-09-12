# =====================================================
# Project: Business Performance Analysis
# File: load_to_sql.py
# Purpose: Load processed CSV files into SQL Server
# =====================================================

from pathlib import Path
import os

import pandas as pd
import pyodbc


# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DATA_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)


# =====================================================
# SQL Server Configuration
# =====================================================
# Connection values can be provided through environment
# variables instead of hard-coding credentials.
#
# Example:
#
# SQL_SERVER=localhost
# SQL_DATABASE=BusinessPerformanceDB
# SQL_USERNAME=sa
# SQL_PASSWORD=your_password
# =====================================================

SQL_SERVER = os.getenv(
    "SQL_SERVER",
    "localhost"
)

SQL_DATABASE = os.getenv(
    "SQL_DATABASE",
    "BusinessPerformanceDB"
)

SQL_USERNAME = os.getenv(
    "SQL_USERNAME"
)

SQL_PASSWORD = os.getenv(
    "SQL_PASSWORD"
)

SQL_DRIVER = os.getenv(
    "SQL_DRIVER",
    "ODBC Driver 18 for SQL Server"
)


# =====================================================
# Build Connection String
# =====================================================

if SQL_USERNAME and SQL_PASSWORD:

    CONNECTION_STRING = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"UID={SQL_USERNAME};"
        f"PWD={SQL_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )

else:

    CONNECTION_STRING = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        f"Trusted_Connection=yes;"
        f"TrustServerCertificate=yes;"
    )


# =====================================================
# Required Processed Files
# =====================================================

required_files = {
    "DimCustomer": (
        PROCESSED_DATA_DIR
        / "DimCustomer.csv"
    ),
    "DimProduct": (
        PROCESSED_DATA_DIR
        / "DimProduct.csv"
    ),
    "DimRegion": (
        PROCESSED_DATA_DIR
        / "DimRegion.csv"
    ),
    "DimDate": (
        PROCESSED_DATA_DIR
        / "DimDate.csv"
    ),
    "FactSales": (
        PROCESSED_DATA_DIR
        / "FactSales.csv"
    ),
}


# =====================================================
# Validate Input Files
# =====================================================

missing_files = [
    str(file_path)
    for file_path
    in required_files.values()
    if not file_path.exists()
]

if missing_files:

    raise FileNotFoundError(
        "Missing processed data files:\n"
        + "\n".join(missing_files)
    )


# =====================================================
# Load Processed CSV Files
# =====================================================

dim_customer = pd.read_csv(
    required_files["DimCustomer"]
)

dim_product = pd.read_csv(
    required_files["DimProduct"]
)

dim_region = pd.read_csv(
    required_files["DimRegion"]
)

dim_date = pd.read_csv(
    required_files["DimDate"]
)

fact_sales = pd.read_csv(
    required_files["FactSales"]
)


# =====================================================
# Convert Date Column
# =====================================================

dim_date["FullDate"] = pd.to_datetime(
    dim_date["FullDate"]
).dt.date


# =====================================================
# Connect to SQL Server
# =====================================================

print(
    "Connecting to SQL Server..."
)

connection = pyodbc.connect(
    CONNECTION_STRING
)

connection.autocommit = False

cursor = connection.cursor()

cursor.fast_executemany = True


# =====================================================
# Helper Function
# =====================================================

def dataframe_rows(
    dataframe,
    columns,
):

    cleaned = dataframe[
        columns
    ].copy()

    cleaned = cleaned.where(
        pd.notnull(cleaned),
        None,
    )

    return [
        tuple(row)
        for row
        in cleaned.itertuples(
            index=False,
            name=None,
        )
    ]


# =====================================================
# Load Data
# =====================================================

try:

    print(
        "Clearing existing analytical data..."
    )

    # Fact table must be cleared first
    # because it references the dimensions.

    cursor.execute(
        "DELETE FROM FactSales;"
    )

    cursor.execute(
        "DELETE FROM DimDate;"
    )

    cursor.execute(
        "DELETE FROM DimCustomer;"
    )

    cursor.execute(
        "DELETE FROM DimProduct;"
    )

    cursor.execute(
        "DELETE FROM DimRegion;"
    )


    # =================================================
    # Reset Identity Values
    # =================================================

    cursor.execute(
        "DBCC CHECKIDENT "
        "('FactSales', RESEED, 0);"
    )

    cursor.execute(
        "DBCC CHECKIDENT "
        "('DimCustomer', RESEED, 0);"
    )

    cursor.execute(
        "DBCC CHECKIDENT "
        "('DimProduct', RESEED, 0);"
    )

    cursor.execute(
        "DBCC CHECKIDENT "
        "('DimRegion', RESEED, 0);"
    )


    # =================================================
    # Load DimCustomer
    # =================================================

    print(
        "Loading DimCustomer..."
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimCustomer ON;"
    )

    customer_columns = [
        "CustomerID",
        "CustomerName",
        "CustomerSegment",
        "City",
        "Country",
    ]

    customer_rows = dataframe_rows(
        dim_customer,
        customer_columns,
    )

    cursor.executemany(
        """
        INSERT INTO DimCustomer
        (
            CustomerID,
            CustomerName,
            CustomerSegment,
            City,
            Country
        )
        VALUES (?, ?, ?, ?, ?);
        """,
        customer_rows,
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimCustomer OFF;"
    )


    # =================================================
    # Load DimProduct
    # =================================================

    print(
        "Loading DimProduct..."
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimProduct ON;"
    )

    product_columns = [
        "ProductID",
        "ProductName",
        "Category",
        "SubCategory",
    ]

    product_rows = dataframe_rows(
        dim_product,
        product_columns,
    )

    cursor.executemany(
        """
        INSERT INTO DimProduct
        (
            ProductID,
            ProductName,
            Category,
            SubCategory
        )
        VALUES (?, ?, ?, ?);
        """,
        product_rows,
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimProduct OFF;"
    )


    # =================================================
    # Load DimRegion
    # =================================================

    print(
        "Loading DimRegion..."
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimRegion ON;"
    )

    region_columns = [
        "RegionID",
        "RegionName",
        "Country",
    ]

    region_rows = dataframe_rows(
        dim_region,
        region_columns,
    )

    cursor.executemany(
        """
        INSERT INTO DimRegion
        (
            RegionID,
            RegionName,
            Country
        )
        VALUES (?, ?, ?);
        """,
        region_rows,
    )

    cursor.execute(
        "SET IDENTITY_INSERT "
        "DimRegion OFF;"
    )


    # =================================================
    # Load DimDate
    # =================================================

    print(
        "Loading DimDate..."
    )

    date_columns = [
        "DateID",
        "FullDate",
        "DayNumber",
        "MonthNumber",
        "MonthName",
        "QuarterNumber",
        "YearNumber",
    ]

    date_rows = dataframe_rows(
        dim_date,
        date_columns,
    )

    cursor.executemany(
        """
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
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """,
        date_rows,
    )


    # =================================================
    # Load FactSales
    # =================================================

    print(
        "Loading FactSales..."
    )

    fact_columns = [
        "OrderID",
        "DateID",
        "CustomerID",
        "ProductID",
        "RegionID",
        "Quantity",
        "UnitPrice",
        "UnitCost",
        "Revenue",
        "Cost",
        "Profit",
    ]

    fact_rows = dataframe_rows(
        fact_sales,
        fact_columns,
    )

    cursor.executemany(
        """
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
            ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?
        );
        """,
        fact_rows,
    )


    # =================================================
    # Commit Transaction
    # =================================================

    connection.commit()

    print(
        "\n==================================="
    )

    print(
        "SQL LOAD COMPLETED SUCCESSFULLY"
    )

    print(
        "==================================="
    )

    print(
        f"DimCustomer: "
        f"{len(dim_customer):,} rows"
    )

    print(
        f"DimProduct: "
        f"{len(dim_product):,} rows"
    )

    print(
        f"DimRegion: "
        f"{len(dim_region):,} rows"
    )

    print(
        f"DimDate: "
        f"{len(dim_date):,} rows"
    )

    print(
        f"FactSales: "
        f"{len(fact_sales):,} rows"
    )

    print(
        f"\nDatabase: "
        f"{SQL_DATABASE}"
    )

    print(
        f"Server: "
        f"{SQL_SERVER}"
    )


# =====================================================
# Rollback on Error
# =====================================================

except Exception as error:

    connection.rollback()

    print(
        "\nSQL load failed."
    )

    print(
        f"Error: {error}"
    )

    raise


# =====================================================
# Close Connection
# =====================================================

finally:

    cursor.close()

    connection.close()

    print(
        "\nSQL Server connection closed."
    )

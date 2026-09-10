# =====================================================
# Project: Business Performance Analysis
# File: prepare_data.py
# Purpose: Clean, validate, and prepare generated data
#          for SQL Server and Power BI
# =====================================================

from pathlib import Path
import pandas as pd


# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =====================================================
# Load Data
# =====================================================

customers = pd.read_csv(
    RAW_DATA_DIR / "customers.csv"
)

products = pd.read_csv(
    RAW_DATA_DIR / "products.csv"
)

regions = pd.read_csv(
    RAW_DATA_DIR / "regions.csv"
)

dates = pd.read_csv(
    RAW_DATA_DIR / "dates.csv"
)

sales = pd.read_csv(
    RAW_DATA_DIR / "sales.csv"
)


# =====================================================
# Validate Required Columns
# =====================================================

required_sales_columns = [
    "SalesID",
    "OrderID",
    "OrderDate",
    "CustomerID",
    "ProductID",
    "RegionID",
    "Quantity",
    "UnitPrice",
    "UnitCost",
    "DiscountRate",
    "Revenue",
    "Cost",
    "Profit",
]

missing_columns = [
    column
    for column in required_sales_columns
    if column not in sales.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )


# =====================================================
# Remove Duplicates
# =====================================================

customers = customers.drop_duplicates(
    subset=["CustomerID"]
)

products = products.drop_duplicates(
    subset=["ProductID"]
)

regions = regions.drop_duplicates(
    subset=["RegionID"]
)

dates = dates.drop_duplicates(
    subset=["DateID"]
)

sales = sales.drop_duplicates(
    subset=["SalesID"]
)


# =====================================================
# Convert Data Types
# =====================================================

sales["OrderDate"] = pd.to_datetime(
    sales["OrderDate"],
    errors="coerce"
)

dates["FullDate"] = pd.to_datetime(
    dates["FullDate"],
    errors="coerce"
)


# =====================================================
# Missing Value Check
# =====================================================

critical_columns = [
    "OrderID",
    "OrderDate",
    "CustomerID",
    "ProductID",
    "RegionID",
    "Quantity",
    "UnitPrice",
    "UnitCost",
]

missing_summary = (
    sales[critical_columns]
    .isnull()
    .sum()
)

print("\nMissing values:")
print(missing_summary)


# =====================================================
# Remove Invalid Records
# =====================================================

sales = sales.dropna(
    subset=critical_columns
)

sales = sales[
    sales["Quantity"] > 0
]

sales = sales[
    sales["UnitPrice"] >= 0
]

sales = sales[
    sales["UnitCost"] >= 0
]


# =====================================================
# Create DateID
# =====================================================

sales["DateID"] = (
    sales["OrderDate"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)


# =====================================================
# Recalculate Financial Metrics
# =====================================================

sales["GrossRevenue"] = (
    sales["Quantity"]
    * sales["UnitPrice"]
)

sales["DiscountAmount"] = (
    sales["GrossRevenue"]
    * sales["DiscountRate"]
)

sales["Revenue"] = (
    sales["GrossRevenue"]
    - sales["DiscountAmount"]
)

sales["Cost"] = (
    sales["Quantity"]
    * sales["UnitCost"]
)

sales["Profit"] = (
    sales["Revenue"]
    - sales["Cost"]
)

sales["ProfitMargin"] = (
    sales["Profit"]
    / sales["Revenue"]
).fillna(0)


# =====================================================
# Validate Foreign Keys
# =====================================================

valid_customer_ids = set(
    customers["CustomerID"]
)

valid_product_ids = set(
    products["ProductID"]
)

valid_region_ids = set(
    regions["RegionID"]
)

valid_date_ids = set(
    dates["DateID"]
)

sales = sales[
    sales["CustomerID"].isin(
        valid_customer_ids
    )
]

sales = sales[
    sales["ProductID"].isin(
        valid_product_ids
    )
]

sales = sales[
    sales["RegionID"].isin(
        valid_region_ids
    )
]

sales = sales[
    sales["DateID"].isin(
        valid_date_ids
    )
]


# =====================================================
# Prepare Fact Table
# =====================================================

fact_sales = sales[
    [
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
].copy()


# =====================================================
# Prepare Dimension Tables
# =====================================================

dim_customer = customers[
    [
        "CustomerID",
        "CustomerName",
        "CustomerSegment",
        "City",
        "Country",
    ]
].copy()

dim_product = products[
    [
        "ProductID",
        "ProductName",
        "Category",
        "SubCategory",
    ]
].copy()

dim_region = regions[
    [
        "RegionID",
        "RegionName",
        "Country",
    ]
].copy()

dim_date = dates[
    [
        "DateID",
        "FullDate",
        "DayNumber",
        "MonthNumber",
        "MonthName",
        "QuarterNumber",
        "YearNumber",
    ]
].copy()


# =====================================================
# Export Processed Data
# =====================================================

dim_customer.to_csv(
    PROCESSED_DATA_DIR / "DimCustomer.csv",
    index=False
)

dim_product.to_csv(
    PROCESSED_DATA_DIR / "DimProduct.csv",
    index=False
)

dim_region.to_csv(
    PROCESSED_DATA_DIR / "DimRegion.csv",
    index=False
)

dim_date.to_csv(
    PROCESSED_DATA_DIR / "DimDate.csv",
    index=False
)

fact_sales.to_csv(
    PROCESSED_DATA_DIR / "FactSales.csv",
    index=False
)


# =====================================================
# Summary
# =====================================================

print("\n===================================")
print("ETL PROCESS COMPLETED")
print("===================================")

print(
    f"Customers: {len(dim_customer):,}"
)

print(
    f"Products: {len(dim_product):,}"
)

print(
    f"Regions: {len(dim_region):,}"
)

print(
    f"Dates: {len(dim_date):,}"
)

print(
    f"Sales Records: {len(fact_sales):,}"
)

print(
    f"Total Revenue: "
    f"{fact_sales['Revenue'].sum():,.2f}"
)

print(
    f"Total Profit: "
    f"{fact_sales['Profit'].sum():,.2f}"
)

print("\nProcessed files saved to:")
print(PROCESSED_DATA_DIR)

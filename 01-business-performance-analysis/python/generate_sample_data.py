# =====================================================
# Project: Business Performance Analysis
# File: generate_sample_data.py
# Purpose: Generate realistic synthetic business data
#          for SQL Server, ETL, and Power BI analysis
# =====================================================

from pathlib import Path
from datetime import datetime, timedelta
import random

import pandas as pd


# =====================================================
# Reproducibility
# =====================================================

random.seed(42)


# =====================================================
# Project Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =====================================================
# Configuration
# =====================================================

NUM_CUSTOMERS = 200
NUM_ORDERS = 5000

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 12, 31)


# =====================================================
# Customer Reference Data
# =====================================================

city_region_mapping = {
    "Hamburg": "North",
    "Hannover": "North",
    "Bremen": "North",
    "Kiel": "North",

    "Munich": "South",
    "Stuttgart": "South",
    "Nuremberg": "South",

    "Frankfurt": "West",
    "Cologne": "West",
    "Dusseldorf": "West",
    "Dortmund": "West",

    "Berlin": "East",
    "Leipzig": "East",
    "Dresden": "East",
}

cities = list(
    city_region_mapping.keys()
)

segments = [
    "Corporate",
    "SME",
    "Consumer",
]


# =====================================================
# Regions
# =====================================================

regions = [
    {
        "RegionID": 1,
        "RegionName": "North",
        "Country": "Germany",
    },
    {
        "RegionID": 2,
        "RegionName": "South",
        "Country": "Germany",
    },
    {
        "RegionID": 3,
        "RegionName": "West",
        "Country": "Germany",
    },
    {
        "RegionID": 4,
        "RegionName": "East",
        "Country": "Germany",
    },
]

regions_df = pd.DataFrame(
    regions
)

region_name_to_id = {
    row["RegionName"]: row["RegionID"]
    for row in regions
}


# =====================================================
# Customers
# =====================================================

customers = []

for customer_id in range(
    1,
    NUM_CUSTOMERS + 1,
):

    city = random.choice(
        cities
    )

    region_name = (
        city_region_mapping[city]
    )

    customers.append(
        {
            "CustomerID": customer_id,
            "CustomerName": (
                f"Customer {customer_id:03d}"
            ),
            "CustomerSegment": random.choice(
                segments
            ),
            "City": city,
            "Country": "Germany",
            "RegionID": region_name_to_id[
                region_name
            ],
        }
    )

customers_df = pd.DataFrame(
    customers
)


# =====================================================
# Products
# =====================================================

products = [
    {
        "ProductID": 1,
        "ProductName": "Business Laptop",
        "Category": "Technology",
        "SubCategory": "Computers",
        "UnitPrice": 1200.00,
        "UnitCost": 900.00,
    },
    {
        "ProductID": 2,
        "ProductName": "Office Monitor",
        "Category": "Technology",
        "SubCategory": "Displays",
        "UnitPrice": 350.00,
        "UnitCost": 250.00,
    },
    {
        "ProductID": 3,
        "ProductName": "Wireless Headset",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 180.00,
        "UnitCost": 110.00,
    },
    {
        "ProductID": 4,
        "ProductName": "Keyboard",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 90.00,
        "UnitCost": 45.00,
    },
    {
        "ProductID": 5,
        "ProductName": "Ergonomic Chair",
        "Category": "Office",
        "SubCategory": "Furniture",
        "UnitPrice": 450.00,
        "UnitCost": 300.00,
    },
    {
        "ProductID": 6,
        "ProductName": "Office Desk",
        "Category": "Office",
        "SubCategory": "Furniture",
        "UnitPrice": 700.00,
        "UnitCost": 500.00,
    },
    {
        "ProductID": 7,
        "ProductName": "Printer",
        "Category": "Office",
        "SubCategory": "Equipment",
        "UnitPrice": 320.00,
        "UnitCost": 220.00,
    },
    {
        "ProductID": 8,
        "ProductName": "Docking Station",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 210.00,
        "UnitCost": 130.00,
    },
    {
        "ProductID": 9,
        "ProductName": "Webcam",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 130.00,
        "UnitCost": 75.00,
    },
    {
        "ProductID": 10,
        "ProductName": "Conference Speaker",
        "Category": "Technology",
        "SubCategory": "Communication",
        "UnitPrice": 280.00,
        "UnitCost": 170.00,
    },
]

products_df = pd.DataFrame(
    products
)


# =====================================================
# Date Dimension
# =====================================================

date_range = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D",
)

dates_df = pd.DataFrame(
    {
        "FullDate": date_range,
    }
)

dates_df["DateID"] = (
    dates_df["FullDate"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dates_df["DayNumber"] = (
    dates_df["FullDate"].dt.day
)

dates_df["MonthNumber"] = (
    dates_df["FullDate"].dt.month
)

dates_df["MonthName"] = (
    dates_df["FullDate"]
    .dt.month_name()
)

dates_df["QuarterNumber"] = (
    dates_df["FullDate"].dt.quarter
)

dates_df["YearNumber"] = (
    dates_df["FullDate"].dt.year
)

dates_df = dates_df[
    [
        "DateID",
        "FullDate",
        "DayNumber",
        "MonthNumber",
        "MonthName",
        "QuarterNumber",
        "YearNumber",
    ]
]


# =====================================================
# Random Date Generator
# =====================================================

def random_date(
    start_date,
    end_date,
):
    number_of_days = (
        end_date - start_date
    ).days

    random_days = random.randint(
        0,
        number_of_days,
    )

    return (
        start_date
        + timedelta(days=random_days)
    )


# =====================================================
# Sales Transactions
# =====================================================

sales = []

discount_options = [
    0.00,
    0.00,
    0.00,
    0.00,
    0.05,
    0.05,
    0.10,
    0.15,
]

for sales_id in range(
    1,
    NUM_ORDERS + 1,
):

    customer = random.choice(
        customers
    )

    product = random.choice(
        products
    )

    order_date = random_date(
        START_DATE,
        END_DATE,
    )

    quantity = random.randint(
        1,
        20,
    )

    discount_rate = random.choice(
        discount_options
    )

    gross_revenue = (
        quantity
        * product["UnitPrice"]
    )

    discount_amount = (
        gross_revenue
        * discount_rate
    )

    revenue = (
        gross_revenue
        - discount_amount
    )

    cost = (
        quantity
        * product["UnitCost"]
    )

    profit = (
        revenue
        - cost
    )

    sales.append(
        {
            "SalesID": sales_id,
            "OrderID": (
                f"ORD-{sales_id:06d}"
            ),
            "OrderDate": (
                order_date.strftime(
                    "%Y-%m-%d"
                )
            ),
            "CustomerID": customer[
                "CustomerID"
            ],
            "ProductID": product[
                "ProductID"
            ],
            "RegionID": customer[
                "RegionID"
            ],
            "Quantity": quantity,
            "UnitPrice": round(
                product["UnitPrice"],
                2,
            ),
            "UnitCost": round(
                product["UnitCost"],
                2,
            ),
            "DiscountRate": round(
                discount_rate,
                2,
            ),
            "Revenue": round(
                revenue,
                2,
            ),
            "Cost": round(
                cost,
                2,
            ),
            "Profit": round(
                profit,
                2,
            ),
        }
    )

sales_df = pd.DataFrame(
    sales
)


# =====================================================
# Remove RegionID from Customer Export
# =====================================================
# RegionID is used internally to generate geographically
# consistent transactions but is not required by
# DimCustomer in the analytical model.
# =====================================================

customers_export_df = (
    customers_df[
        [
            "CustomerID",
            "CustomerName",
            "CustomerSegment",
            "City",
            "Country",
        ]
    ].copy()
)


# =====================================================
# Data Validation
# =====================================================

if customers_export_df[
    "CustomerID"
].duplicated().any():
    raise ValueError(
        "Duplicate CustomerID detected."
    )

if products_df[
    "ProductID"
].duplicated().any():
    raise ValueError(
        "Duplicate ProductID detected."
    )

if regions_df[
    "RegionID"
].duplicated().any():
    raise ValueError(
        "Duplicate RegionID detected."
    )

if dates_df[
    "DateID"
].duplicated().any():
    raise ValueError(
        "Duplicate DateID detected."
    )

if sales_df[
    "SalesID"
].duplicated().any():
    raise ValueError(
        "Duplicate SalesID detected."
    )

if sales_df[
    "OrderID"
].duplicated().any():
    raise ValueError(
        "Duplicate OrderID detected."
    )

if (
    sales_df["Quantity"] <= 0
).any():
    raise ValueError(
        "Invalid sales quantity detected."
    )

if (
    sales_df["UnitPrice"] < 0
).any():
    raise ValueError(
        "Negative UnitPrice detected."
    )

if (
    sales_df["UnitCost"] < 0
).any():
    raise ValueError(
        "Negative UnitCost detected."
    )


# =====================================================
# Export Raw CSV Files
# =====================================================

customers_export_df.to_csv(
    RAW_DATA_DIR / "customers.csv",
    index=False,
)

products_df.to_csv(
    RAW_DATA_DIR / "products.csv",
    index=False,
)

regions_df.to_csv(
    RAW_DATA_DIR / "regions.csv",
    index=False,
)

dates_df.to_csv(
    RAW_DATA_DIR / "dates.csv",
    index=False,
    date_format="%Y-%m-%d",
)

sales_df.to_csv(
    RAW_DATA_DIR / "sales.csv",
    index=False,
)


# =====================================================
# Summary
# =====================================================

total_revenue = (
    sales_df["Revenue"].sum()
)

total_cost = (
    sales_df["Cost"].sum()
)

total_profit = (
    sales_df["Profit"].sum()
)

profit_margin = (
    total_profit
    / total_revenue
    if total_revenue != 0
    else 0
)


print(
    "\n==================================="
)

print(
    "SAMPLE DATA GENERATION COMPLETED"
)

print(
    "==================================="
)

print(
    f"Customers: "
    f"{len(customers_export_df):,}"
)

print(
    f"Products: "
    f"{len(products_df):,}"
)

print(
    f"Regions: "
    f"{len(regions_df):,}"
)

print(
    f"Dates: "
    f"{len(dates_df):,}"
)

print(
    f"Sales Transactions: "
    f"{len(sales_df):,}"
)

print(
    f"Total Revenue: "
    f"{total_revenue:,.2f}"
)

print(
    f"Total Cost: "
    f"{total_cost:,.2f}"
)

print(
    f"Total Profit: "
    f"{total_profit:,.2f}"
)

print(
    f"Profit Margin: "
    f"{profit_margin:.2%}"
)

print(
    "\nRaw CSV files saved to:"
)

print(
    RAW_DATA_DIR
)

print(
    "\nGenerated files:"
)

print(
    "- customers.csv"
)

print(
    "- products.csv"
)

print(
    "- regions.csv"
)

print(
    "- dates.csv"
)

print(
    "- sales.csv"
)

# =====================================================
# Project: Business Performance Analysis
# File: generate_sample_data.py
# Purpose: Generate realistic sample business data
# =====================================================

import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)


# =========================
# Configuration
# =========================

NUM_CUSTOMERS = 200
NUM_ORDERS = 5000

START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 12, 31)


# =========================
# Customers
# =========================

cities = [
    "Berlin",
    "Frankfurt",
    "Hamburg",
    "Munich",
    "Cologne",
    "Dusseldorf",
    "Stuttgart",
    "Leipzig",
    "Dresden",
    "Hannover",
]

segments = [
    "Corporate",
    "SME",
    "Consumer",
]

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    customers.append(
        {
            "CustomerID": customer_id,
            "CustomerName": f"Customer {customer_id:03d}",
            "CustomerSegment": random.choice(segments),
            "City": random.choice(cities),
            "Country": "Germany",
        }
    )

customers_df = pd.DataFrame(customers)


# =========================
# Products
# =========================

products = [
    {
        "ProductID": 1,
        "ProductName": "Business Laptop",
        "Category": "Technology",
        "SubCategory": "Computers",
        "UnitPrice": 1200,
        "UnitCost": 900,
    },
    {
        "ProductID": 2,
        "ProductName": "Office Monitor",
        "Category": "Technology",
        "SubCategory": "Displays",
        "UnitPrice": 350,
        "UnitCost": 250,
    },
    {
        "ProductID": 3,
        "ProductName": "Wireless Headset",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 180,
        "UnitCost": 110,
    },
    {
        "ProductID": 4,
        "ProductName": "Keyboard",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 90,
        "UnitCost": 45,
    },
    {
        "ProductID": 5,
        "ProductName": "Ergonomic Chair",
        "Category": "Office",
        "SubCategory": "Furniture",
        "UnitPrice": 450,
        "UnitCost": 300,
    },
    {
        "ProductID": 6,
        "ProductName": "Office Desk",
        "Category": "Office",
        "SubCategory": "Furniture",
        "UnitPrice": 700,
        "UnitCost": 500,
    },
    {
        "ProductID": 7,
        "ProductName": "Printer",
        "Category": "Office",
        "SubCategory": "Equipment",
        "UnitPrice": 320,
        "UnitCost": 220,
    },
    {
        "ProductID": 8,
        "ProductName": "Docking Station",
        "Category": "Technology",
        "SubCategory": "Accessories",
        "UnitPrice": 210,
        "UnitCost": 130,
    },
]

products_df = pd.DataFrame(products)


# =========================
# Regions
# =========================

regions = [
    {"RegionID": 1, "RegionName": "North", "Country": "Germany"},
    {"RegionID": 2, "RegionName": "South", "Country": "Germany"},
    {"RegionID": 3, "RegionName": "West", "Country": "Germany"},
    {"RegionID": 4, "RegionName": "East", "Country": "Germany"},
]

regions_df = pd.DataFrame(regions)


# =========================
# Random Date Generator
# =========================

def random_date(start_date, end_date):

    delta = end_date - start_date

    random_days = random.randint(
        0,
        delta.days,
    )

    return start_date + timedelta(days=random_days)


# =========================
# Sales Transactions
# =========================

sales = []

for sales_id in range(1, NUM_ORDERS + 1):

    product = random.choice(products)

    quantity = random.randint(1, 20)

    discount_rate = random.choice(
        [
            0,
            0,
            0,
            0.05,
            0.10,
            0.15,
        ]
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

    order_date = random_date(
        START_DATE,
        END_DATE,
    )

    sales.append(
        {
            "SalesID": sales_id,
            "OrderID": f"ORD-{sales_id:06d}",
            "OrderDate": order_date.date(),
            "CustomerID": random.randint(
                1,
                NUM_CUSTOMERS,
            ),
            "ProductID": product["ProductID"],
            "RegionID": random.randint(
                1,
                4,
            ),
            "Quantity": quantity,
            "UnitPrice": product["UnitPrice"],
            "UnitCost": product["UnitCost"],
            "DiscountRate": discount_rate,
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

sales_df = pd.DataFrame(sales)


# =========================
# Date Dimension
# =========================

date_range = pd.date_range(
    start=START_DATE,
    end=END_DATE,
)

date_df = pd.DataFrame(
    {
        "FullDate": date_range,
    }
)

date_df["DateID"] = (
    date_df["FullDate"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

date_df["DayNumber"] = (
    date_df["FullDate"]
    .dt.day
)

date_df["MonthNumber"] = (
    date_df["FullDate"]
    .dt.month
)

date_df["MonthName"] = (
    date_df["FullDate"]
    .dt.month_name()
)

date_df["QuarterNumber"] = (
    date_df["FullDate"]
    .dt.quarter
)

date_df["YearNumber"] = (
    date_df["FullDate"]
    .dt.year
)

date_df = date_df[
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


# =========================
# Export CSV Files
# =========================

customers_df.to_csv(
    "customers.csv",
    index=False,
)

products_df.to_csv(
    "products.csv",
    index=False,
)

regions_df.to_csv(
    "regions.csv",
    index=False,
)

date_df.to_csv(
    "dates.csv",
    index=False,
)

sales_df.to_csv(
    "sales.csv",
    index=False,
)


# =========================
# Summary
# =========================

print("Sample data generated successfully.")
print(f"Customers: {len(customers_df)}")
print(f"Products: {len(products_df)}")
print(f"Regions: {len(regions_df)}")
print(f"Dates: {len(date_df)}")
print(f"Sales transactions: {len(sales_df)}")

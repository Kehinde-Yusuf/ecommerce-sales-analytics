import pandas as pd
from sqlalchemy import create_engine

# Read cleaned datasets
customers = pd.read_csv("cleaned_data/customers_cleaned.csv")
orders = pd.read_csv("cleaned_data/orders_cleaned.csv")
products = pd.read_csv("cleaned_data/products_cleaned.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:1234@localhost:5432/ecommerce_db_demo"
)

# Load customers table
customers.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)
# Load orders table
orders.to_sql(
    "orders",
    engine,
    if_exists="replace",
    index=False
)
# Load products table
products.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)

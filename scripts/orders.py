from pathlib import Path
import pandas as pd

#Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
#Read the Json File
orders = pd.read_json(BASE_DIR / "raw_data" / "orders.json")
products = pd.read_csv(BASE_DIR / "raw_data" / "products.csv")
customers = pd.read_csv(
    BASE_DIR / "raw_data" / "customers.txt",
    sep="|"
)

# Remove duplicate rows
orders = orders.drop_duplicates()

# Clean amount_paid column
orders["amount_paid"] = (
    orders["amount_paid"]
    .str.replace("₦", "", regex=False)
    .str.replace("NGN", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

orders["amount_paid"] = pd.to_numeric(orders["amount_paid"])

# Convert order_date to datetime
orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)

# Remove orders with invalid product IDs
orders = orders[
    orders["product_id"].isin(products["product_id"])
]

# Remove orders with invalid customer IDs
orders = orders[
    orders["customer_id"].isin(customers["id"])
]

# Save cleaned dataset
output_file = BASE_DIR / "cleaned_data" / "orders_cleaned.csv"

orders.to_csv(output_file, index=False)

# Final Summary
print("=" * 50)
print("ORDERS CLEANING SUMMARY")
print("=" * 50)

print(f"Final Shape: {orders.shape}")

print("\nMissing Values:")
print(orders.isna().sum())

print(f"\nDuplicate Rows: {orders.duplicated().sum()}")

print("\n✅ Cleaned dataset saved successfully!")
print(f"Location: {output_file}")
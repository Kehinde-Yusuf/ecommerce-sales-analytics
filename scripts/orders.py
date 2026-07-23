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
#Show the first 5 rows
print("\nFirst Five Rows")
print(orders.head())

print("\nDataset Shapes:")
print(orders.shape)

print("\nColumn Names:")
print(orders.columns)

print("\nData Types:")
print(orders.dtypes)

print("\nMissing Values:")
print(orders.isnull().sum())


print("\nDuplicate Rows:")
print(orders.duplicated().sum())

print("\nDuplicate Rows:")
print(orders[orders.duplicated()])

orders = orders.drop_duplicates()
print("\nDuplicate Rows After Cleaning:")
print(orders.duplicated().sum())

print("\nFinal Dataset Shape:")
print(orders.shape)

print("\nRows with Missing Amount Paid:")
print(orders[orders["amount_paid"].isna()])

orders["amount_paid"] =(
    orders["amount_paid"]
    .str.replace("₦", "", regex=False)
    .str.replace("NGN", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

orders["amount_paid"] = pd.to_numeric(orders["amount_paid"])
print("\nNew Data Type")
print(orders["amount_paid"])
print(orders["amount_paid"].dtype)

print("\nSample Order Date:")
print(orders["order_date"].head(15))

print("\nOriginal Order Dates:")
print(orders["order_date"].head(20))

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)
print("\nData Type:")
print(orders["order_date"].dtype)

print("\nMissing Dates:")
print(orders["order_date"].isna().sum())

print(orders["order_date"].head(20))
print("\nRows with Missing Dates:")
print(orders[orders["order_date"].isna()])

print("=" * 50)
print("ORDERS DATASET FINAL CHECK")
print("=" * 50)

print("\nShape:")
print(orders.shape)

print("\nData Types:")
print(orders.dtypes)

print("\nMissing Values:")
print(orders.isna().sum())

print("\nDuplicate Rows:")
print(orders.duplicated().sum())
#Remove orders with invalid product IDS
orders = orders[
    orders["product_id"].isin(products["product_id"])
]
#Remove orders with invalid customer IDS
orders = orders[
    orders["customer_id"].isin(customers["id"])
]
output_file = BASE_DIR / "cleaned_data" / "orders_cleaned.csv"

orders.to_csv(output_file, index=False)

print("\n✅ Cleaned dataset saved successfully!")
print(output_file)

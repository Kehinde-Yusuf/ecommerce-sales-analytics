import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

products = pd.read_csv(BASE_DIR / "raw_data" / "products.csv")

print(products.head())

print("\nDataset Shape:")
print(products.shape)

print("\nColumn Names:")
print(products.columns)

print("\nData Types:")
print(products.dtypes)

print("\nMissing Values:")
print(products.isnull().sum())

print("\nDuplicate Rows:")
print(products.duplicated().sum())

print("\nUnique Categories:")
print(products["category"].unique())

print("\nNumber of Categories:")
print(products["category"].nunique())

print("\nSample Cost Prices:")
print(products["cost_price"].head(10))

products["cost_price"] = (
    products["cost_price"]
    .str.replace("₦", "", regex=False)
    .str.replace("NGN", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
print("\nCleaned Cost Prices:")
print(products["cost_price"].head(10))

products["cost_price"] = pd.to_numeric(products["cost_price"])

print("\nNew Data Type:")
print(products["cost_price"].dtype)

print("\nSample Selling Prices:")
print(products["selling_price"].head(10))

products["selling_price"] = (
   products["selling_price"]
   .str.replace("₦", "", regex=False)
   .str.replace("NGN", "", regex=False)
   .str.replace(",", "", regex=False)
   .str.strip()
)
print("\nCleaned Selling Prices") 
print(products["selling_price"].head(10))

products["selling_price"] = pd.to_numeric(products["selling_price"])
print("\nNew Data Type:")
print(products["selling_price"].dtype)

products["category"] = (
    products["category"]
    .str.replace(">", "|", regex=False)
    .str.replace(",", "|", regex=False)
    .str.replace("|", " | ", regex=False)
    .str.replace("  ", " ",regex=False)
    .str.strip()
)

print("\nCleaned Categories:")
print(products["category"].unique())
print("\nNumber of Categories:")
print(products["category"].nunique())

products.loc[48, "category"] = "Groceries | Cereals"
products.loc[97, "category"] = "Electronics | Audio"

print("\nMissing Categories:")
print(products["category"].isna().sum())

print("\nRows with Missing Categories:")
print(products[products["category"].isna()])

print("\nDuplicated Rows:")
print(products[products.duplicated()])

products = products.drop_duplicates()

products[["category", "sub_category"]] = (
    products["category"]
    .str.split("|", expand=True)
)
print(products.head())
products["category"] = products["category"].str.strip()
products["sub_category"] = products["sub_category"].str.strip()
print(products[["cost_price", "selling_price"]].head(10))

print("\nDuplicated Rows:")
print(products.duplicated().sum())

print("\nFinal Dataset Shape:")
print(products.shape)

print("\nMissing Values:")
print(products.isna().sum())

print("\nDuplicate Rows:")
print(products.duplicated().sum())

print("\nRow with Missing Cost Price:")
print(products[products["cost_price"].isna()])
print("\nRows with Missing Selling Price:")
print(products[products["selling_price"].isna()])
print(products["category"].head(10))
print(products["sub_category"].head(10))

output_file = BASE_DIR / "cleaned_data" / "products_cleaned.csv"

products.to_csv(output_file, index=False)

print("\n✅ Cleaned dataset saved successfully!")
print(output_file)

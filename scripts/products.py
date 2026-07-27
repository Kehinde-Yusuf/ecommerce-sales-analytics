import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

products = pd.read_csv(BASE_DIR / "raw_data" / "products.csv")

# Clean cost_price
products["cost_price"] = (
    products["cost_price"]
    .str.replace("₦", "", regex=False)
    .str.replace("NGN", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

products["cost_price"] = pd.to_numeric(products["cost_price"])

# Clean selling_price
products["selling_price"] = (
    products["selling_price"]
    .str.replace("₦", "", regex=False)
    .str.replace("NGN", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

products["selling_price"] = pd.to_numeric(products["selling_price"])

# Clean category
products["category"] = (
    products["category"]
    .str.replace(">", "|", regex=False)
    .str.replace(",", "|", regex=False)
    .str.replace("|", " | ", regex=False)
    .str.replace("  ", " ", regex=False)
    .str.strip()
)

# Fix inconsistent categories
products.loc[48, "category"] = "Groceries | Cereals"
products.loc[97, "category"] = "Electronics | Audio"

# Remove duplicates
products = products.drop_duplicates()

# Split category and subcategory
products[["category", "sub_category"]] = (
    products["category"]
    .str.split("|", expand=True)
)

products["category"] = products["category"].str.strip()
products["sub_category"] = products["sub_category"].str.strip()

# Save cleaned dataset
output_file = BASE_DIR / "cleaned_data" / "products_cleaned.csv"

products.to_csv(output_file, index=False)

# Final Summary
print("=" * 50)
print("PRODUCTS CLEANING SUMMARY")
print("=" * 50)

print(f"Final Shape: {products.shape}")

print("\nMissing Values:")
print(products.isna().sum())

print(f"\nDuplicate Rows: {products.duplicated().sum()}")

print("\n✅ Cleaned dataset saved successfully!")
print(f"Location: {output_file}")
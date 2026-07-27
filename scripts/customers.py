from pathlib import Path
import pandas as pd

#Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
#Read the text File
customers = pd.read_csv(
    BASE_DIR / "raw_data" / "customers.txt",
    sep="|"
)

#Remove duplicate rows
customers = customers.drop_duplicates()

#Convert DOB column to datetime
customers["dob"] = pd.to_datetime(
    customers["dob"],
    format="mixed",
    errors="coerce"
) 

#Save cleaned dataset
output_file = BASE_DIR / "cleaned_data" / "customers_cleaned.csv"

customers.to_csv(output_file, index=False)

#Final Summary
print("=" * 50)
print("CUSTOMERS CLEANING SUMMARY")
print("=" * 50)

print(f"Final Shape;: {customers.shape}")

print("\nMissing Values:")
print(customers.isna().sum())

print(f"nDuplicate Rows: {customers.duplicated().sum()}")
print("\n✅ Cleaned dataset saved successfully!")
print(f"Location:(output_file)")


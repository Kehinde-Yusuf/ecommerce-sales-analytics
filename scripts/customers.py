from pathlib import Path
import pandas as pd

#Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent
#Read the text File
customers = pd.read_csv(
    BASE_DIR / "raw_data" / "customers.txt",
    sep="|"
)

print("=" * 50)
print("Customers Dataset")
print("=" * 50)

print("\nFirst Five Rows:")
print(customers.head())

print("\nDataset Shape:")
print(customers.shape)

print("\nDataset Columns:")
print(customers.columns)

print("\nDataset Data Types")
print(customers.dtypes)

print("\nMissing Values")
print(customers.isna().sum())

print("\nDuplicated Rows")
print(customers.duplicated().sum())

#To see exactly where the duplicate is
print("\nDuplicate Rows")
print(customers[customers.duplicated()])
#To solve it, we will drop the duplicate
customers = customers.drop_duplicates()

print("\nFinal Shapes:")
print(customers.shape)
print("\nDuplicate Rows")
print(customers.duplicated().sum())

#We are moving to Missing Values now
print("\nRows with Missing Date of Birth:")
print(customers[customers["dob"].isna()])

print("\nRows with Missing Email:")
print(customers[customers["email"].isna()])

customers["dob"] = pd.to_datetime(
    customers["dob"],
    format="mixed",
    errors="coerce"
) 
print("\nDataset Dob Type:")
print(customers["dob"].dtype)

print("\nMissing DOB:")
print(customers[customers["dob"].isna()])

print("\nSample DOB:")
print(customers["dob"].head(15))

print("=" * 50)
print("CUSTOMERS DATASET FINAL CHECK")
print("=" * 50)

print("\nShape:")
print(customers.shape)

print("\nData Types:")
print(customers.dtypes)

print("\nMissing Values:")
print(customers.isna().sum())

print("\nDuplicate Rows:")
print(customers.duplicated().sum())

output_file = BASE_DIR / "cleaned_data" / "customers_cleaned.csv"

customers.to_csv(output_file, index=False)

print("\n✅ Cleaned dataset saved successfully!")
print(output_file)

print(customers.head())
print(customers.info())
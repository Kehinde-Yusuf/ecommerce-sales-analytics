from pathlib import Path
import pandas as pd
#Get the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

products = pd.read_csv(BASE_DIR / "cleaned_data" / "products_cleaned.csv")
orders = pd.read_csv(BASE_DIR / "cleaned_data" / "orders_cleaned.csv")
customers = pd.read_csv(BASE_DIR / "cleaned_data" / "customers_cleaned.csv")

print("=" * 50)
print("REFERENTIAL INTEGRITY CHECK")
print("=" * 50)

print("\nProducts Shape:")
print(products.shape)

print("\nOrders Shape:")
print(orders.shape)

print("\nCustomers Shape:")
print(customers.shape)

print("\nChecking Products IDs...")

invalid_products = orders[
    ~orders["product_id"].isin(products["product_id"])
]
print(invalid_products)

print("\nChecking Customer IDs...")

invalid_customers = orders[
    ~orders["customer_id"].isin(customers["id"])
]
print(invalid_customers)

print("\nMerging Orders with Products")
orders_with_price = orders.merge(
    products[["product_id", "selling_price"]],
    on="product_id",
    how="left"
)
print(orders_with_price.head())
print(orders_with_price[orders_with_price["selling_price"].isna()])
# print(products[products["product_id"] ==79])
# print(products[products["product_id"] ==59])
# print(products[products["product_id"] ==86])
# print(products[products["product_id"] ==13])
orders_with_price["expected_amount"] =(
    orders_with_price["quantity_purchased"] *orders_with_price["selling_price"]
) 
print(orders_with_price.head())

orders_with_price["difference"] = (
    orders_with_price["amount_paid"]
    - orders_with_price["expected_amount"]
)
print(
    orders_with_price[
        [
            "order_id",
            "amount_paid",
            "expected_amount",
            "difference"
        ]
    ].head(10)
)


print("\nOrders needs review:")
orders_needing_review = orders_with_price[
    orders_with_price["difference"].isna()
]
print(orders_needing_review)

payment_mismatches = orders_with_price[
    (orders_with_price["difference"].notna()) &
    (orders_with_price["difference"] !=0)
]
print(payment_mismatches)

print(orders["quantity_purchased"].describe())
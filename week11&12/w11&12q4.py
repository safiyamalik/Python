# Original catalog prices
Catalog_Prices = {
    "Laptop": 80000,
    "Mobile": 20000,
    "Headphones": 2000
}

# Sale updates (flash sale prices)
Sale_Updates = {
    "Mobile": 18000,
    "Headphones": 1500
}

# Merge dictionaries (Sale_Updates overwrite Catalog_Prices)
Catalog_Prices.update(Sale_Updates)

# Print final prices
print("Updated Catalog Prices:")
print(Catalog_Prices)
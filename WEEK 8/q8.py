name = input("Enter product name: ")

if len(name) < 2:
    print("Output: ''")
else:
    sku = name[:2] + name[-2:]
    print("SKU Code:", sku)
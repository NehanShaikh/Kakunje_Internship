# Dictionary of products and their prices
products = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000
}

print("Available products:", products.keys())

product_name = input("Enter product name: ").lower()

if product_name in products:
    print("Price:", products[product_name])
else:
    print("Product not found")

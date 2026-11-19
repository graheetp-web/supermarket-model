# Supermarket shopping list with prices
items = [
    {"name": "Milk", "price": 3.49},
    {"name": "Bread", "price": 2.99},
    {"name": "Eggs", "price": 4.19},
    {"name": "Chicken Breast", "price": 9.99},
    {"name": "Apples", "price": 1.50},
    {"name": "Rice", "price": 5.49},
    {"name": "Tomatoes", "price": 2.79},
    {"name": "Cheese", "price": 4.25},
    {"name": "Yogurt", "price": 1.39},
    {"name": "Orange Juice", "price": 3.99}
]

# Calculate total cost
total = sum(item["price"] for item in items)

# Display the list and total
print("Supermarket Shopping List:")
for i, item in enumerate(items, 1):
    print(f"{i}. {item['name']}: ${item['price']:.2f}")
print(f"\nTotal estimated cost: ${total:.2f}")
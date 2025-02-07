# Real-world scenario: Grocery shopping with decision-making

# Variables for the grocery shopping scenario
budget = 1000  # Total money you have for shopping
available_in_store = ["Milk", "Eggs", "Bread", "Rice", "Apples"]  # Items available in the store
grocery_list = ["Milk", "Eggs", "Chicken", "Rice", "Apples"]  # Items you need to buy
already_at_home = ["Chicken"]  # Items you already have at home
total_spent = 0

# Prices of items
item_prices = {
    "Milk": 50,
    "Eggs": 60,
    "Chicken": 250,
    "Rice": 80,
    "Apples": 100
}

# Control flow to decide what to buy
for item in grocery_list:
    if item in already_at_home:  # If the item is already at home, skip it
        print(f"{item} is already at home, skipping.")
        continue
    
    if item not in available_in_store:  # If the item is not in the store
        print(f"{item} is not available in the store, mark for later.")
        continue
    
    price = item_prices[item]
    
    if total_spent + price <= budget:  # Check if you can afford the item
        print(f"Buying {item} for {price} INR.")
        total_spent += price
    else:
        print(f"Not enough budget to buy {item}. Skipping it.")

# Output total spent
print(f"\nTotal money spent: {total_spent} INR")
print(f"Money left: {budget - total_spent} INR")

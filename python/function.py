# Function to abstract the process of ordering food
def place_order(dish_name, quantity, price_per_dish):
    # Calculate total cost
    total_cost = quantity * price_per_dish
    
    # Apply discount if the total cost exceeds 500
    discount = 0
    if total_cost > 500:
        discount = 0.1 * total_cost  # 10% discount
    
    final_cost = total_cost - discount
    
    # Print the order summary
    print(f"Order Summary:")
    print(f"Dish: {dish_name}")
    print(f"Quantity: {quantity}")
    print(f"Price per Dish: {price_per_dish} INR")
    print(f"Total cost: {total_cost} INR")
    
    if discount > 0:
        print(f"Discount applied: {discount} INR")
    
    print(f"Final cost: {final_cost} INR")
    print("----------------------\n")
    
    return final_cost

# Example usage of the abstracted function
place_order("Pizza", 3, 200)  # Ordering 3 pizzas, each priced at 200 INR
place_order("Pasta", 2, 150)  # Ordering 2 pastas, each priced at 150 INR

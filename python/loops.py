# List of items to pack
items_to_pack = ["Shirt", "Pants", "Shoes", "Toothbrush", "Charger", "Towel"]
already_packed_items = ["Shoes"]  # Skip packing items that are already packed
bag_capacity = 4
items_packed = 0

print("Packing items:")

for item in items_to_pack:
    if item in already_packed_items:
        print(f"{item} is already packed. Skipping.")
        continue  # Skip the already packed item

    print(f"Packing {item}...")
    items_packed += 1

    if items_packed >= bag_capacity:  # Stop packing when the bag is full
        print("Bag is full. Stopping.")
        break

print(f"Total items packed: {items_packed}\n")

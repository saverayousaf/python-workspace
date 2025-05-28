# Q5: Shopping list program
shopping_list = ["milk", "bread", "eggs", "butter", "juice", "sugar", "salt", "biscuits", "tea", "coffee"]

print("Current shopping list:")
for item in shopping_list:
    print("-", item)


add_item = input("Do you want to add an item? (yes/no): ").lower()
if add_item == 'yes':
    new_item = input("Enter item to add: ")
    shopping_list.append(new_item)
    print(f"Added {new_item} to list.")


remove_item = input("Do you want to remove an item? (yes/no): ").lower()
if remove_item == 'yes':
    item_to_remove = input("Enter item to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"Removed {item_to_remove} from list.")
    else:
        print("Item not found")


print("Updated shopping list:")
for item in shopping_list:
    print("-", item)

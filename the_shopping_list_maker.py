# Task 1: Write a function that lets the user add items to a list
items = ['gaming chair', 'headphone', 'monitor', 'scuff controller', 'speaker']
def user_list():
    while True:
        print("\nUser list")
        print("1. View Inventroy")
        print("2. Remove Item From Inventory")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nUser list: ")
            for item in items[:5]:
                print(item)
        elif choice == '2':
            unwanted_item = input("Remove Item from Inventory: ")
            if unwanted_item in items:
                items.remove(unwanted_item)
                print(f"{unwanted_item} has been removed")
            else:
                print(f"{unwanted_item}Unwanted item was not found in the lsit")
        elif choice =='3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again")
user_list()


# Task 2: Include a function to remove items from the list.

# Taks 3: Add a function that prints out the entire list in a formated way
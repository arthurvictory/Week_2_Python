# 1) Build a Shopping Cart

# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# shopping menu function
def shopping_menu():
    
    while True:

        print("""
            <<-----Shopping Menu----->>
            1. Add item
            2. Delete Item
            3. View Shopping Cart
            4. Quit
        """)

        option = input("Choose your option: ")

        if option == "1":
            add_item()
        elif option == "2":
            del_item()
        elif option == "3":
            view_cart()
        elif option == "4":
            print("Thank you for shopping at V-Mart!")
            print(*shopping_list, sep = ", ")
            break
        else:
            print("That is not a valid choice!")

shopping_list = []
# add item/price function
def add_item():
    item = input("Add item to your shopping list: ")
    shopping_list.append(item)
    print(f"{item} has been added to your cart.")

# remove item function
def del_item():
    item = input("Remove item from your shopping list: ")
    shopping_list.remove(item)
    print(f"{item} has been removed from your cart.")

# view cart function
def view_cart():
    print(*shopping_list, sep = ", ")


shopping_menu()
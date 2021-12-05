print("""
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

""")
print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

""")
print("""
***********************************
** What would you like to order? **
***********************************
""")
menu = [
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon",
    "Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea", "Unicorn Tears",
]


def menu_input():
    user_choice = input("> ")
    for menu in range(1):
        if user_choice == "quit":
            print("Exiting have a good day")
        if user_choice == menu:
            print(f" 1 order of {user_choice} have been added to your meal")


menu_input()

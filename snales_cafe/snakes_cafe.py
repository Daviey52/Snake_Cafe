def menu_items():
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

if __name__ == "__main__":
    menu_items()

    def menu_input():
        user_choice = input("> ")
        items_ordered = []
        count = 1
        while user_choice:
            if user_choice == "quit":
                print("Exiting have a good day")
                break
            if user_choice != "quit":
                items_ordered.append(user_choice)
                if user_choice == items_ordered:
                    count += 1
                print(
                    f" {count} order of {user_choice} has been added to your meal")
                user_choice
                break

    menu_input()

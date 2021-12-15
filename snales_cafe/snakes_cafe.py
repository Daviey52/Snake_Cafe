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


menu_order = [
    {
        "Name": "Wings",
        "Count": 0
    },
    {
        "Name": "Cookies",
        "Count": 0
    },
    {
        "Name": "Spring Rolls",
        "Count": 0
    },
    {
        "Name": "Salmon",
        "Count": 0
    }, {
        "Name": "steak",
        "Count": 0
    },
    {
        "Name": "Meat Tornado",
        "Count": 0
    },
    {
        "Name": "A literal Garden",
        "Count": 0
    },
    {
        "Name": "Ice Cream",
        "Count": 0
    },
    {
        "Name": "Cake",
        "Count": 0
    },
    {
        "Name": "Pie",
        "Count": 0
    },
    {
        "Name": "Coffee",
        "Count": 0
    },
    {
        "Name": "Tea",
        "Count": 0
    },
    {
        "Name": "Unicorn Tears",
        "Count": 0
    }

]

if __name__ == "__main__":
    menu_items()
    user_choice = ""

    while user_choice != "quit":
        user_choice = input(">").capitalize()

        for item in menu_order:
            if item["Name"] == user_choice:
                item["Count"] += 1
                if item["Count"] > 1:
                    noun = "order"
                    verb = "has"

                else:
                    noun = "orders"
                    verb = "have"

                print(
                    f' {item["Count"]} {noun} of {item["Name"]} {verb} been added to your meal')

        if user_choice == "Quit":
            print("Exiting have a good day")
            break

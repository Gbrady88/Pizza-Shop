# Author: Gerald Brady
# IST 140 Fall semester 2021
# LM8: Final Project
# December 10, 2021

# Function to display intro and menu to the app
def intro():
    menu = "1.Pizza \n2.Steaks \n3.Register \n4.Coupon \n5.More about Sammy B's \n6.Exit"
    print("Welcome to Sammy B's Pizza & Steaks!")
    print("We have a few options to choose from to get you started: \n")
    print(menu)


# Displays intro
intro()
# User makes a selection from menu
selection = input("\nPlease make a selection. Type the corresponding number to make a selection: ")


# Selection 1 (Pizza)
def pizza():
    # Dictionary of pizza toppings
    toppings = {"cheese": 10, "pepperoni": 12, "sausage": 12, "supreme": 14, "meats": 14.50, "veggie": 12}

    print("We have a few pizza choices to pick from:")
    print("Cheese \nPepperoni \nSausage \nSupreme \nMeats \nVeggie \nOr type ""Menu"" to return back to the main menu")
    pizzaType = input("\nPlease make a selection: ").lower()

    # Keeps user in pizza ordering unless menu is selected
    while pizzaType != "menu":
        pizzaMessage = "You selected " + pizzaType + " pizza"
        steakAdd = "Would you like to add a steak to your order? "

        if pizzaType == "cheese":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    return
            print("Your order comes to $" + str(toppings["cheese"]))
            break
        elif pizzaType == "pepperoni":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(toppings["pepperoni"]))
            break
        elif pizzaType == "sausage":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(toppings["sausage"]))
            break
        elif pizzaType == "supreme":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(toppings["supreme"]))
            break
        elif pizzaType == "meats":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(toppings["meats"]))
            break
        elif pizzaType == "veggie":
            print(pizzaMessage)
            yesORno = input(steakAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    steaks()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(toppings["veggie"]))
            break

        else:
            print("Your selection was invalid. Please try again.")
            pizza()


# Selection 2 (Steaks)
def steaks():
    beef = 9
    chicken = 8

    american = 2
    swiss = 2
    provolone = 3
    wiz = 2.75

    steakProtein = input("Do you want Beef or Chicken? \nOr type ""Menu"" to return back to the main menu:\n").lower()

    # Keeps user in Steaks ordering unless menu is selected
    while steakProtein != "menu":
        steakMessage = "You selected " + steakProtein + " steak"
        pizzaAdd = "Would you like to add a pizza to your order? "
        cheeseSelection = "What kind of cheese for your steak? \nAmerican, Swiss, Provolone, or Wiz: "
        cheese = input(cheeseSelection)
        # Options for cheese
        if steakProtein == "beef":
            print(steakMessage)
            if cheese == "american":
                total = beef + american
            elif cheese == "swiss":
                total = beef + swiss
            elif cheese == "provolone":
                total = beef + provolone
            elif cheese == "wiz":
                total = beef + wiz
            else:
                print("Invalid choice, please make a correct selection. ")
                cheese = input(cheeseSelection)
            yesORno = input(pizzaAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    pizza()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(total))
            break
        elif steakProtein == "chicken":
            print(steakMessage)
            if cheese == "american":
                total = chicken + american
            elif cheese == "swiss":
                total = chicken + swiss
            elif cheese == "provolone":
                total = chicken + provolone
            elif cheese == "wiz":
                total = chicken + wiz
            else:
                print("Invalid choice, please make a correct selection. ")
                cheese = input(cheeseSelection)
            yesORno = input(pizzaAdd)
            while yesORno != "no":
                if yesORno == "yes":
                    pizza()
                else:
                    print("Your selection was invalid. We will just do your current order.")
                    break
            print("Your order comes to $" + str(total))
            break

        else:
            print("Your selection was invalid. Please try again.")
            steaks()


# Selection 3 (Registration)
def register():
    name = input("What is your full name? ")
    email = input("What is your email address? ")
    verify = input("You entered in\nName: " + name + "\nEmail: " + email + "\nIs that correct? Yes or No: ").lower()
    if verify == "yes":
        print("You have successfully registered.")
    else:
        register()


# Selection 4 (Coupon)
def coupon(two_off):
    print("Your order qualifies for $2 off a pizza order.")

    pizza()


# Selection 5 (Info on Sammy)
def info():
    print("\nStarting as a hobby and love for pizza, Samuel starting selling pizzas out of his parents garage. \nHis "
          "first customers were just his friends which soon grew to neighbors, and eventually now a center city "
          "location. \nMost customers say they can taste the passion in his sauce which is a old family recipe."
          "\nYou will not be disappointed with our famous pizzas and now our new steaks. Enjoy Beef or Chicken!")


# Selection 6 (Exit app)
def exit_app():
    print("\nThank you for visiting Sammy B's \nPlease come again!")


# List to hold total
price = []

# The first (outer) loop
while selection != "6":

    if selection == "1":
        pizza()
        break

    elif selection == "2":
        steaks()
        break

    elif selection == "3":
        register()
        print("\nFrom the main menu...")
        selection = input("Please make a selection: ")

    elif selection == "4":
        coupon()
        break

    elif selection == "5":
        info()
        print("\nFrom the main menu...")
        selection = input("Please make a selection: ")

    else:
        print("You selection was invalid. Please try again.")

exit_app()

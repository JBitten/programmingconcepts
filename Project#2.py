# Beverage class
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Vending Machine class
class VendingMachine:
    def __init__(self, beverages):
        self.beverages = beverages

    def display_menu(self):
        print("\nVending Machine Menu")
        for i in range(len(self.beverages)):
            print(i + 1, "-", self.beverages[i].name, "$", self.beverages[i].price)

    def vend(self):
        while True:
            self.display_menu()

            choice = int(input("Select a beverage (1-6): "))

            if choice < 1 or choice > 6:
                print("Invalid selection.")
                continue

            drink = self.beverages[choice - 1]
            print("You selected:", drink.name)

            money = float(input("Insert money: "))

            if money < drink.price:
                print("Not enough money. Please add more money.")
            else:
                change = money - drink.price
                print("Dispensing", drink.name)
                print("Your change is $", round(change, 2))


# Create beverages
b1 = Beverage("Coke", 1.50)
b2 = Beverage("Pepsi", 1.50)
b3 = Beverage("Water", 1.00)
b4 = Beverage("Juice", 2.00)
b5 = Beverage("Tea", 1.75)
b6 = Beverage("Coffee", 2.25)

# Create vending machine
machine = VendingMachine([b1, b2, b3, b4, b5, b6])

# Start machine
machine.vend()

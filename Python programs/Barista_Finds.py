print("Welcome to the Cofffer's Cafe!!")

name = input("What may be your name?\n")

print("Hello " + name + ", nice to meet you!\n\n\n")

menu = ["Black coffee", "Cappcino", "Americano", "Espresso", "Latte", "Mocha"]


print("What would you like to have today from the menu?\n")
print(menu)

order = input("\n")

quantity = int(input("How many would you like?\n"))

if order == "Black Coffee":
    price = str(quantity * 3)
    print("That will be $" + price + ". Thank you!!")
elif order == "Cappcino":
    price = str(quantity * 4.5)
    print("That will be $" + price + ". Thank you!!")
elif order == "Americano":
    price = str(quantity * 7)
    print("That will be $" + price + ". Thank you!!")
elif order == "Espresso":
    price = str(quantity * 6)
    print("That will be $" + price + ". Thank you!!")
elif order == "Latte":
    cream = input("Would you like wipped cream in your latte?\n")
    if cream == "Yes":
        price = str(quantity * 6.5)
        print("That will be $" + price + ". Thank you!!")
    else:
        price = str(quantity * 5.5)
        print("That will be $" + price + ". Thank you!!")
elif order == "Mocha":
    price = str(quantity * 7)
    print("That will be $" + price + ". Thank you!!")
else:
    print("Sorry, we don't sell that here")
input()

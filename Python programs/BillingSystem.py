discount = 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
while(True):
    memberShip = input("Do you want to become a member? (y/n)")
    if memberShip == 'y':
        memberCard = input("Which membership card do you want to apply for? (gold/silver/bronze)")
        if memberCard == 'gold':
            print("Congratulations! You have become a gold member!")
            print("You will be receiving a 30% discount in your purchases now!!")
            discount = 30
            break
        elif memberCard == 'silver':
            print("Congratulations! You have become a silver member!")
            print("You will be receiving a 20% discount in your purchases now!!")
            discount = 20
            break
        elif memberCard == 'bronze':
            print("Congratulations! You have become a bronze member!")
            print("You will be receiving a 10% discount in your purchases now!!")
            discount = 10
            break
        else:
            print("Invalid membership card!")
            continue

    elif memberShip == 'n':
        print("You can still shop with us!")
        break

    else:
        print("Invalid input!")
        continue

userPurchase = input("Do you want to purchase anything?")
if userPurchase == 'y':
    print("S.N0\tItem\tPrice")
    print("1\tApple\t100")
    print("2\tBanana\t50")
    print("3\tOrange\t80")
    print("4\tMango\t150")
    print("5\tPineapple\t200")

    print("What do you want to purchase?")
    item = int(input("Enter the item number: "))
    quantity = int(input("Enter the quantity: "))
    if item == 1:
        price = 100
    elif item == 2:
        price = 50
    elif item == 3:
        price = 80
    elif item == 4:
        price = 150
    elif item == 5:
        price = 200
    else:
        print("Invalid item number!")
        price = 0

    if price > 0:
        total = price * quantity
        print("The total price is: ", total)
        print("You have received a discount of ", discount, "%")
        finalPrice = total - (total * discount / 100)
        print("The final price is: ", finalPrice)
    
elif userPurchase == 'n':
    print("Thank you for visiting us!")

else:
    print("Invalid input!")

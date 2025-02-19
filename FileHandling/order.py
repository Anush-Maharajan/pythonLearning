order ="order.txt"
def orders():

    with open("FileHandling/order.txt", "a") as file:
        customerOrder = input("What do you want?\n")
        file.write(f"{customerOrder},INPROCESS\n")

orders()

def readOrders():
    with open("FileHandling/order.txt", "r") as file:
        ordered = file.readlines()
        # print(" ".join(ordered))
        print()

readOrders()
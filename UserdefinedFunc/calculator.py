# Defining the calculaor function
def calc(a, o, b):
    # Definning Addition Function
    def add(a, b):
        return a+b
    # Defining subtraction Function
    def sub(a, b):
        return a-b
    # Checking which operation needs to be done
    if o == "+":
        return add(a, b)
    
    elif o == "-":
        return sub(a, b)

    # returns invalid if unknown operant is used
    return "Invalid"

# ask for two numbers and a na operant
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
op = input("Do you want to add[+] or subract[-]: ")

# call the function to do the operation
res = calc(x, op, y)

# prints the result
print(res)
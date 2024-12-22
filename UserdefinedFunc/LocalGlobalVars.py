# Defining a global variable
msg = "Hello, World!!"

#defining a function
def greet():
    # creating a local variable
    msg = "Hello, Sanshar!!"
    print(f"Inside msg: {msg}")

# calling the function
greet()

# Printing the global variable
print(f"Outside msg: {msg}")


print("\n\n\n")

# Defining a global variable
msg = "Hello, World!!"

#defining a function
def greet():
    # calling the global variable
    global msg
    # Now changes in this varible changes the global variable value
    msg = "Hello, Sanshar!!"
    print(f"Inside msg: {msg}")

# calling the function
greet()

# Printing the global variable
print(f"Outside msg: {msg}")
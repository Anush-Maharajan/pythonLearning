for i in range(1,5):
    print("I", i)
    for j in range(1,5):
        print("\tJ", j)

print("\n\n\n\n")

for i in range(1,10):
    print()
    for j in range(i,10):
        print("*", end="")
    for j in range(10-i,10):
        print(" ", end="")
    for j in range(i,10):
        print("*", end="")
randNum = 4
x = 0 
count = 0
print("Guess the number!!!\n\n")

while x != randNum:
    x = int(input("Enter the Number: "))
    if x > randNum:
        print("the number is very big!!")
    if x< randNum:
        print("The number is very small")
    count+=1

print("-"*40)
print("Congratulaions!!!")
print("You completed the challenge within", count, "time(s)!!")
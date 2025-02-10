# multiplicationNumber = int(input("Enter the number you want to multiply: "))
# for i in range(1,11):
#     print(multiplicationNumber, "X", i, "=" ,multiplicationNumber*i )

i, j = 1 , 1
while i < 11 and j < 11:
    print(f"{i} X {j} = {i*j}")
    if j >= 10:
        print()
        i+= 1
        j = 0
    j += 1
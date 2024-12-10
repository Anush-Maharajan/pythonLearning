n = 10
#right-angled left triangle
for i in range(1,n + 1):
    print("*"*i)
    i+=1
#right-angled right triangle
for i in range(1,n + 1):
    print("*"*(n - i))
    i+=1

# Pyramid pattern
for i in range(1,n + 1):
    j = n - i
    while j > 0:
        print(end=" ")
        j-=1
    k=1
    while k <= 2*i - 1:
        print("*",end="")
        k+=1
    print()

for i in range(1,n + 1):
    k=1
    while k <= i*i - 1:
        print(end=" ")
        k+=1
    j = n*n - i*i
    while j > 0:
        print(end="*")
        j-=1
    print()
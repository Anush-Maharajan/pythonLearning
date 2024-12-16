def add(x, y):
    return x + y

a, b = map(int, (input("Enter two number: ").split()))

res = add(a, b)
print(res)
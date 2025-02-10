def equi(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

def equiRev(n):
    for i in range(n):
        spaces = " " * (2 * i + 1)
        stars = "*" * (n - i - 1)
        print(spaces + stars)
        
equi(5)
for i in range(5):
    spaces = " " * (2 * i - 1)
    stars = "*" * (5 - i - 1)
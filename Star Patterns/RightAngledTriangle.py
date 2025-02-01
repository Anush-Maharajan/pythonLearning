def rightAngledTriangle(n):
    i = 1
    while i <= n:
        print("*" * i)
        i+=1

def rightAngledtriangleRev(n):
    i = 1
    while i<= n:
        print("*" * (n - i + 1))
        i+=1
    
def rATflipped(n):
    i = 1
    while i <= n:
        print(" " * (n - i) , "*" * i)
        i+=1

def rATflippedRev(n):
    i = 1
    while i <= n:
        print(" " * (i - 1) , "*" * (n - i + 1))
        i+=1

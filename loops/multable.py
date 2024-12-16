"""
    Multiplication Tables up to 10 
        i. Use a loop to iterate through numbers 1 to 10 (for loop)
        ii. For each number, use another loop to calculate its multiples from 1 to 10 (inner loop).
        iii. Print each result in the format: a x b = c
"""
for i in range(1, 10+1): 
    print("\n\nMultiplication table of ", i)
    print("-"*40)
    for j in range(1, 10+1): 
        print(i,'x',j,'=', i*j)
        
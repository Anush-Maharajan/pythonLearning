# 1. Countdown from the number entered by the user to zero
num = int(input("Enter a number: "))
if num >= 0:
    while num >= 0:
        print(num)
        num -= 1
else:
    print("Please enter a non-negative number.")

# 2. Check if the number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3. Find the largest number among three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print(f"The largest number is: {largest}")

# 4. Check if the year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 5. Print odd numbers up to a specified limit
limit = int(input("Enter a limit: "))
print("Odd numbers:", end=' ')
for num in range(1, limit + 1):
    if num % 2 != 0:
        print(num, end=' ')
print()  # for a new line

# 6. Guess if the number is in a specified range
number = int(input("Enter a number: "))
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))
if range_start <= number <= range_end:
    print(f"The number {number} is in the range ({range_start}, {range_end}).")
else:
    print(f"The number {number} is not in the range ({range_start}, {range_end}).")














# 1. Accept a number from the user and display it
number = input("Enter a number: ")
print("You entered:", number)

# 2. Accept 2 numbers from the user and display their addition
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
print("The addition is:", addition)

# 3. Accept 2 input values and perform arithmetic operations
print("Arithmetic operations on", num1, "and", num2)
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
if num2 != 0:
    result_div = num1 / num2
else:
    result_div = "Division by zero is not allowed."
result_mod = num1 % num2

print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)
print("Modulus:", result_mod)

# 4. Accept 2 numbers from the user and print their swapping
num1 = input("Enter first number to swap: ")
num2 = input("Enter second number to swap: ")
print("Before swapping: num1 =", num1, ", num2 =", num2)
num1, num2 = num2, num1  # Swapping
print("After swapping: num1 =", num1, ", num2 =", num2)

# 5. Accept 5 subject marks from a student and calculate total and percentage
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total = sum(marks)
percentage = total / 5
print("Total marks:", total)
print("Percentage (average):", percentage)

# 6. Accept Basic salary and calculate total salary of an employee
basic = float(input("Enter Basic salary: "))
grade_pay = 2 * basic
da = 0.7 * basic
ta = 200
hra = 0.2 * basic
salary = grade_pay + da + ta + hra
print("Total Salary of the employee:", salary)

# strings = []
# print("HELL 2 U")
# for _ in range(int(input())):
#     string = input()
#     strings.append(string)

# for string in strings:
#     if string[4] == "o" or string[4] == "O":
#         print(string)

# Initialize an empty list to store the input strings
strings = []

# Print a greeting
print("HELL 2 U")

# Read the number of strings to be entered
num_of_strings = int(input("Enter the number of strings: "))

# Loop to read multiple strings
for _ in range(num_of_strings):
    string = input("Enter a string: ")
    strings.append(string)

# Check each string for the specific condition and print if it matches
for string in strings:
    if len(string) >= 4 and (string[3] == "o" or string[3] == "O"):
        print(string)

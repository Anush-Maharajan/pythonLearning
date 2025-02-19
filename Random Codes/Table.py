from tabulate import tabulate

# Data for the table
data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Doctor"],
    ["Charlie", 22, "Artist"]
]

# Column headers
headers = ["Name", "Age", "Profession"]

# Create and display the table
print(tabulate(data, headers=headers, tablefmt="grid"))

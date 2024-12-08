from collections import Counter
import random as r
from random import randint

this_list = list()
# Sample list (iterable)
for _ in range(100):
    x = r.randint(0, 9)
    this_list.append(x)

# Create a Counter object
item_counts = Counter(this_list)

s = set(this_list)

# Print the count of each unique item
for item in s:
    print(f"Item {item} occurs {item_counts[item]} times.")

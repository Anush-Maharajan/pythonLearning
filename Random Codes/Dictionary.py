"""
    This is a program for learning the various methods and functions of dictionary!    
"""

std = {
    "name": "Anush Maharjan",
    "age": 18,
    "clz": "Techspire",
    "edu": "BSc.IT"
}

print(f"\nThe default values of ditionary std: \n{std}")

std.update({"DOB": "2006"})
print(f"\nstd dictionary after updating value by adding DOB \n{std}")

remove_key = std.pop("age")
print(f"\nRemoving the age key using pop\n{std}")

l1 = ["abc", "def", "xyz"]
l2 = ["cba", "fed", "zyx"]
print(f"Making two lists:\n{l1}\n{l2}\n")

dictionary = dict.fromkeys(l1, l2) #All the l1 elements will have the elements of l2 
print(f"\nUsing the above list to make a dictionary:\n{dictionary}")

# Adding the keys and values using index

dictionary["abc"] = "cba" # update
dictionary["ghi"] = "ihg" # add

print(f"\n Adding the keys and values in dictionary using index:\n{dictionary}")
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
print(f"\nRemoving the age key using pop\n {std}")

l1 = ["abc", "def", "xyz"]
l2 = ["cba", "fed", "zyx"]


dictionary = dict.setdefault(l1)

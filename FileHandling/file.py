# name, age, jobtitle, *xtra = input("Name, age, jobtitle: ").split() 


# with open("csvfile.txt", "a") as file:
#     file.write(f"{name},{age},{jobtitle}\n")

with open("csvfile.txt", "r") as file:
    print(file.read())
    print("\n\n")
    file.seek(0)
    print(file.readlines())

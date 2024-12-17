import random

print("This program is used to create random roll number to form a group!!\n\n")

groupSize = int(input("Enter the number of Student tomake in a group: "))
studentSize = int(input("Enter number of students participating: "))

seen = {}

for _ in range(groupSize/studentSize + 1):
    studentNumber = random.randint(1,groupSize + 1)
    if studentNumber != seen:
        seen.update(studentNumber)

    elif studentNumber == seen:
        pass

    else:
        print("Error: Inception")
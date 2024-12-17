import random

def create_groups(students, group_size):
    # Shuffle the students list to ensure random groups
    random.shuffle(students)
    
    # Create groups
    groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
    
    return groups

def main():
    # Input the number of students and group size
    num_students = int(input("Enter the number of students: "))
    group_size = int(input("Enter the group size: "))
    
    # Create a list of students (for simplicity, we use numbers as student identifiers)
    students = [f"Student {i+1}" for i in range(num_students)]
    
    # Generate groups
    groups = create_groups(students, group_size)
    
    # Print the generated groups
    for i, group in enumerate(groups, 1):
        print(f"Group {i}: {', '.join(group)}")

if __name__ == "__main__":
    main()

import RightAngledTriangle as RAT

while True:

        print("Which shape of triangle do you want?")
        print("1. Equilateral")
        print("2. Right Angled")
        print("3. Isosceles")

        triangleShape = input()
        match triangleShape:
                case "1":
                        size = int(input("Enter the height of the triange: ", end = ""))
                        

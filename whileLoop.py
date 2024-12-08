#Do while loop
while True:
    st = input("Enter Here: ")
    if st == "stop":
        break
    if st == "no":
        continue
    if st == "hi":
        pass
    print("Test", st)

#How was the experience
while True:
    choice = input("How was it: ")
    if choice == "good":
        print("Noice")
        break
    if choice == "bad":
        continue
    if choice == "meh":
        pass
    print("Not", choice)


#Age finding sys ...
while True:
    age = int(input("What is your age?\n"))
    if age <= 0:
        break
    if age < 60:
        print("You are a old man")
        pass
    if age < 16:
        print("You are a miner")
        continue
    if age > 60:
        print("you are sentinal")
        pass
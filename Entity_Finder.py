import random
import string

testSubjectCount = 5
subjectCount = 0 #Counts the No. of times the test subject have entered
anomalyCount = 0 #Counts the No. of anomaly occured
anomalyEscapeCount = 0 #Counts the No. of anomaly gone on shelter
killCount = 0 #Counts the No. of Human sent to collection Area
anomalyCollected = 0 #Counts the No. of anomaly sent to collection Area
dazeCount = 1 #Tells how much sane the interrogator is (higher value show more no. of anomaly)

testSubjectNames = ["Alver", "Scarlet", "Estella", "Villith", "Wiltio",
                    "Seth", "Shigo", "Avis", "Alvis", "Eiran",
                    "Sylus", "Nora", "Clare", "Alberu", "Nikolai",
                    "Brandon", "Elisa", "Annika","Lucas", "Nadia"]

testSubjectIDs = ['QW2834', 'ZX4501', 'UV9203', 'BC7654', 'ER1298', 
                 'MN4312', 'PL7645', 'XK9087', 'TE3409', 'LU5160', 
                 'JD2741', 'HR8392', 'YT0538', 'DF6209', 'OP3948', 
                 'NB5720', 'AK1703', 'SM4825', 'VG1930', 'WL3094']

testSubjectIDwName = list(zip(testSubjectNames, testSubjectIDs))

testSubjectReason = ["Oh, I  was out collecting samples.", "I was collecting the scraps.",
                     "I went outside to transport the samples.",
                     "I went out to collect resources.", "I was hunting the anomalies.",
                     "I went out to get milk!", "I was following my friend.",
                     "I wanted to sketch the landscapes", "I was looking for stranded survivors",
                     "The shelter has structural issues, overcrowding, and violence. It's no longer safe.",
                     "We're out of essential resources like food, water, and medical supplies.",
                     "I need medical treatment that's only available outside the shelter.",
                     "I need to find my family and friends to ensure their safety.",
                     "This confined space is affecting my mental health. I need a change.",
                     "We need more information about the outside situation to plan our next steps.",
                     "Someone needs to scout safe routes or places for potential relocation.",
                     "I want to help those in more dire situations outside the shelter.",
                     "Bravery is needed to confront and solve the root problems."]

def testSubjectInteraction():
    testSubjectDialogue = ["Can I go in?\n\n", "What are my reports, interrogator?\n\n", "Am I free to go in?\n\n",
                         "Can you hurry up?\n\n", "Hello, may I ask about my report?\n\n"]
    print(testSubjectDialogue[random.randint(0,4)])
    
def userDecision():
    print("""1)You are clear.\t\t2)What is  your name?\n3)Give me your ID!\t\t4)Show ID List
5)Ask why they went Out.\t6)Declare as anomaly!?!""")
    decision1 = int(input("===> "))
    return decision1

def IDfromName(IDwName,testSub):
    for ID in IDwName:
        if ID[0] == testSub:
            return ID[1]

def generate_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=4))
    return letters + numbers

print("""\"n\n\n\nYou are a Anomaly Detector and your job is to find abnormal
entity that enters the shelter. Some may be human and some may not....
Use the necessary data in the lab to find if the person is human or not.\"\n\n\n""")

input("Press enter to continue.....\n")

while subjectCount != testSubjectCount:
    testSubject = testSubjectNames[random.randint(0,19)]
    if random.randint(1,10) > dazeCount:
        testSubjectID = IDfromName(testSubjectIDwName,testSubject)
    else:
        testSubjectID = generate_id()
        anomalyCount+=1
    
    reasonToLeave = testSubjectReason[random.randint(0,17)]
    print("\n\nA new test subject enters the lab...\n")
    testSubjectInteraction()
    decision = userDecision()
    
    while decision != 1 and decision !=6:
        if decision == 2:
            print("\nHello, my name is " + testSubject + ".\n\n\n")
        elif decision == 3:
            print("Here is my ID.... The ID reads " + testSubjectID + "\n\n\n")
        elif decision == 4:
            print("The ID list is...\n")
            for _ in testSubjectIDwName:
                print(_)
            print("\n\n\n")
        elif decision == 5:
            print(reasonToLeave + "\n\n\n")
        else:
            print("Choose a proper option\n\n\n")
        decision = userDecision()
    
    if decision == 1:
        print("You have let " + testSubject + " inside the shelter...")
        if testSubjectID != IDfromName(testSubjectIDwName,testSubject):
            anomalyEscapeCount+=1
    elif decision == 6:
        print(testSubject + " was taken inside the collection area....")
        if testSubjectID == IDfromName(testSubjectIDwName,testSubject):
            killCount+=1
        else:
            anomalyCollected+=1
    input("Enter to continue....")
    subjectCount +=1
    
    
print("\n\n\n\n\nThe test is finished..... and the reports are.......")
print("Anomaly occured: " + str(anomalyCount) + "\nAnomaly collected: "
      + str(anomalyCollected) + "\nHuman(s) killed: "
      + str(killCount) + "\nAnomaly escaped: " + str(anomalyEscapeCount) +
      "\nTotal Test Subjects: " + str(testSubjectCount))
input()
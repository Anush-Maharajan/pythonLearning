import random
import string
from data import testSubjectIDs, testSubjectNames, testSubjectReason, testSubjectIDwName

# Global Vairables
testSubjectCount = 5
subjectCount = 0  # Counts the No. of times the test subject have entered
anomalyCount = 0  # Counts the No. of anomaly occured
anomalyEscapeCount = 0  # Counts the No. of anomaly gone on shelter
killCount = 0  # Counts the No. of Human sent to collection Area
anomalyCollected = 0  # Counts the No. of anomaly sent to collection Area
dazeCount = (
    1  # Tells how much sane the interrogator is (higher value show more no. of anomaly)
)


def subjectWithNoticeOFArrival():
    arrivalNotice = []
    for x in testSubjectNames:
        if random.randint(-1, 1) == 0:
            arrivalNotice.append(x)


def testSubjectInteraction():
    testSubjectDialogue = [
        "Can I go in?\n\n",
        "What are my reports, interrogator?\n\n",
        "Am I free to go in?\n\n",
        "Can you hurry up?\n\n",
        "Hello, may I ask about my report?\n\n",
    ]
    print(testSubjectDialogue[random.randint(0, 4)])


def userDecision():
    print(
        """1)You are clear.\t\t2)What is  your name?\n3)Give me your ID!\t\t4)Show ID List
    5)Ask why they went Out.\t6)Declare as anomaly!?!"""
    )
    decision1 = int(input("===> "))
    return decision1


def IDfromName(IDwName, testSub):
    for ID in IDwName:
        if ID[0] == testSub:
            return ID[1]


def generate_id():
    letters = "".join(random.choices(string.ascii_uppercase, k=2))
    numbers = "".join(random.choices(string.digits, k=4))
    return letters + numbers


def main(
    subjectCount,
    testSubjectCount,
):
    print(
        """\"n\n\n\nYou are a Anomaly Detector and your job is to find abnormal
    entity that enters the shelter. Some may be human and some may not....
    Use the necessary data in the lab to find if the person is human or not.\"\n\n\n"""
    )

    input("Press enter to continue.....\n")

    while subjectCount != testSubjectCount:
        testSubject = testSubjectNames[random.randint(0, 19)]
        if random.randint(1, 10) > dazeCount:
            testSubjectID = IDfromName(testSubjectIDwName, testSubject)
        else:
            testSubjectID = generate_id()
            anomalyCount += 1

        reasonToLeave = testSubjectReason[random.randint(0, 17)]
        print("\n\nA new test subject enters the lab...\n")
        testSubjectInteraction()
        decision = userDecision()

        while decision != 1 and decision != 6:
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
            if testSubjectID != IDfromName(testSubjectIDwName, testSubject):
                anomalyEscapeCount += 1
        elif decision == 6:
            print(testSubject + " was taken inside the collection area....")
            if testSubjectID == IDfromName(testSubjectIDwName, testSubject):
                killCount += 1
            else:
                anomalyCollected += 1
        input("Enter to continue....")
        subjectCount += 1

    print("\n\n\n\n\nThe test is finished..... and the reports are.......")
    print(
        "Anomaly occured: "
        + str(anomalyCount)
        + "\nAnomaly collected: "
        + str(anomalyCollected)
        + "\nHuman(s) killed: "
        + str(killCount)
        + "\nAnomaly escaped: "
        + str(anomalyEscapeCount)
        + "\nTotal Test Subjects: "
        + str(testSubjectCount)
    )
    input()


if __name__ == "__main__":

    main()

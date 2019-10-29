
def lettersToNumbers(listName):
    i = 0
    number = 0
    length = len(listName)
    while (i < length):
        letter = listName[i]
        if (listName == normalGrades):
            number = convertToGP(letter, number)
        elif (listName == apGrades):
            number = convertToGP(letter, number) + 1
        listName[i] = number
        i = i + 1
    print(listName)

def convertToGP(letter, number):
    if letter == "A":
        number = 4
    elif letter == "A-":
        number = 3.67
    elif letter == "B+":
        number = 3.33
    elif letter == "B":
        number = 3.00
    elif letter == "B-":
        number = 2.67
    return number

normalGrades = []
apGrades = []

print("Input the grades of all of your 4.0 scale classes")
gradeValue = "A"
while (gradeValue != ""):
    gradeValue = raw_input()
    if (gradeValue != ""):
        normalGrades.append(gradeValue)
print(normalGrades)

print("Input the grades of all of your 5.0 scale classes")
gradeValue = "A"
while (gradeValue != ""):
    gradeValue = raw_input("")
    if (gradeValue != ""):
        apGrades.append(gradeValue)
print(apGrades)

lettersToNumbers(normalGrades)
lettersToNumbers(apGrades)

unweightedApGrades = [x - 1 for x in apGrades] #subtracts one from all grade
.py
unweightedGrades = normalGrades + unweightedApGrades
weightedGrades = normalGrades + apGrades

unweightedGPA = 0
count = 0
length = len(unweightedGrades)
while(count<length):
    unweightedGPA = unweightedGPA + unweightedGrades[count]
    count = count + 1

weightedGPA = 0
count = 0
length = len(weightedGrades)
while(count<length):
    weightedGPA = weightedGPA + weightedGrades[count]
    count = count + 1

unweightedGPA = unweightedGPA / len(unweightedGrades)
weightedGPA = weightedGPA / len(weightedGrades)

print("Unweighted GPA is: ")
print(unweightedGPA)
print("Weighted GPA is: ")
print(weightedGPA)

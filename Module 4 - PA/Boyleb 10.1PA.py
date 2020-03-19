#Program Name: PA 4 10.1
#Student: Brendan Boyle
#My submission of this program indicates that I have neither received nor given unauthorized assistance in writing this program

#enter values for scores
value0, value1, value2, value3, = input("Enter 4 scores ").split()
print("Scores are: ", value0, end = " ")
print(value1, end = " ")
print(value2, end = " ")
print(value3)

#find best score and grade values
best = max(value0, value1, value2, value3)
best = int(best)
aGrade = (best - 10)
bGrade = (best - 20)
cGrade = (best - 30)
dGrade = (best - 40)

#data for value0
value0 = int(value0)
if value0 >= aGrade:
    grade0 = "A"
elif value0 >= bGrade:
    grade0 = "B"
elif value0 >= cGrade:
    grade0 = "C"
elif value0 >= dGrade:
    grade0 = "D"
else:
    grade0 = "F"
print("Student 0 score is", value0, "and grade is", grade0)

#data for value1
value1 = int(value1)
if int(value1) >= aGrade:
    grade1 = "A"
elif value1 >= bGrade:
    grade1 = "B"
elif value1 >= cGrade:
    grade1 = "C"
elif value1 >= dGrade:
    grade1 = "D"
else:
    grade1 = "F"
print("Student 1 score is", value1, "and grade is", grade1)

#data for value2
value2 = int(value2)
if value2 >= aGrade:
    grade2 = "A"
elif value2 >= bGrade:
    grade2 = "B"
elif value2 >= cGrade:
    grade2 = "C"
elif value2 >= dGrade:
    grade2 = "D"
else:
    grade2 = "F"
print("Student 2 score is", value2, "and grade is", grade2)

#data for value3
value3 = int(value3)
if value3 >= aGrade:
    grade3 = "A"
elif value3 >= bGrade:
    grade3 = "B"
elif value3 >= cGrade:
    grade3 = "C"
elif value3 >= dGrade:
    grade3 = "D"
else:
    grade3 = "F"
print("Student 3 score is", value3, "and grade is", grade3)


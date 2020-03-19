#Program Name: PA 4 5.19
#Student: Brendan Boyle
#My submission of this program indicates that I have neither received nor given unauthorized assistance in writing this program

#enter input for lines
lines = input("Enter number of lines: ")
lines = int(lines)
while lines < 1 or lines > 15:
    print("Enter a value between 1 and 15.")
    lines = input("Enter number of lines: ")
    lines = int(lines)

#make pyramid with range statements
lines = lines + 2

for i in range(1, lines):
    for j in range(lines - i):
        print(end = "  ")
    for j in range(i-1, 1, -1):
        print(j, end = " ")
    for j in range(1, i):
        print(j, end = " ")
    print("\n")
    



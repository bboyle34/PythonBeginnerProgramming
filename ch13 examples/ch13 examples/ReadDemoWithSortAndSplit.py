
# Open file for input
infile = open("Presidents.txt", "r")
# read lines into a list
presList = infile.readlines()
print("Before sort:", presList)
# sort the list
presList.sort()
print("After sort:", presList)

# split first and last names into
# separate lists
fnList = []
lnList = []
for pres in presList:
    fnList.append(pres.split()[0])
    lnList.append(pres.split()[1])
print("First names",fnList)
print("Last names",lnList)
    



# we expect a file with numbers separated by commas
# and we want to sum all the numbers
fname = input("Enter a file name: ")
tot = 0
try:     # trying to read file, and sum values
   file = open(fname)
   lines = file.readlines()
   for i in range(len(lines)):
      nbrList = lines[i].split()
      print(nbrList)
      print ("x")
      for val in nbrList:
         tot += int(val)
   print("Total:", tot)
   print (nbrList)
         
except IOError:   # if you can't read the file, this exception occurs
    print("No such file")
except:           # here we deal with any other exception
    print("Bad data in file")




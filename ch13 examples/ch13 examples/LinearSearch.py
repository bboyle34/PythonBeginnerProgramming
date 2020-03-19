# The function for finding a key in the list(from chapter 10)
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

      
# make a couple lists
list1 = [4, 7, 9, 10, 23, 10, 50, 3, 7]
list2 = ['a', 'x', 'z', 'p', 'v', 'i', 'm']

# do some searches and print results
i = linearSearch(list1, 23)
print ("The number 23 is found in list1 position", i)

j = linearSearch(list1, 10)
print ("The number 10 is found in list1 position", j)
# the linear search returns the position of the first occurrence
# of the searched-for value

k = linearSearch(list2, 'v')
print(print ("The string 'v' is found in list2 position", k)

l = linearSearch(list2, 'o')
print("The string 'o' is found in list2 position", k)
# if linearSearch returns -1, this means the value was not found

      


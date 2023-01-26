#the purpose of this is to build an array that will log all the pairs of itself.
#Log Array

from itertools import combinations

# list to get pairs from
list1 = [1,2,3,4,5,6,7,8,9]

# prints to the console the origional list
print("The original list : " + str(list1))

# All possible pairs in List1
# Calls the combination feature
output = list(combinations(list1, 2))

# printing result
print("All possible pairs are " + str(output))
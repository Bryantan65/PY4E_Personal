f = open("regex_sum_1482698.txt")
import re #import regex
total = 0
totalvals = list()

for line in f:
    x= re.findall('[0-9]+' , line) #find all numbers
    if x: #if found
       totalvals.extend(x) #extend the list, append does not work because it will make lists within lists

print(sum(map(int, totalvals))) #map is like a for loop that does int for each value in the list, if you just do int(totalvals), it won't work, since totalvals is a list
print(len(totalvals))
        
      


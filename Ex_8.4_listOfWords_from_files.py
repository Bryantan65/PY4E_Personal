#fname = input("Enter file name: ")
fh = open("romeo.txt").read()
#.read reads the thing line by line
lst = list()

#for each word inside  of this text file
for line in fh.split():
    #it will add that word into the list if the word is not in list
    if line not in lst:
        lst.append(line)
   
#sort is a method, it wil sort the list but will return nothing by itself
lst.sort()
print(lst)

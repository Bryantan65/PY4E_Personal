count = dict()

file = open("romeo.txt")

#for each element (in text file it is a line), so u will have line by line STRINGS!!
for lines in file:
   
    #for each element in the STRINGS , print out the element aka each LETTER in the strings
    #unless you add a .split() , which splits them based on spaces and converts the strings to lists
    for word in lines.split():

        #add an item in the count dictionary, which the key "word" and value of the word, if the word exists, return the value +1 which is  + 1, if no, default to 0

        #looks inside count for the value of word
        #if word exists, take the value of word and add 1 to it
        #if word does not exist, assign count[word] with the value of 1 (0+1)
        count[word] = count.get(word,0) + 1 
    
print(count)
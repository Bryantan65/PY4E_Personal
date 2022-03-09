fileName = input("Input file name")
f = open(fileName)


#decalring a list to add the emails into
emails = list()

#for each line in the text document
for line in f:
    
    if line.startswith('From') and not line.startswith('From:') : #the emails are in 2 lines, 'From' and 'From:' which led to duplicates, this prevents them
        print(line.strip().split()[1])  #strip the end spaces at end of each line, split the spaces and take out the 1st index aka the email name, and print it out
        emails.append(line.split()[1])  #split the words in the from line and add into the email list
        #positioning of the [1] must be AFTER the split command, if not, split will just split the word 'From'
         

print("There were" , len(emails) , "lines in the file with From as the first word")

f.close()
#always do file close after opening the file


#OLD CODE================================================================================================================
#reading = f.read()
#spliting = reading.split()
#fromlines = reading.startswith('From')
#if fromlines:
#    print(reading)
#i believe this code doesn't work cuz it's reading word by word, then the moment it detects a from, it just print the whole f.read statement
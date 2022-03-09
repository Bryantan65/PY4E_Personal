filename = input("Enter file name") #asking for input of file name
totalamt = 0

try:
    fopen = open(filename) #tosses an error if the file can't be opened
except:
    print("Your file", filename, "could not be opened")
    quit()

for linez in fopen: #for each line in the file
    if "X-DSPAM-Confidence:" in linez: #if this string is found
        digitpos = linez.find(":") #find which position number : is at
        digitline = linez[digitpos+1:] #take the characters starting from the 1st digit AFTER the :, until the end of the string
        digit = float(digitline.strip()) #remove whitespace and convert that string number into a float
        lines = len(linez) #get the total number of lines
        totalamt = totalamt + digit #get the total value of all lines

print("Average spam confidence:" , totalamt / lines)
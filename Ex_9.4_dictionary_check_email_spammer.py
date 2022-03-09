from itertools import count


f = open("mbox-short.txt")
emaildic = dict()
bigNum = 0
bigEmail = None


#open the text file and read each line starting with 'From'
for lines in f:
    if lines.startswith('From '):
        #take the 2nd WORD from each line and save as variable email
        #split each line by spacing to seperate out the words, if not, [1] will specify the 'r' in 'From'
        email = lines.split()[1]
        #assign the value of emaildic[] to either email:0+1 or email:x+1
        emaildic[email] = emaildic.get(email , 0) + 1

#for each value in the dic, if the new value is bigger than none, it becomes the new big value
        for emails , emailNum in emaildic.items():
            if emailNum > bigNum:
                bigNum = emailNum
                bigEmail = emails
                
                
            
            
if bigNum > 0:        
    print(bigEmail, bigNum)
else:
    print(bigNum , "emails found")



    



        


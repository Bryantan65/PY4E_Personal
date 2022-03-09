f = open("mbox-short.txt")

emaildic = dict()

for lines in f:
    if lines.startswith('From '):
         email = lines.split()[5] #splits the LINE and takes the 5th element, aka the hours:mins:sec
         hours = email.split(":")[0] #splits the hours[0] ":" mins[1] ":" sec[2], takes the first element which is hours
         
         
         emaildic[hours] = emaildic.get(hours , 0) + 1  #get the total number of time each hour has appeared
        

#this is the only code where i referred to the video for SHEEEEEEEEEESH
for k , v in sorted(emaildic.items()): #sorts the result
    print(k,v)

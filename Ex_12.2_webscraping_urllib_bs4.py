#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#initialize reading of the website
url = "http://py4e-data.dr-chuck.net/comments_1482700.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

 
# Retrieve all of the span tags
tags = soup('span')

#initialize variable to track sum of numbers
sum = 0

#for each line in the span tags
for tag in tags:
    # print(str(tag.split())) #nonetype error because you are trying to split a bs4 element BEFORE it gets converted into a string
    # print(str(tag).split()) #works

    #for each character in each line
    for character in tag:
        if character.isdigit():
            #if the character is a digit , add it to the sum, however since it is still a string, it must be converted to int
             sum += int(character)
            

print(sum)


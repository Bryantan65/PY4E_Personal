from bs4 import BeautifulSoup #you are only importing beautifulsoup module only
import urllib.request, urllib.parse, urllib.error
import ssl #you are importing the entire libray

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/known_by_Ciara.html"

position = 18


for x in range(7): #loop that repeats 7 times:
    links = list()  #list created so that you can get the 18th link , declared here so the loop will be fresh every loop
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href' , None)) #add all the href in the links list
    url = links[position-1] #url takes the 18th link as the new varible and runs the next iteration of the loop
    

print(url)


    




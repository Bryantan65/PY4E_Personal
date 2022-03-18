import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

while True:
    # file = input('Enter url: ')
    
    url = "http://py4e-data.dr-chuck.net/comments_1482702.xml" #website to be parsed , change this to an input when done
    xml = urllib.request.urlopen(url, context=ctx).read() #parsing the website and getting the sauce

    #print(xml.decode())

    tree = ET.fromstring(xml.decode())

    num = tree.findall('.//count')

     #u must convert to string else your results is just pure elemnts
    for eachitem in num: #this list must be created to seperate each item if not there will be an error? because ET.tostring doesn't like to convert a list
        extractednum = eachitem.text #FINALLY
        total+= int(extractednum)
        #print(ET.tostring(eachitem)) #EXPLAIN WHY THIS DOESN'T WORK
    
    print(total)
    break
    
        


    

f = open("mbox-short.txt")
import re

emaildic = dict()

for lines in f:
    lines = lines.rstrip()
    if re.search('^ From: ' , lines):
        print(lines)
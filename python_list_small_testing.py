numlist = list()

while True:
    inp = input('Enter a number')
    if inp == 'done':
        break
    numlist.append(float(inp))
    
average = sum(numlist) / len(numlist)

print(average)
largest = None
smallest = None
while True:
    num = input("Please enter a number")
    if num == "done":
        break
    try:
        num = int(num)
        if smallest == None:
            smallest = num
        if largest == None:
            largest = num
        if num > largest:
            largest = num 
        elif num < smallest:
            smallest = num
    except:
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)
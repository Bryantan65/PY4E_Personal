
def computepay(h, r):
    if h > 40:
        return (40 * r) + ((h - 40) * (r * 1.5))
    elif h < 40:
        return h * r
    else:
        return "Error"

    

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate"))
#testest hrs
p = computepay(hrs, rate)
print("Pay", p)
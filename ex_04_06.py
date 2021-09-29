def computepay(hour, rate):
    fhour = float(hour)
    frate = float(rate)
    pay1 = fhour * frate
    pay2 = 40 * frate + (fhour - 40) * frate * 1.5
    if fhour <= 40:
        return pay1
    else:
        return pay2

hour = input("Please enter hours:")
rate = input("Please enter rate:")
p = computepay(hour,rate)
print("Pay",p)

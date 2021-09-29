Hours = float(input("Please enter hours:"))
Rate = float(input("please enter rate:"))

if Hours <= 40:
    pay = Hours * Rate
else:
    pay = 40 * Rate + (Hours - 40) * Rate * 1.5

print(pay)

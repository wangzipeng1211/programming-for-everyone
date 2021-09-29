largestnum = None
smallestnum = None

while True:
    s = input('Enter a number: ')
    if s == "done":
        break
    try:
        f = int(s)
    except:
        print('Invalid input')
        continue

    if largestnum is None:
        largestnum = f
    elif f > largestnum:
        largestnum = f

    if smallestnum is None:
        smallestnum = f
    elif f < smallestnum:
        smallestnum = f

print('Maximum is',largestnum)
print('Minimum is',smallestnum)

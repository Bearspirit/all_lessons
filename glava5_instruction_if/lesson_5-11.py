digit = [x for x in range(1,10)]
print(digit)
for i in digit:
    if i == 1:
        print(str(i) +"st")
    elif i == 2:
        print(str(i) + "nd")
    elif i == 3:
        print(str(i) +"rd")
    else:
        print(str(i) + "th")
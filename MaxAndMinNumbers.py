# Write another program that prompts for a list of numbers as above and
# at the end prints out both the maximum and minimum of the numbers instead of the average.

tot = 0
num = 0
highestInt = float('-inf')
lowestInt = float('inf')

while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    tot += fval
    num += 1

    if fval > highestInt:
        highestInt = fval
    if fval < lowestInt:
        lowestInt = fval

if num > 0:
    print('Highest Integer inputted: ', highestInt)
    print('Lowest integer inputted: ', lowestInt)
else:
    print('No integers were entered. No maximum or minimum to display!')
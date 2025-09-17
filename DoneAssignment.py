# Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count,
# and average of the integers. If the user enters anything other than an integer,
# detect their mistake using try and except and print an error message and skip to the next integers.

tot = 0
num = 0

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

if num > 0:
    print('Total: ', tot)
    print('Count: ', num)
    print('Average: ', tot/num)
else:
    print('No integers were entered. No total, count, or average to display!')
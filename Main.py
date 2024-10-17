# Calculator App -- GUI

# addition = a + b:
# subtraction = a - b:
# multiplication = a * b:
# division = a / b:

def add(a,b):
    newNum = a + b
    if newNum % 1 == 0:
        newNum = int(newNum)
    else: newNum = float(newNum)

    return(newNum)

def subtract(a,b):
    newNum = a - b
    if newNum % 1 == 0:
        newNum = int(newNum)
    else: newNum = float(newNum)

    return(newNum)


def multiply(a,b):
    newNum = a * b
    if newNum % 1 == 0:
        newNum = int(newNum)
    else: newNum = float(newNum)

    return(newNum)


def divide(a,b):
    newNum = a / b
    if newNum % 1 == 0:
        newNum = int(newNum)
    else: newNum = float(newNum)

    return(newNum)

def addNum (num,num2):
    if num % 1 == 0:
        num = int(num)
    else: num = float(num)
    if num2 % 1 == 0:
        num2 = int(num2)
    else: num2 = float(num2)

    print((num), '+', (num2), '=', add(num,num2))

def subNum (num,num2):
    if num % 1 == 0:
        num = int(num)
    else: num = float(num)
    if num2 % 1 == 0:
        num2 = int(num2)
    else: num2 = float(num2)

    print((num), '-', (num2), '=', subtract(num,num2))

def mulNum (num,num2):
    if num % 1 == 0:
        num = int(num)
    else: num = float(num)
    if num2 % 1 == 0:
        num2 = int(num2)
    else: num2 = float(num2)

    print((num), '*', (num2), '=', multiply(num,num2))

def divNum (num,num2):
    if num % 1 == 0:
        num = int(num)
    else: num = float(num)
    if num2 % 1 == 0:
        num2 = int(num2)
    else: num2 = float(num2)

    print((num), '/', (num2), '=', divide(num,num2))

while True:
    print ('Choose a mathematical operation:')
    print ('1. Addition')
    print ('2. Subtraction')
    print ('3. Multiplication')
    print ('4. Division')
    print ('5. Exit')

    Operation = input('Select option 1-5 \n')

    if Operation in ('1','2','3','4','5'):
        if Operation == '5':
            break
        try:
            num = float(input('Enter first number for the equation \n'))
            num2 = float(input('Enter second number for the equation \n'))
        except ValueError:
            print ('Please enter a whole or decimal number to proceed with the operation')
            continue

        if Operation == '1':
            addNum(num,num2)
        elif Operation == '2':
            subNum(num,num2)
        elif Operation == '3':
            mulNum(num,num2)
        elif Operation == '4':
            divNum(num,num2)
    else:
        print('Invalid Input.')

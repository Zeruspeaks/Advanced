#==****======*****===========******=============
#             ADVANCED PROGRAMMING ASSIGNMENT 1
# Name: Zerubabel Jember
# ID: ETS0184/10
# SECTION:B
# SUBMITTED TO:Mr.EYOB
# SUBMISSION DATE:MAY 6,2022
##==****======*****===========******=============
from __future__ import division 
from math import e
import math
from math import sqrt
from re import sub
from select import select
import string
from tkinter import N
#  1
def cube():
    number = (
        input('insert the number to find its cube'))
    num = int(number)
    cubic_value = num * num * num
    print(cubic_value)


# 2
def triangle():
    width = input('insert the value of the base of the triangle:')
    w = float(width)
    height = input('insert the value of the height of the triangle:')
    h = float(height)
    area = 0.50 * h * w
    print(area)


# ***************************
# 3(RECTANGLE AREA)
# ***************************


def rectangle():
    w = float(input('insert the value of the base of the recangle:'))

    h = float(input('insert the value of the height of the recangle:'))

    area = h * w
    print('the area of the rectangle= ' + str(area))


# *****************
#  4(LINE)
# ******************


def Line():
    m = float(input('insert the slope of the line:'))
    b = float(input('insert the x-intercept of the line:'))
    x = float(
        input('insert the value of x-coordinate for its respectative y:'))
    y = m * x + b
    print('the respectative y value is ' + str(y))


# *******************************
#  5(LINE INTERSECTION)
# ********************************
def Intersect():
    m1 = float(input('insert the m1 coefficient of line 1:'))
    b1 = float(input('insert the b1 coefficient of line 1:'))
    m2 = float(input('insert the m2 coefficient of line 2:'))
    b2 = float(input('insert the b2 coefficient of line 2:'))
    # if they intersect they will have at least one same(x,y) value
    # y=m1x+b1 and y=m2x+b2
    # m1x+b1=m2x+b2
    # finally if the intersect they will intersect at x=(b2-b1)/(m1-m2)
    x = (b2 - b1) / (m1 - m2)
    y1 = m1 * x + b1
    y2 = m2 * x + b2
    print('they will intersect at x=  ' + str(x) + "y= " + str(y1))
    if (y1 == y2):
        print('1')
    else:
        print('0')

#6********************************************************
def factorial():
    n=int(input("Please enter Positive integer: "))
    if (n>0):
        fact=1
        i=0
        for i in range(n):
            fact = fact * (n-i)
        print("The factorial of",n,"is = ",fact)
    else :
        print("Your enter value is incorrect!")
        factorial()
#7***************************************
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    for i in range(n):
        print(fibonacci(i))   

# ***********************************************
# QUESTION 8(PRIME CHECK AND SUM OF THAT DIGIT)
# ***********************************************
def prime_sum():
    num3 = int(input('insert the number for prime check:'))

    if num3 < 1:
        print('its not a prime number')
    else:
        for i in range(2, num3):
            if (num3 % i == 0):
                print('its not a prime number')
                break
            else:
                print('its a prime number')
                break
    sum = 0
    while num3 > 0:
        digit = num3 % 10
        sum = sum + digit
        num3 = num3 // 10
    print("the sum of the digits===> ", sum)


# *****************************
# QUESTION 9(ASCENDING ORDER]
# ****************************


def ascend():
    arr = []
    x = int(input('Enter the amount of numbers to insert:'))
    for k in range(x):
        num = int(input('Enter the numbers to be sorted:'))
        arr.append(num)

    temp = 0
    print("Elements of original array: ")
    for i in range(x):
        print(arr[i], end=" ")

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print("Elements of array sorted in ascending order: ")
    for i in range(0, len(arr)):
        print(arr[i], end=" ")


# ******************************
# QUESTION 10(ASCENDING ORDER]
# ******************************


def G_mark():
    siz = int(input('Enter the amount of the students you need for calc:'))
    score = []
    counter = 0

    for i in range(siz):
        num = int(input("write the numbers one-by-one:"))
        score.append(num)

    for j in range(siz):
        if (score[j] > 20):
            counter = counter + 1

    print('Number of students that scored above 20 is ', counter)


# *******************************
# QUESTION 11(CELL OR LINE PHONE]
# ********************************


def cellphone():
    contact_number = int(input("enter the 9 digit contact number==>"))
    if (contact_number // 100000000 == 0 or contact_number // 100000000 > 9):
        print('Invalid Input')
    elif (contact_number // 100000000 == 9):
        print("mobile")
    else:
        print("fixed phone")


# ***********************************
# QUESTION 12(MAX MIN USER DEFIINED)
# ***********************************


def max_min():
    siz = int(input('Enter the amount of the number you need for calc:'))
    numlist = []

    for i in range(siz):
        num = int(input("write the numbers one-by-one:"))
        numlist.append(num)
    min = max = numlist[0]
    for i in range(siz):
        if (numlist[i] > max):
            max = numlist[i]
        if (numlist[i] < min):
            min = numlist[i]
    print('Maximum in the list==> ', max)
    print('Minimum in the list==> ', min)


# **************************
# QUESTION 13(REVERSE ORDER]
# ***************************


def reverse():
    num = int(input("enter the number that is goining to be reversed:"))
    rev = 0
    while (num > 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    print('reversed number is: ', rev)


# *****************
# QUESTION 14(GCD)
# *****************


def gcd():
    n1 = int(input('enter the first number : '))
    n2 = int(input('enter the second number :'))
    if n1 > n2:
        small = n2
    else:
        small = n1
    for i in range(1, small + 1):
        if ((n1 % i == 0) and (n2 % i == 0)):
            gcd = i

    print("the GCD of the two numbers==>", gcd)


# *****************
# QUESTION 15(LCM)
# ******************


def lcm():
    n1 = int(input('enter the first number : '))
    n2 = int(input('enter the second number :'))
    for i in range(1, n1 * n2 + 1):
        if ((i % n1 == 0) and (i % n2 == 0)):
            print("the LCM of the two numbers==>", i)
            break


# **********************
# QUESTION 16(FRAC SUM)
# ***********************


def frac_sum():
    sum = 0
    for i in range(1, 99, 2):
        x = i / (i + 2)
        sum = sum + x
        print(x)
    print("the sum of the fraction is ==> ", sum)


# *********************
# QUESTION 17(ISBN)
# *********************


def isbn():

    dig9 = int(input('ENTER A 9 DIGIT NUMBER ONLY: '))
    original_dig9 = dig9
    arr = []
    if ((dig9 // 100000000) > 9 or (dig9 // 10000000 == 0)):
        print("Invalid number please enter a 9 digit number")
    else:
        for i in range(9):
            digit = dig9 % 10
            dig9 = dig9 // 10
            arr.append(digit)
    checksum = 0
    for i in range(9):
        a = arr[i] * (9 - i)
        checksum = checksum + a
    checksum = checksum % 11
    display = ((original_dig9 * 10) + checksum) - (arr[8] * 1000000000)
    print("the ISBN of the entered number is ==>", arr[8], end="")
    print(display, end="")


# ********************
# QUESTION 18(EXP)
# *********************


def exp():
    x = int(input('enter the value of x for e^x =>'))
    sum = 0
    for i in range(15):
        a = x**i / math.factorial(i)
        sum = sum + a

    print(sum)


# **********************
# QUESTION 19(LEAP)
# **********************


def leap():
    year = 2001
    leap = []
    while year <= 2100:
        if year % 4 == 0:
            leap.append(year)
        year = year + 1

    for i in range(25):
        if i % 10 == 0:
            print(leap[i])
        else:
            print(leap[i], end=" ")


# ******************************
# QUESTION 20(MAX AND OCCURENCE)
# ********************************


def maxoccurence():
    x = int(input('enter the number of students: '))
    student = []
    for i in range(x):
        score = int(input('Enter the numbers to find max and its occurence :'))
        student.append(score)
    i = 0
    max = student[0]
    while i < x:
        if (student[i] > max):
            max = student[i]
        i = i + 1

    j = 0
    counter = 0
    while j < x:
        if (student[j] == max):
            counter = counter + 1
        j = j + 1

    print("The maximum of the numbers' is ", max)
    print("it occurs ", counter, " times")


# *********************************
# QUESTION 21(CUBE OF THREE WORDS)
# *********************************


def cube_of_digits():
    low = 100
    high = 1000
    for a in range(low, high):
        sum = 0
        test = a
        while test > 0:
            digit = test % 10
            test = test // 10
            cube = digit**3
            sum += cube
        if a == sum:
            print(a)


# **************************
# QUESTION 22(No of Digits)
# *************************


def No_of_digit():
    counter = 0
    num = 1
    while 1 == 1:
        num = int(
            input(
                'Enter a positive integer(negative number terminates) to find its number of digits'
            ))
        if (num < 0):
            print("loop terminated negative number entered")
            break
        else:
            counter = 0
            while (num > 0):
                digit = num % 10
                num = num // 10
                counter = counter + 1
            print(counter)


# ***************************
# QUESTION 23(No of Primes)
# **************************


def No_of_prime():
    counter = 0
    n = int(
        input("enter the maximum restriction to the prime number searching "))
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            counter += 1

    print("the number of prime numbers= ", counter)


# *****************************
# QUESTION 24(PERFECT NUMBER)
# ****************************


def perfect_number():
    sum = 0
    n = int(input("enter the numbet that you want to check perfection: "))
    arr = []
    for x in range(1, n):
        if n % x == 0:
            sum += x
            arr.append(x)
    if sum == n:
        print("its a perfect number ")
        print("its divisors", arr)
    else:
        print("its not a perfect number")


# *******************************
# QUESTION 25(TOTAL COMPUTATION)
# *******************************


def t_comp():
    counterpos = 0
    counterneg = 0
    sum = 0
    average = 0
    while 1 == 1:
        num = int(
            input("Enter an int value,program exits if the input is zero "))
        if (num > 0):
            counterpos += 1
            sum = sum + num
        elif (num < 0):
            counterneg += 1
            sum = sum + num
        else:
            break
    average = (sum) / (counterpos + counterneg)
    print("the number of positives is", counterpos)
    print("the number of negatives is", counterpos)
    print("the total is", sum)
    print("the average is", average)


# ************************
# QUESTION 26(TUITION)
# ************************


def tuition():
    initial_tuition = 10000.0
    sum = 0.0
    for i in range(1, 11):
        after_years = initial_tuition * 1.05
        initial_tuition = after_years
    print("after ten years tuition", initial_tuition)
    sum = initial_tuition
    for j in range(1, 5):
        initial_tuition = initial_tuition * 1.05
        sum = sum + initial_tuition
    print("four years tuition 10 years after ward==> ", sum)


# **************************
# QUESTION 27(CONVERSION)
# *************************


def conversion():
    print("1.kilograms to pounds")
    print("2.miles to kilometers")
    print("3.hour to minutes")
    N = int(input("Enter the conversion type:"))

    if (N == 1):
        kilo = float(input("Enter the kilogram amount:"))
        pound = 2.20462 * kilo
        print(kilo, "kilograms=", pound, "pounds")
    elif (N == 2):
        mile = float(input("Enter the amount of miles:"))
        kilometers = 1.60934 * mile
        print(mile, "miles=", kilometers, "kilometers")
    elif (N == 3):
        hours = float(input("Enter the amount of hours:"))
        minutes = 60 * hours
        print(hours, "hours=", minutes, "minutes")
    else:
        print("Invalid number entered")


# ***********************************************
# QUESTION 28(STUDENT NAME AND SCORE 1st and 2nd)
# ***********************************************

def student():
    size = int(input('Enter the number of students: '))
    student = []
    for i in range(size):
        name = input("Enter the name of students: ")
        score = int(input("Enter the score of the student: "))
        student.append(name)
        student.append(score)
    max1 = student[1]
    for j in range(1, 2 * size, 2):
        if (student[j] > max1):
            max1 = student[j]
            name = student[j - 1]
    max2 = 0
    for k in range(1, 2 * size, 2):
        if (student[k] != max1):
            if (student[k] > max2):
                max2 = student[k]
                name2 = student[k - 1]
    print("1st place The name of the student is ", name, " and it scores:",
          max1)
    print("2nd place The name of the student is ", name2, " and it scores:",
          max2)


# ****************************************
# QUESTION 29(STUDENT NAME AND SCORE 1st)
# ****************************************


def stu():
    size = int(input('Enter the number of students: '))
    student = []
    for i in range(size):
        name = input("Enter the name of students: ")
        score = int(input("Enter the score of the student: "))
        student.append(name)
        student.append(score)
    max = student[1]
    for j in range(1, 2 * size, 2):
        if (student[j] > max):
            max = student[j]
            name = student[j - 1]
    print("1st place The name of the student is ", name, " and it scores:",
          max)


# ***********************
# QUESTION 30(5 and 6)
# **********************


def fivesix():
    num = 100
    five_six = []
    while num <= 200:
        if ((num % 5 == 0) or (num % 6 == 0)):
            if (num % 30 != 0):
                five_six.append(num)
    num = num + 1

    for i in range(len(five_six)):
        if i % 10 == 0:
            print(five_six[i])
        else:
            print(five_six[i], end=" ")


# ***********************
# QUESTION 31(ASCII)
# ***********************


def ascii():
    i = 1
    while i < 127 - 32:
        result = chr(i + 32)

        if i % 10 == 0:
            print(result)
        else:
            print(result, end=' ')

        i = i + 1


# *****************************
# QUESTION 32A(right tringle)
# ****************************


def right_tri():
    rows = 6
    for i in range(1, rows + 1):
        for space in range(1, (rows - i)):
            print(" ", end="")
        for symbol in range(i, 0, -1):
            print("{0}".format(symbol), end="")

        print()


# ****************************************
# QUESTION 32B(UPSIDE DOWN right tringle)
# ***************************************


def upside():
    rows = 6
    for i in range(1, rows + 2):
        for space in range(1, i + 2):
            print(" ", end="")
        for symbol in range(1, rows - i + 2):
            print("{0}".format(symbol), end="")
        print()


# ********************************
# QUESTION 33(pyramid of 8numbers)
# *********************************


def right_en_left():
    num = int(input("Enter the amount of the row from 1-15:"))
    if (num < 1 or num > 15):
        print("Invalid Number please enter a number between 1 to 15")
    else:
        for i in range(1, num + 1):
            for j in range(1, num - i + 1):
                print(end=" ")
            for j in range(i, 0, -1):
                print(j, end="")
            for j in range(2, i + 1):
                print(j, end="")
            print()


# *********************************
# QUESTION 34(POWER OF 2 TRIANGLE)
# ********************************


def pow2pyramid():
    lines = []
    for i in range(1, 9):
        lines.append([str(2**j) for j in range(i)])

    b = len(lines[-1])
    buffers = [len(x) for x in lines[-1]]

    for line in lines:
        l = len(line)
        line = [" "] * (b - len(line)) + line
        out = []
        for x, y in zip(line, buffers):
            out.append(x.rjust(y))
        print(" ".join(out + out[::-1][1:]))


# **********************
# QUESTION 35(LOAN)
# **********************
import math


def Loan():
    loanAmount = int(input("Enter loan amount:"))
    numberOfYears = int(input("Enter number of years: "))
    annualInterestRate = 5000.0
    print("Interest Rate", "     ", "Monthly Payment", "      ",
          "Total Payment")
    while (annualInterestRate <= 8000.0):
        monthlyInterestRate = (annualInterestRate / 1000) / 1200
        monthlyPayment = (
            loanAmount * monthlyInterestRate /
            (1 - 1 / math.pow(1 + monthlyInterestRate, numberOfYears * 12)) *
            10)
        totalPayment = (monthlyPayment * numberOfYears * 12)
        print((annualInterestRate / 1000), "      ", monthlyPayment, "      ",
              totalPayment)
        annualInterestRate = annualInterestRate + 125.0


# ************************
# QUESTION 36(HEXA DECIMAL)
# **************************
def hexadec():
    num = int(input("enter the decimal numbet to convert it to hexa decimal:"))
    conversion_table = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hexadecimal = ''
    while (num > 0):
        remainder = num % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        num = num // 16

    print("The hexadecimal form of", num, "is", hexadecimal)


# *****************************
# QUESTION 37(EULER FACTORIAL)
# *****************************


def e():

    def factorial(n):
        for i in range(n):
            if n == 0 or n == 1:
                return 1
            else:
                n = n * n - 1

    sum = 0
    for i in range(15):
        a = 1 / math.factorial(i)
        sum = sum + a
    print("e=", sum)


# **********************
# QUESTION 38(PRIME)
# **********************


def prim():
    num3 = int(input('insert the number for prime check:'))

    if num3 < 1:
        print('its not a prime number')
    else:
        for i in range(2, num3):
            if (num3 % i == 0):
                print('its not a prime number')
                break
            else:
                print('its a prime number')
                break


# *****************************
# QUESTION 39(EULER FACTORIAL)
# *****************************


def even():
    num = int(input("Enter the number to check evenity:"))
    if num < 0:
        print(" The number is zero or negative")
    else:
        if (num % 2 == 0):
            print("its even")
        else:
            print('its not even, odd number')


# ************************
# QUESTION 40(CALCULATOR)
# ***********************


def calculator():

    def sum():
        print('Sum is ', num1 + num2)

    def product():
        print('Product is ', num1 * num2)

    def quoitient():
        if (num2 != 0):
            print('quoitient is ', num1 / num2)
        else:
            print('Division by zero not possible')

    def difference():
        print('Difference is ', num1 - num2)

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    print('1.Addition')
    print('2.Multiplication')
    print('3.Division')
    print('4.Subtraction')
    op = int(input('Select operation:'))

    if op <= 0 or op > 4:
        print('please enter a valid number')
    else:
        if (op == 1):
            sum()
        elif (op == 2):
            product()
        elif (op == 3):
            quoitient()
        else:
            difference()


# **********************
# QUESTION 41(FACT SUM)
# *********************8


def fact_sum():
    x = int(input('Enter the limit of the summation: '))
    pro = 1
    sum = 0
    for i in range(1, x + 1):
        pro = i * pro
        sum = sum + pro
    print(sum)
while 1:
    Qnumber = int(input("Enter Question Number 1-41 :"))
    if (Qnumber <= 0) or (Qnumber > 41):
        print('Invalid Number!please Enter a valid one')
    if (Qnumber == 1):
        cube()
    elif (Qnumber == 2):
        triangle()
    elif (Qnumber == 3):
        rectangle()
    elif (Qnumber == 4):
        Line()
    elif (Qnumber == 5):
        Intersect()
    elif (Qnumber == 6 ):
        factorial()
    elif (Qnumber == 7 ):
        fibonacci(6)   
    elif (Qnumber == 8):
        prime_sum()
    elif (Qnumber == 9):
        ascend()
    elif (Qnumber == 10):
        G_mark()
    elif (Qnumber == 11):
        cellphone()
    elif (Qnumber == 12):
        max_min()
    elif (Qnumber == 13):
        reverse()
    elif (Qnumber == 14):
        gcd()
    elif (Qnumber == 15):
        lcm()
    elif (Qnumber == 16):
        frac_sum()
    elif (Qnumber == 17):
        isbn()
    elif (Qnumber == 18):
        exp()
    elif (Qnumber == 19):
        leap()
    elif (Qnumber == 20):
        maxoccurence()
    elif (Qnumber == 21):
        cube_of_digits()
    elif (Qnumber == 22):
        No_of_digit()
    elif (Qnumber == 23):
        No_of_prime()
    elif (Qnumber == 24):
        perfect_number()
    elif (Qnumber == 25):
        t_comp()
    elif (Qnumber == 26):
        tuition()
    elif (Qnumber == 27):
        conversion()
    elif (Qnumber == 28):
        student()
    elif (Qnumber == 29):
        stu()
    elif (Qnumber == 30):
        fivesix()
    elif (Qnumber == 31):
        ascii()
    elif (Qnumber == 32):
        print('1=A')
        print('2=B')
        sub_question = int(input('Enter 1 or 2:'))
        if (sub_question == 1):
            right_tri()
        elif (sub_question == 2):
            upside()
        else:
            print('Invalid input')
    elif (Qnumber == 33):
        right_en_left()
    elif (Qnumber == 34):
        pow2pyramid()
    elif (Qnumber == 35):
        Loan()
    elif (Qnumber == 36):
        hexadec()
    elif (Qnumber == 37):
        e()
    elif (Qnumber == 38):
        prim()
    elif (Qnumber == 39):
        even()
    elif (Qnumber == 40):
        calculator()
    else:
        fact_sum()
     

    Qnumber = int(input("Enter Question Number 1-41:"))
    if (Qnumber <= 0) or (Qnumber > 41):
        print('Invalid Number!please Enter a valid one')
    if (Qnumber == 1):
        cube()
    elif (Qnumber == 2):
        triangle()
    elif (Qnumber == 3):
        rectangle()
    elif (Qnumber == 4):
        Line()
    elif (Qnumber == 5):
        Intersect()
    elif (Qnumber == 6 ):
        factorial()
    elif (Qnumber == 7 ):
        fibonacci(6)   
    elif (Qnumber == 8):
        prime_sum()
    elif (Qnumber == 9):
        ascend()
    elif (Qnumber == 10):
        G_mark()
    elif (Qnumber == 11):
        cellphone()
    elif (Qnumber == 12):
        max_min()
    elif (Qnumber == 13):
        reverse()
    elif (Qnumber == 14):
        gcd()
    elif (Qnumber == 15):
        lcm()
    elif (Qnumber == 16):
        frac_sum()
    elif (Qnumber == 17):
        isbn()
    elif (Qnumber == 18):
        exp()
    elif (Qnumber == 19):
        leap()
    elif (Qnumber == 20):
        maxoccurence()
    elif (Qnumber == 21):
        cube_of_digits()
    elif (Qnumber == 22):
        No_of_digit()
    elif (Qnumber == 23):
        No_of_prime()
    elif (Qnumber == 24):
        perfect_number()
    elif (Qnumber == 25):
        t_comp()
    elif (Qnumber == 26):
        tuition()
    elif (Qnumber == 27):
        conversion()
    elif (Qnumber == 28):
        student()
    elif (Qnumber == 29):
        stu()
    elif (Qnumber == 30):
        fivesix()
    elif (Qnumber == 31):
        ascii()
    elif (Qnumber == 32):
        print('1=A')
        print('2=B')
        sub_question = int(input('Enter 1 or 2:'))
        if (sub_question == 1):
            right_tri()
        elif (sub_question == 2):
            upside()
        else:
            print('Invalid input')
    elif (Qnumber == 33):
        right_en_left()
    elif (Qnumber == 34):
        pow2pyramid()
    elif (Qnumber == 35):
        Loan()
    elif (Qnumber == 36):
        hexadec()
    elif (Qnumber == 37):
        e()
    elif (Qnumber == 38):
        prim()
    elif (Qnumber == 39):
        even()
    elif (Qnumber == 40):
        calculator()
    else:
        fact_sum()

# =============================================================
#             THE END
# ============================================================

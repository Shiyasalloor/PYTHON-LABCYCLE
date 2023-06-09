# -*- coding: utf-8 -*-
"""QUESTION 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DIWDTN5o83f9dcKsPi2dkaioziV0LSp7
"""

# *Function to check a number is happy or not

def check_happy(num):
    for i in range(1, 101):
        sum = 0
        while (num > 0):
            r = num % 10
            num = num//10
            sum = sum+(r*r)
        if sum == 1:
            return True
        else:
            num = sum
            if (i == 100):
                return False

# *Function to get all happy numbers between a range


def happy_range(lowlimit, upprlimit):
    for i in range(lowlimit, upprlimit):
        isHappy = check_happy(i)
        if isHappy:
            print(i, end=" ")

# *Function to get all happy numbers upto n range


def happy_n(l, upprlimit):
    for i in range(l, upprlimit):
        isHappy = check_happy(i)
        if isHappy:
            print(i, end=" ")

# *To print a number is happy or not


num = int(input("Enter the number : "))
result = check_happy(num)
if result:
    print(num, "Is Happy ")
else:
    print(num, "Is Sad")

# *To print all happy numbers in a range

lower_limit = int(input("Enter the lower limit:"))
upper_limit = int(input("Enter the upper limit:"))
happy_range(lower_limit, upper_limit)

# *To print all happy numbers upto n range

limit = int(input("\nenter the limit of upto which you want to print: "))
happy_n(1, limit)
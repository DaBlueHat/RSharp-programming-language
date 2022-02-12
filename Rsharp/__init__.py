import random
import os

def println(string):
    print(string)

def add_nums(num1, num2):
    print(num1 + num2)

def subtract_nums(subnum1, subnum2):
    print(subnum1 - subnum2)

def divide_nums(divnum1, divnum2):
    print(divnum1 / divnum2)

def printrand(min, max):
    rand = random.randint(min, max)
    print(rand)

def startfile(filename):
    os.startfile(filename)

def close():
    exit()
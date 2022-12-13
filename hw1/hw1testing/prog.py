# Minh Nguyen
# Homework 1: Python Assignment 1 -- Finding Word Ladders
# cpsc3400
# Professor LeBlanc

#variables and types
x = 30
x = "Hello"

#Here is a list of basic types in Python:
#• Integers
#• Floating Point
#• Boolean
#o Literals are True and False
#• Strings
#o Either surrounded by single-quotes (') or double-quotes (")
#o Escape sequences in C++ work here:
# \n newline
# \t tab
# \\ backslash

#Arithmetic and Logical Operators
#use and or not instead of && || !
#** is used to raise to a power (2 ** 7 = 128)
#• // is floor division (7 // 4.0 = 1.0)
#o 7 / 4 = 1
#o 7 / 4.0 = 1.75

#Input / Output
num = 10
print("The number is: ", num)

#Multiple entities can be printed using a comma separated list.
#• Spaces are automatically added between the variables and strings.
#o To suppress the spaces, use sep='' as an argument.
#o Example: print("The number is", num, sep='')
#• A newline is automatically printed.
#o To suppress the newline, use end='' as an argument.
#o Example: print("The number is", num, end='')

inputStr = input("Enter a number: ")
inputNum = int(inputStr)

inputNum = int(input("Enter a number: "))

#Compound Statements and Indenting
#(def, while, for, if, elif, else):
#To introduce a compound statement:
#1. Start with a header statement – a statement
#(def, while, for, if, elif, else) that ends with a colon ':'
#2. The following lines (statements) must be indented.
#3. To end the compound statement, simply stop the indentation.

#if statements
a = 1
b = 2
if a < b:
 print("Less than")
elif a > b:
 print("Greater than")
else:
 print("Equal")

#while loops
x = 1
sum = 0
while x < 10:
 sum = sum + x
 x = x + 1 # or x += 1 but not x++
print(sum)

# function
#defined with def
def average(a, b, c):
 sum = a + b + c
 return sum / 3.0

#modules and libraries
import math
x = math.sqrt(2)
area = r ** 2 * math.pi

#Common modules:
#• math – math function
#• random – random number generation
#• os – operating system information
#• sys – system specific parameters
#• re – regular expressions

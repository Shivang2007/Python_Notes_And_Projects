
# Printing output
print("Hello World")

# Printing multiple values
print("Python", "Programming", 101)


# COMMENTS
# ------------------------------------------------------------

# Single-line comment

"""
Multi-line string.
Can also be used as a documentation string (docstring).
"""


# ------------------------------------------------------------
# VARIABLES
# ------------------------------------------------------------

# Variables are used to store data.
name = "Shivang"
age = 18
is_student = True

# Printing variables
print(name)
print(age)

# Multiple variable assignment
a, b, c = 10, 20, 30

# Assigning the same value
x = y = z = 100


# ------------------------------------------------------------
# INPUT AND OUTPUT
# ------------------------------------------------------------

# input() always returns a string.

name = input("Enter your name: ")
print("Hello", name)

# Taking integer input
age = int(input("Enter your age: "))

# Taking float input
marks = float(input("Enter your marks: "))

# Taking multiple inputs
a, b = input("Enter two numbers: ").split()

# Converting multiple inputs into integers
a, b = map(int, input().split())

# Formatted output (f-string)
print(f"My name is {name} and my age is {age}")


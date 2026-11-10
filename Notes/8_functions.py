

# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------

# Functions are reusable blocks of code.

def greet():
    print("Hello World")

greet()


# Function with parameters

def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# Default arguments

def greet(name="User"):
    print("Hello", name)

greet()
greet("Shivang")


# Keyword arguments

def details(name, age):
    print(name, age)

details(age=18, name="Shivang")


# Variable number of arguments (*args)

def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30))


# Keyword variable arguments (**kwargs)

def information(**data):
    print(data)

information(name="Shivang", age=18)


# Lambda function

square = lambda x: x * x
print(square(5))


# ------------------------------------------------------------
# RECURSION
# ------------------------------------------------------------

# A function calling itself is called recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# ------------------------------------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(type(numbers))
print(id(numbers))
print(abs(-10))
print(round(10.567, 2))
print(pow(2, 3))

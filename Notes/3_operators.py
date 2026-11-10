# ------------------------------------------------------------
# OPERATORS
# ------------------------------------------------------------

# A. Arithmetic Operators

a = 10
b = 3

print(a + b)     # Addition: 13
print(a - b)     # Subtraction: 7
print(a * b)     # Multiplication: 30
print(a / b)     # Division: 3.333...
print(a // b)    # Floor division: 3
print(a % b)     # Modulus: 1
print(a ** b)    # Exponentiation: 1000


# B. Comparison Operators

print(a == b)    # Equal to
print(a != b)    # Not equal to
print(a > b)     # Greater than
print(a < b)     # Less than
print(a >= b)    # Greater than or equal to
print(a <= b)    # Less than or equal to


# C. Logical Operators

x = True
y = False

print(x and y)   # AND
print(x or y)    # OR
print(not x)     # NOT


# D. Assignment Operators

x = 10

x += 5           # x = x + 5
x -= 2           # x = x - 2
x *= 2           # x = x * 2
x /= 2           # x = x / 2
x //= 2
x %= 2
x **= 2


# E. Bitwise Operators

a = 5            # Binary: 0101
b = 3            # Binary: 0011

print(a & b)     # AND
print(a | b)     # OR
print(a ^ b)     # XOR
print(~a)        # NOT
print(a << 1)    # Left shift
print(a >> 1)    # Right shift

# Toggle the third bit (bit position 2)
x = 10
x = x ^ (1 << 2)


# F. Membership Operators

numbers = [10, 20, 30]

print(20 in numbers)
print(40 not in numbers)


# G. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True
print(a is c)    # False
print(a == c)    # True


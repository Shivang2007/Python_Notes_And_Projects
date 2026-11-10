# ------------------------------------------------------------
# DATA TYPES
# ------------------------------------------------------------

# 1. Integer
a = 10

# 2. Float
b = 10.5

# 3. String
c = "Python"

# 4. Boolean
d = True

# 5. Complex
e = 2 + 3j

# 6. List
f = [10, 20, 30]

# 7. Tuple
g = (10, 20, 30)

# 8. Set
h = {10, 20, 30}

# 9. Dictionary
i = {"name": "Shivang", "age": 18}

# Checking data type
print(type(a))
print(type(c))


# ------------------------------------------------------------
# TYPE CONVERSION
# ------------------------------------------------------------

# Converting one data type into another.

x = "100"

a = int(x)       # String to integer
b = float(x)     # String to float
c = str(100)     # Integer to string

print(a, b, c)

# Other conversions
int(10.5)        # 10
float(10)        # 10.0
bool(1)          # True
list("ABC")      # ['A', 'B', 'C']

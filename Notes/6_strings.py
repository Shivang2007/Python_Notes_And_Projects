
# ------------------------------------------------------------
# STRINGS
# ------------------------------------------------------------

text = "Hello Python"

# Accessing characters
print(text[0])
print(text[-1])

# Slicing
print(text[0:5])
print(text[:5])
print(text[6:])
print(text[::-1])       # Reverse string

# String methods

name = "shivang"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())

text = "  Python  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

text = "Hello Python"

print(text.replace("Python", "World"))
print(text.find("Python"))
print(text.count("o"))
print(text.startswith("Hello"))
print(text.endswith("Python"))

# Splitting a string
text = "10 20 30"
numbers = text.split()

# Joining strings
words = ["Hello", "World"]
result = " ".join(words)

# String length
print(len(text))


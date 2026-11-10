
# ------------------------------------------------------------
# SETS
# ------------------------------------------------------------

# Sets are unordered collections of unique elements.

numbers = {10, 20, 30, 40}

# Adding elements
numbers.add(50)
numbers.update([60, 70])

# Removing elements
numbers.remove(20)
numbers.discard(100)    # Does not raise error if absent

# Set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Membership
print(3 in a)


# ------------------------------------------------------------
# DICTIONARIES
# ------------------------------------------------------------

# Dictionaries store data in key-value pairs.

student = {
    "name": "Shivang",
    "age": 18,
    "branch": "CSE"
}

# Accessing values
print(student["name"])
print(student.get("age"))

# Adding and updating
student["college"] = "NIT Patna"
student["age"] = 19

# Removing
student.pop("age")
del student["branch"]

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Iterating
for key, value in student.items():
    print(key, value)


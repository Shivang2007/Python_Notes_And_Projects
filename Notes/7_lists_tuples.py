

# ------------------------------------------------------------
# LISTS
# ------------------------------------------------------------

# Lists are ordered, mutable and allow duplicate values.

numbers = [10, 20, 30, 40, 50]

# Accessing elements
print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])

# Changing elements
numbers[0] = 100

# Adding elements
numbers.append(60)
numbers.insert(1, 15)
numbers.extend([70, 80])

# Removing elements
numbers.remove(30)      # Removes specified value
numbers.pop()           # Removes last element
numbers.pop(0)          # Removes element at index 0
del numbers[1]          # Deletes element

# Other methods
numbers.sort()
numbers.reverse()

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(numbers.count(40))
print(numbers.index(40))

# Copying a list
new_list = numbers.copy()

# Clearing a list
new_list.clear()

# Iterating through a list
for item in numbers:
    print(item)

# List comprehension
squares = [x*x for x in range(1, 6)]

# Filter even numbers
even = [x for x in range(1, 11) if x % 2 == 0]


# ------------------------------------------------------------
# TUPLES
# ------------------------------------------------------------

# Tuples are ordered and immutable.

numbers = (10, 20, 30, 40)

print(numbers[0])
print(numbers[-1])
print(numbers[1:3])

print(len(numbers))
print(numbers.count(20))
print(numbers.index(30))

# Tuple unpacking
a, b, c, d = numbers

# Reverse a list
numbers = [1, 2, 3, 4]
numbers.reverse()

# Reverse without modifying original list
reversed_list = numbers[::-1]

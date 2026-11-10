
# Enumerate
for index, value in enumerate(numbers):
    print(index, value)

# Zip
names = ["A", "B", "C"]
marks = [80, 90, 95]

for name, mark in zip(names, marks):
    print(name, mark)

# Map
values = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, values))

# Filter
even = list(filter(lambda x: x % 2 == 0, values))

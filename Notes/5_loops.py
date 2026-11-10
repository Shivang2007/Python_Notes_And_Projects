
# ------------------------------------------------------------
# LOOPS
# ------------------------------------------------------------

# FOR LOOP

for i in range(5):
    print(i)

# range(start, stop, step)

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)


# WHILE LOOP

i = 1

while i <= 5:
    print(i)
    i += 1


# BREAK
# Terminates the loop immediately.

for i in range(10):
    if i == 5:
        break
    print(i)


# CONTINUE
# Skips the current iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)


# PASS
# Does nothing; used as a placeholder.

for i in range(5):
    pass


# NESTED LOOPS

for i in range(3):
    for j in range(3):
        print(i, j)


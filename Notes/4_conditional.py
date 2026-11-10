
# ------------------------------------------------------------
# CONDITIONAL STATEMENTS
# ------------------------------------------------------------

# IF statement

age = 18

if age >= 18:
    print("Eligible to vote")


# IF-ELSE statement

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# IF-ELIF-ELSE statement

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# Nested IF

age = 20

if age >= 18:
    if age >= 21:
        print("Age is 21 or above")
    else:
        print("Age is between 18 and 20")


# Ternary operator

a = 10
b = 20

maximum = a if a > b else b
print(maximum)


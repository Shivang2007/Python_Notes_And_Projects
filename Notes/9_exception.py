
# ------------------------------------------------------------
# EXCEPTION HANDLING
# ------------------------------------------------------------

# Used to handle runtime errors.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid integers")

except Exception as error:
    print("Error:", error)

else:
    print("No exception occurred")

finally:
    print("Execution completed")


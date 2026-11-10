
# Swapping two variables
a = 10
b = 20

a, b = b, a




# Check palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


# Check prime number

n = 17
is_prime = n > 1

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)


# Fibonacci series

a, b = 0, 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b


# Count frequency of elements

numbers = [1, 2, 2, 3, 3, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

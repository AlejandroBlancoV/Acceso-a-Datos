# Ask the user for an integer
num = int(input("Enter an integer: "))

# Check if the number is prime
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

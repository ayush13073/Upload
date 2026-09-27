n = int(input("Enter a number: "))

sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum = sum + i

    i = i + 1

if sum == n:
    print("The number is equal to the sum of all its divisors.")
else:
    print("The number is not equal to the sum of all its divisors.")

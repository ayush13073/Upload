n = int(input("Enter a number: "))

original = n
temp = n
digits = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    power = 1
    i = 0

    while i < digits:
        power = power * digit
        i = i + 1

    sum = sum + power
    temp = temp // 10

if sum == original:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

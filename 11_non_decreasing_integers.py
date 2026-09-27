a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

if a > b:
    temp = a
    a = b
    b = temp

if b > c:
    temp = b
    b = c
    c = temp

if a > b:
    temp = a
    a = b
    b = temp

print("Numbers in non-decreasing order:", a, b, c)

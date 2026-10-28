"""
Question 14: Write a Python program to create Fibonacci series up to n using Lambda.
"""

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

terms = int(input("Enter the number of terms: "))

series = []
for i in range(terms):
    series.append(fib(i))

print("Fibonacci Series:", series)

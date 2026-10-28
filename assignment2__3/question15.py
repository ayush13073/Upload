"""
Question 15: Write a compose(f, g) utility function that returns a new function equivalent to applying g first and then f to the result — that is, compose(f, g)(x) should equal f(g(x)). Test it by composing a lambda that doubles a number with a lambda that adds.
"""


def compose(f, g):
    return lambda x: f(g(x))


double = lambda x: x * 2
add_one = lambda x: x + 1

combined = compose(double, add_one)

num = int(input("Enter a number: "))
print("Result:", combined(num))

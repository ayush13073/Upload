"""
Question 23: Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
"""

strings = ["hello world", "hello python", "world of python"]

words = []

for s in strings:
    for w in s.split():
        words.append(w)

unique_words = set(words)

for word in unique_words:
    count = words.count(word)
    print(word, ":", count)

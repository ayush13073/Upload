"""
Question 20: Write a Python program to convert more than one list to a nested dictionary.
"""

keys = ["a", "b", "c"]
list1 = [1, 2, 3]
list2 = [10, 20, 30]

nested = {}

for i in range(len(keys)):
    nested[keys[i]] = {"list1": list1[i], "list2": list2[i]}

print(nested)

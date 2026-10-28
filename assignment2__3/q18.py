names= ["ayush", "arun"]
ages  = ["23", "32"]
cities = ["pune", "mumbai"]

student = {}

i = 0

while i < len(names):
    inner = {}

    inner["age"] = ages[i]
    inner["cities"] = cities[i]

    student[names[i]] = inner

    i = i + 1

print(student)
import csv

with open("student1.csv","w",newline="") as file:
    writer = csv.writer(file)

    
    writer.writerow(["Name", "City", "Marks"])
    writer.writerow(["Riya", "Pune", 80])
    writer.writerow(["Siya", "Nashik", 85])
    writer.writerow(["Krish", "Nagpur", 75])

print("csv file written")

with open("student1.csv", "r") as file:
    reader = csv.reader(file)
    print("|"+"-" * 36+"|")
    next(reader)

    print("|%-10s | %-10s | %-10s|" %("Name","City","Marks"))
    print("|"+"-" * 36+"|")
    for row in reader:
        print("|%-10s | %-10s | %-10s|" %(row[0],row[1],row[2]))

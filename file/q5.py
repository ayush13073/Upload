import pandas as pd
from tabulate import tabulate

# ---------- write Excel ----------
data = {
    "Name":  ["Riya", "Siya", "Krish"],
    "City":  ["Pune", "Nashik", "Nagpur"],
    "Marks": [80, 85, 75]
}
df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)
print("Excel file written")
print("")

# ---------- read Excel ----------
df2 = pd.read_excel("students.xlsx")

print(tabulate(df2, headers="keys", tablefmt="grid", showindex=False))

"""
Question 5: Read excel file and display the result in tabular format.
Hint: import pandas and tabulate.
"""

import pandas as pd
from tabulate import tabulate

try:
    df = pd.read_excel("students.xlsx")
except Exception:
    df = pd.read_csv("students.csv")

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

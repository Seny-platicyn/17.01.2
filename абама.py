import pandas as pd
from openpyxl import Workbook

df = pd.read_excel('LIST.xlsx')

for i in range(len(df)):
    print(f"{i+1}. {df.iloc[i]}")

choice = int(input("Введите номер строки, которую хотите выбрать: "))

if choice <= len(df):
    selected_row = df.iloc[choice-1]
    print(f"Ваша выбранная строка:\n{selected_row}")
else:
    print("Неверный номер строки!")


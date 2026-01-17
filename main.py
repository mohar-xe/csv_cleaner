import pandas as pd

print("Enter the file path of the CSV file to clean:")
file_path = input()

file = pd.read_csv(file_path)
print(file.describe())

print("1. Remove Duplicates \n 2. Fill Missing Value \n 3. Change Date Format \n 4. Exit")



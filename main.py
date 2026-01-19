import pandas as pd
import os


print("Enter the file path of the CSV file to clean:")
file_path = input()

file = pd.read_csv(file_path)
print(file.describe())

print("1. Remove Duplicates \n 2. Fill Missing Value \n 3. Change Date Format \n 4. Exit")
option = int(input())
if option == 1:
    cleaned_file = file.drop_duplicates()
    print("Duplicates removed.")
elif option == 2:
    print("Enter the column name to fill missing values:")
    column_name = input()
    print("Enter the value to fill missing values with:")
    fill_value = input()
    cleaned_file = file.fillna({column_name: fill_value})
    print(f"Missing values in column '{column_name}' filled with '{fill_value}'.")
elif option == 3:
    print("Enter the column name with date values:")
    date_column = input()
    print("Enter the desired date format (e.g., '%Y-%m-%d'):")
    date_format = input()
    cleaned_file = file.copy()
    cleaned_file[date_column] = pd.to_datetime(cleaned_file[date_column]).dt.strftime(date_format)
    print(f"Date format in column '{date_column}' changed to '{date_format}'.")
else:
    print("Exiting without changes.")
    cleaned_file = file

if option != 4:
    base_name = "cleaned_file"
    extension = ".csv"
    output_path = base_name + extension
    count = 1

while os.path.exists(output_path):
    output_path = f"{base_name}_{count}{extension}"
    count += 1
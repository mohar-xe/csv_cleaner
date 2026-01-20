import pandas as pd
import os


print("Enter the file path of the CSV file to clean:")
file_path = input() #Inputs the file path from the user

file = pd.read_csv(file_path)
print(file.describe()) #Displays basic statistics of the CSV file

print("1. Remove Duplicates\n2. Fill Missing Value\n3.Change Date Format \n4. Exit")
#Checking if the input is valid
try:
    option = int(input())
    if option < 1 or option > 4:
        print("Invalid input. Please enter a number between 1 and 4.")
        option = 4
except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    option = 4

#Cleaning operations
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

#Generating unique output file name and saving
if option != 4:
    base_name = "cleaned_file"
    extension = ".csv"
    output_path = base_name + extension
    count = 1
    
    while os.path.exists(output_path):
        output_path = f"{base_name}_{count}{extension}"
        count += 1
    
    cleaned_file.to_csv(output_path, index=False)
    print(f"Cleaned file saved as '{output_path}'.")
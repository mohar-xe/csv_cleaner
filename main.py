import pandas as pd

print("Enter the file path of the CSV file to clean:")
file_path = input()

file = pd.read_csv(file_path)
print(file.describe())





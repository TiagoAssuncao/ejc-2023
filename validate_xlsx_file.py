import openpyxl

# Open the Excel file
workbook = openpyxl.load_workbook('file.xlsx')

# Select the first worksheet
sheet = workbook.active

# Store the values of the second column in a list
column2 = [cell.value for cell in sheet['B']]

duplicates = {}

for i, value in enumerate(column2):
    if value in column2[i+1:] and value not in duplicates.values():
        index = column2[i+1:].index(value) + i + 1
        duplicates[index] = value

if duplicates:
    print("The following rows contain duplicate values in the second column:")
    for index, value in duplicates.items():
        print(f"Row {index+1}: {value}")
else:
    print("There are no duplicate values in the second column of the file.")

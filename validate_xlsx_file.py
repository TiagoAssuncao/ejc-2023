import openpyxl
import re

def check_duplicates():
    """Check for duplicate values in the second column of an Excel file.

    Reads an Excel file named 'file.xlsx', selects the first worksheet, and stores the values of the second column in a list
    after cleaning the values of any whitespace or special characters. Then, checks for duplicate values in the list and
    prints out the rows containing the duplicates.

    Returns:
    None
    """

    # Open the Excel file
    workbook = openpyxl.load_workbook('file.xlsx')

    # Select the first worksheet
    sheet = workbook.active

    # Store the values of the second column in a list, cleaned of whitespace and special characters
    column2 = [re.sub(r'\W+', '', str(cell.value).strip()) for cell in sheet['B']]

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


check_duplicates()

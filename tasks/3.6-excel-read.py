import openpyxl
# Load the Excel workbook
workbook = openpyxl.load_workbook('hosts.xlsx')
# Get the active sheet
sheet = workbook.active
# Print the sheet title
print(sheet.title)
# print column names 
for cell in sheet[1]:
    print(cell.value)

# your code goes here
# print the first column
for cell in sheet['A']:
    print(cell.value)
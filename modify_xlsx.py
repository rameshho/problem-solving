import sys
from openpyxl import load_workbook
filename = sys.argv[1]
workbook = load_workbook(filename)

worksheet = workbook.get_sheet_by_name("Current")

index = 2
while True:
    cell = 'D' + str(index)
    cell_content = worksheet[cell].value
    if cell_content:
        worksheet[cell] = cell_content.replace('-02-', '-03-')
        index += 1
    else:
        break

workbook.save(filename)

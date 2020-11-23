import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
try:
    ws1 = wb.create_sheet("TestSheet")
    ws1.sheet_properties.tabColor = "1072BA"
    print(' Created worksheet successfuly')
except:
    print(" Error occured while creating worksheet")

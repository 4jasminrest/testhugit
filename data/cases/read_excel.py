import os
import yaml
from openpyxl import load_workbook

#获取工作簿
wb = load_workbook('D:/test.xlsx')
#获取工作表--Sheet
# 获得所有sheet的名称
print(wb.get_sheet_names())
# 根据sheet名字获得sheet
a_sheet = wb.get_sheet_by_name('Sheet1')
# 获得sheet名
print(a_sheet.title)
# 获得当前正在显示的sheet, 也可以用wb.get_active_sheet()
sheet = wb.active
column = sheet.columns
row = sheet.rows
value1 = sheet.values


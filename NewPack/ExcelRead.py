

import xlrd

wb=xlrd.open_workbook("C:\\Users\\Shubham\\OneDrive\\Desktop\\Study\\Selenium\\Book1.xls")
sh=wb.sheet_by_name("MyData")
print(sh.nrows)
print(sh.ncols)

for i in range(1,sh.nrows):
    name=sh.cell_value(i,0)
    password=sh.cell_value(i,1)
    company=sh.cell_value(i,2)
    salary=sh.cell_value(i,3)
    print(name,password,company,salary)
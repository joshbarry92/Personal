##Read Budget Sheets and Return Requested Values
import xlrd
import os

#######

#List all the file locations
#path = input('Please Enter XLS Locations: ')
path = 'C:\\Users\\Joshua Barry\\Desktop\\FY04'
x = os.listdir(path)
num = len(x)
l =[]
###

for budgets in range(0,num):
    s = path + '\\' + x[budgets]
    print(s)
    workbook = xlrd.open_workbook(s)
    worksheet = workbook.sheet_by_name('Summary')
    cell_value1 = worksheet.cell_value(16,1)
    cell_value2 = worksheet.cell_value(16,2)
    fin = x[budgets] + '| Requested: ' + str(cell_value1) + '| Allocated: ' + str(cell_value2)
    l.append(fin)
    #print(l) 

file2 = open('FY04 Budget List.txt','w')
for item in l:
  file2.write("%s\n" % item)
file2.close()





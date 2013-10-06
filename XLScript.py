##Import Statements for Excel Fils ##
import xlrd
import xlwt
import os

##Look in Directory and make Matrix of files ## 
x = os.listdir("C:\Users\Joshua Barry\Desktop\InvFY14")
num = len(x)

##Define book to write into
writebook = xlwt.Workbook()
writesheet = writebook.add_sheet('Inventory')

#Initialize Sheet
writesheet.write(2,1,'Inventory Sheet')
writesheet.write(4,1,'Fiscal Year 14')
writesheet.write(6,0,'Item')
writesheet.write(6,1,'Model/Desc.')
writesheet.write(6,2,'Quanity')
writesheet.write(6,3,'Condition')
writesheet.write(6,4,'Yr. Purchased')
writesheet.write(6,5,'Purchase Price')
writesheet.write(6,6,'Club Name')
#End sheet initialization

#Row to start with in new sheet#
aRow = 6

#Loop to iterate through saved excel sheets 
for booknum in range (0, num-1):
	aRow = aRow + 1 
	str = x[1]
	workbook = xlrd.open_workbook(x[booknum])
	worksheet = workbook.sheet_by_name('Sheet1')

	num_rows = worksheet.nrows - 1
	num_cells = worksheet.ncols - 1
	curr_row = 3
	
	c1 = worksheet.cell_value(4,1)
	c2 = worksheet.cell_value(4,2)
	club = c1+c2
	print club
	
	## While Loop to Iterate through rows ##
	while curr_row < num_rows:
		curr_row += 1
		row = worksheet.row(curr_row)
		print 'Row:', curr_row
		curr_cell = -1
		##While loop to look at each column in the cosen row ##
		while curr_cell < num_cells:
			curr_cell += 1
			# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
			cell_type = worksheet.cell_type(curr_row, curr_cell)
			cell_value = worksheet.cell_value(curr_row, curr_cell)
			writesheet.write(aRow, curr_cell, cell_value)
			print '	', cell_type, ':', cell_value
			writebook.save('tester.xls')

		
writebook.save('tester.xls')
raw_input("Press Enter to continue...")


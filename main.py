import itertools
import xlrd
import sys
import util

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    file_name = 'E.xlsx'

xl_workbook = xlrd.open_workbook(file_name)
xl_sheet = xl_workbook.sheet_by_index(0)
print('Open Excel workbook %s, sheetname: %s' % (file_name, xl_sheet.name))

ncols = xl_sheet.ncols  # Number of columns
nrows = xl_sheet.nrows

print('Stats: \n\t rows: %s, columns: %s' % (nrows, ncols))
util.printsheet(xl_sheet)
comb = []
util.getallcomb(comb, ncols)
util.get_data(xl_sheet, comb)
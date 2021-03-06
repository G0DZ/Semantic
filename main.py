import itertools
import xlrd
import sys
#import newutil
import datatools
import logic
import util

from config import logger


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'E.xlsx'

    table = datatools.get_data(filename)
    nrows = len(table)
    ncols = 0
    if nrows:
        ncols = len(table[0])
    if ncols:
        logger.info('Stats: rows: %s, columns: %s' % (nrows, ncols))
        comb_list = util.combinations(ncols)

#
# xl_workbook = xlrd.open_workbook(file_name)
# xl_sheet = xl_workbook.sheet_by_index(0)
# print('Open Excel workbook %s, sheetname: %s' % (file_name, xl_sheet.name))
#
# ncols = xl_sheet.ncols  # Number of columns
# nrows = xl_sheet.nrows
#
# print('Stats: \n\t rows: %s, columns: %s' % (nrows, ncols))
# #util.printsheet(xl_sheet)
# comb_list = util.getallcomb(ncols)
# # logic.q_inf(xl_sheet, 0, 0)
import math

import util


def q_inf(sheet, row, col):
    #количество информации для ячейки
    base = sheet.nrows
    value = 0
    for row_ind in range(0, sheet.nrows):
        if sheet.cell(row_ind, col).value == sheet.cell(row, col).value:
            value += 1
    l = math.log(value, base)
    print("log(base=%s, value=%s) = %s | (row=%s,col=%s) " % (base, value, l, row, col))
    return l
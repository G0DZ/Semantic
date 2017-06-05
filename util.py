import itertools

import math


def printsheet(sheet):
    for row_idx in range(0, sheet.nrows):  # Iterate through rows
        print('-' * 40)
        print('Row: %s' % row_idx)  # Print row number
        for col_idx in range(0, sheet.ncols):  # Iterate through columns
            cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            print('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
    print('-' * 40 + "\n" + '-' * 40 + '\n')


def getallcomb(comb_list, ncols):
    l = list(range(0,ncols))
    #print(l)
    if ncols != 1:
        comb_list.append([])
    for dilimeter in range(1, ncols):
        sublist = [x for x in l if x < dilimeter]
        #sublist = list(l)
        #sublist.remove(dilimeter)
        comb_dilim = list()
        for L in range(0, len(sublist) + 1):
            for subset in itertools.combinations(sublist, L):
                if subset:
                    #print(subset, "->", dilimeter)
                    comb_dilim.append(subset)
        comb_list.append(comb_dilim)


def get_data(sheet, comb):
    for r in range(1, 2): #range(len(comb)): #0 always = []
        print(r, comb[r])
        for l in comb[r]:
            cond_ent(l, r, sheet)


def q_inf(left, right, sheet, row):
    comp_base = []
    comp_value = []
    #base
    for row_ind in range(0, sheet.nrows):
        contains = True
        for col_ind in range(0, sheet.ncols):
            if col_ind in left:
                if not (sheet.cell(row_ind, col_ind).value == sheet.cell(row, col_ind).value):
                    contains = False
                    break
        #print(contains)
        if contains:
            #print("hello: ", row_ind)
            comp_base.append(row_ind)
    print(comp_base)

    #value
    for row_ind in range(0, sheet.nrows):
        if row_ind in comp_base:
            if sheet.cell(row_ind, right).value == sheet.cell(row, right).value:
                comp_value.append(row_ind)
    print(comp_value)

    #ret
    return math.log(len(comp_value), len(comp_base))


def pr_cond_ent(left, right, sheet, row):
    comp_base = []
    comp_value = []

    # base
    for row_ind in range(0, sheet.nrows):
        contains = True
        for col_ind in range(0, sheet.ncols):
            if col_ind in left:
                if not (sheet.cell(row_ind, col_ind).value == sheet.cell(row, col_ind).value):
                    contains = False
                    break
        # print(contains)
        if contains:
            # print("hello: ", row_ind)
            comp_base.append(row_ind)
    print(comp_base)

    # value
    result = 0
    for row_ind in range(0, sheet.nrows):
        comp_value= []
        for row_check in range (0, sheet.nrows):
            if row_ind in comp_base and row_check in comp_base:
                #print(row_ind, row_check)
                if sheet.cell(row_ind, right).value == sheet.cell(row_check, right).value:
                    #print(row_ind, ":", sheet.cell(row_ind, right).value, ",",
                    #      row_check, ":", sheet.cell(row_check, right).value)
                    comp_value.append(row_ind)
        if comp_value:
            #print(comp_value, comp_base, sheet.nrows)
            lo = math.log(len(comp_value), len(comp_base))
            k = lo / (sheet.nrows) # *len(comp_value)
            result += k
            print(lo, k, result)
    return result


def cond_ent(left, right, sheet):
    sum = 0
    for main_row_ind in range(0, sheet.nrows):
        comp_base = []
        comp_value = []

        # base
        for row_ind in range(0, sheet.nrows):
            contains = True
            for col_ind in range(0, sheet.ncols):
                if col_ind in left:
                    if not (sheet.cell(row_ind, col_ind).value == sheet.cell(main_row_ind, col_ind).value):
                        contains = False
                        break
            # print(contains)
            if contains:
                # print("hello: ", row_ind)
                comp_base.append(row_ind)
        print(comp_base)

        # value
        result = 0
        for row_ind in range(0, sheet.nrows):
            comp_value = []
            for row_check in range(0, sheet.nrows):
                if row_ind in comp_base and row_check in comp_base:
                    # print(row_ind, row_check)
                    if sheet.cell(row_ind, right).value == sheet.cell(row_check, right).value:
                        # print(row_ind, ":", sheet.cell(row_ind, right).value, ",",
                        #      row_check, ":", sheet.cell(row_check, right).value)
                        comp_value.append(row_ind)
            if comp_value:
                # print(comp_value, comp_base, sheet.nrows)
                lo = math.log(len(comp_value), len(comp_base))
                k = lo / (sheet.nrows)
                result += k
                #print(lo, k, result)
        h_i = result / (len(left)*sheet.nrows) #* len(comp_base)
        sum+= h_i

        #print(result, len(comp_base), len(left), h_i)
        print(h_i, sum)
    return sum
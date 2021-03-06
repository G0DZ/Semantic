import itertools

import math

def combinations(ncols):
    l = list(range(0, ncols))
    comb_list = []
    for dilimeter in range(0, ncols):
        sublist = list(l)
        sublist.remove(dilimeter)
        comb_dilim = list()
        for L in range(0, len(sublist) + 1):
            for subset in itertools.combinations(sublist, L):
                if subset:
                    comb_dilim.append(subset)
        comb_list.append(comb_dilim)
    return comb_list

def accel_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

print(list(accel_asc(3)))
print(combinations(3))
################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB4--ex2  |--#
################################################################################

import fractions as fr
from math import ceil

def make_triangle(rows):
    lst = []
    for i in range(1, rows):
        tmp = [fr.Fraction(1, i)]
        for j in range(1, i):
            tmp.append(fr.Fraction(lst[i - 2][0][j - 1] - tmp[j - 1]))
        strtmp = [str(x) for x in tmp]
        lst.append((tmp, len("   ".join(strtmp))))
    return lst


def print_triangle(lst):
    maxi = ceil(lst[len(lst) - 1][1] / 2)
    for i in range(len(lst)):
        cnt = maxi - ceil(lst[i][1] / 2)
        print(" " * cnt, end="")
        for j in lst[i][0]:
            print(j, end="   ")
        print("")


################################################################################

rows = input("Enter the nr of rows: ")
if rows.isalpha() or int(rows) < 1:
    print("Errorino."); exit()
print("\nThe Leibniz's harmonic triangle:\n\n")
print_triangle(make_triangle(int(rows) + 1))

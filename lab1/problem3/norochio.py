################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB1--ex3  |--#
################################################################################

from math import log, ceil
from random import randint

def get_result(n):
    boxes = 0
    photos = [x for x in range(n)]
    while photos:
        chio = randint(0, n - 1)
        if chio in photos:
            photos.remove(chio)
        boxes += 1
    return boxes


################################################################################

cases = 1000
n = int(input("Enter n: "))
boxes = sum([get_result(n) for x in range(cases)])
print("The minimal value of boxes is %d" % ceil(boxes / cases))
print("While the estimated value of boxes is %d" % (n * log(n) + n * log(2)))

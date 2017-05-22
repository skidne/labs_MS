################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex11 |--#
################################################################################

from random import random

def findRoots():
    u = random()
    delta = (4 * u) ** 2 - 4
    if delta < 0:
        return 0
    root1 = ((4 * u) - delta) / 2
    root2 = ((4 * u) + delta) / 2
    if isinstance(root1, (float, int)) and isinstance(root2, (float, int)):
        if root1 != root2:
            return 1
    return 0

cnt = 0
for i in range(1000):
    cnt += findRoots()

print("The probability is %f." % (cnt / 1000))
################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex3  |--#
################################################################################

from random import randint, random
from math import sqrt

def findRoots(b, c, pos):
    delta = b ** 2 - 4 * c
    if delta < 0:
        return 0
    root1 = (b - delta) / 2
    root2 = (b + delta) / 2
    if pos:
        if root1 > 0 and root2 > 0:
            return 1
    else:
        if isinstance(root1, (float, int)) and isinstance(root2, (float, int)):
            return 1
    return 0

real = 0
pos = 0
for i in range(10000):
    # [-1, 1]
    b = random() - randint(0, 1);
    c = random() - randint(0, 1);
    real += findRoots(b, c, False)
    pos += findRoots(b, c, True)

print("Probability of real roots is %.2f" % (real / 10000))
print("Probability of positive roots is %.2f" % (pos / 10000))

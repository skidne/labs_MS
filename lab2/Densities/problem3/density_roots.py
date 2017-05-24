################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex3  |--#
################################################################################

from random import randint, random
from math import sqrt

def find_roots(b, c, pos):
    delta = b ** 2 - 4 * c
    if delta < 0:
        return 0
    root1 = (b - sqrt(delta)) / 2
    root2 = (b + sqrt(delta)) / 2
    if pos and root1 > 0 and root2 > 0:
        return 1
    elif not pos and (isinstance(root1, (float, int)) and
            isinstance(root2, (float, int))):
        return 1
    return 0


################################################################################

real    = 0
pos     = 0
cases   = 10000

for i in range(cases):
    b = random() - randint(0, 1);
    c = random() - randint(0, 1);
    real += find_roots(b, c, False)
    pos += find_roots(b, c, True)

print("Probability of real roots is %.2f" % (real / cases))
print("Probability of positive roots is %.2f" % (pos / cases))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex12 |--#
################################################################################

from random import uniform
from math import sqrt

def findProb(x, y, rightHalf, less5, great5, within5):
    if x >= 0 and rightHalf:
        return 1
    if -5 <= x <= 5 and y**2 <= 25 - x**2:
        if less5:
            return 1
    else:
        if great5:
            return 1
    if within5 and -5 <= x <= 5 and (y - 5)**2 <= 25 - x**2:
        return 1
    return 0

probRightHalf = 0
probLess5 = 0
probGreater5 = 0
probWithin5 = 0
cases = 1000

for i in range(cases):
    x = uniform(-10, 10)
    y = uniform(0, sqrt(100 - x**2))
    probRightHalf += findProb(x, y, True, False, False, False)
    probLess5 += findProb(x, y, False, True, False, False)
    probGreater5 += findProb(x, y, False, False, True, False)
    probWithin5 += findProb(x, y, False, False, False, True)

print("Right Half of the upper half = %.3f" % (probRightHalf / cases))
print("Less than 5 inches from the center = %.3f" % (probLess5 / cases))
print("Greater than 5 inches from the center = %.3f" % (probGreater5 / cases))
print("Within 5 inches of the point (0, 5) = %.3f" % (probWithin5 / cases))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex12 |--#
################################################################################

from random import uniform
from math import sqrt

def find_prob(x, y, right_half, less5, great5, within5):
    if right_half and x >= 0:
        return 1
    if less5 and -5 <= x <= 5 and y**2 <= 25 - x**2:
        return 1
    if great5 and y**2 > 25 - x**2:
        return 1
    if within5 and (y - 5)**2 >= 25 - x**2:
        return 1
    return 0


################################################################################

prob_right_half = 0
prob_less5 = 0
prob_greater5 = 0
prob_within5 = 0
cases = 10000
i = 0

while i < cases:
    x = uniform(-10, 10)
    y = uniform(0, 10)
    if y < sqrt(100 - x**2):
        prob_right_half += find_prob(x, y, True, False, False, False)
        prob_less5 += find_prob(x, y, False, True, False, False)
        prob_greater5 += find_prob(x, y, False, False, True, False)
        prob_within5 += find_prob(x, y, False, False, False, True)
        i += 1

print("Right Half of the upper half = %.3f" % (prob_right_half / cases))
print("Less than 5 inches from the center = %.3f" % (prob_less5 / cases))
print("Greater than 5 inches from the center = %.3f" % (prob_greater5 / cases))
print("Within 5 inches of the point (0, 5) = %.3f" % (prob_within5 / cases))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex1  |--#
################################################################################

from random import random

def isTriangle(a, b, c):
	if a + b < c or a + c < b or b + c < a:
		return 1
	return 0

cnt = 0
for i in range(10000):
	ab = random()
	b = 1 - ab;
	if (ab > b):
		bc = ab - random()
	else:
		bc = b - random()
	cd = 1 - bc - ab
	cnt += isTriangle(ab, bc, cd)

print("The Probability is %.2f" % (cnt / 10000));

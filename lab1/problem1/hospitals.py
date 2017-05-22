################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB1--ex1  |--#
################################################################################

from random import randint

def one_day_hosp(kids):
    boys_total = 0
    for i in range(1, kids):
        boy = randint(0, 1)
        boys_total += 1 if boy else 0
    if ((boys_total / kids) * 100) > 60:
        return 1
    return 0


################################################################################

large_hdays = 0
small_hdays = 0

for i in range(1, 365):
    large_hdays += one_day_hosp(45)
    small_hdays += one_day_hosp(15)

if large_hdays < small_hdays:
    print("b) The small hospital")
elif large_hdays > small_hdays:
    print("a) The large hospital")
else:
    print("c) Neither, the number of days will be about the same")

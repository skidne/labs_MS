################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB5--ex2  |--#
################################################################################

import start
from operator import itemgetter

info = start.take_matrix()

people = info[0]
sum_line = info[2]

to_sort = dict(zip(people, sum_line))
sorted_people = sorted(to_sort.items(), key=itemgetter(1), reverse=True)

to_print = "%-20s%9s" % ("Name", "Friends")
print(to_print + "\n" + ("-" * len(to_print)))
for i, name in enumerate(sorted_people):
    print("%-20s|%5d" % (name[0], name[1]))

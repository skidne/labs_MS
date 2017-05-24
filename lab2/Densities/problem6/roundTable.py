################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex6  |--#
################################################################################

from random import shuffle

def find_neighbours(nr, meeting):
    arrangement = {}
    for i in range(nr):
        if i == 0:
            arrangement[meeting[i]] = [meeting[nr - 1], meeting[i + 1]]
        elif i == nr - 1:
            arrangement[meeting[i]] = [meeting[i - 1], meeting[0]]
        else:
            arrangement[meeting[i]] = [meeting[i - 1], meeting[i + 1]]
    return arrangement


def check(nr, lunch, dinner):
    lunch_neighbours = find_neighbours(nr, lunch)
    dinner_neighbours = find_neighbours(nr, dinner)
    for key in lunch_neighbours:
        for key2 in dinner_neighbours:
            if key == key2:
                exists = [i in dinner_neighbours[key2] for i in lunch_neighbours[key]]
                if exists == [True, True]:
                    return 0
    return 1


def no_neighbours(nr):
    lunch = [x for x in range(nr)]
    dinner = [x for x in range(nr)]
    shuffle(lunch); shuffle(dinner)
    if check(nr, lunch, dinner):
        return 1
    return 0


################################################################################

cnt = 0
nr_people = 1000
cases = 1000

for i in range(cases):
    cnt += no_neighbours(nr_people);

print("The probability is %.1f%%" % (cnt / nr_people))

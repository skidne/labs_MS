################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex6  |--#
################################################################################

from random import shuffle

# saving the neighbours of each person in a dictionary #
def findNeighbours(nr, meeting):
    arrangement = {}
    for i in range(nr):
        if i == 0:
            arrangement[meeting[i]] = [meeting[nr - 1], meeting[i + 1]]
        elif i == nr - 1:
            arrangement[meeting[i]] = [meeting[i - 1], meeting[0]]
        else:
            arrangement[meeting[i]] = [meeting[i - 1], meeting[i + 1]]
    return arrangement

# checking if at least one of the neighbours are the same #

def check(nr, lunch, dinner):
    lunchNeighbours = findNeighbours(nr, lunch)
    dinnerNeighbours = findNeighbours(nr, dinner)
    for key in lunchNeighbours:
        for key2 in dinnerNeighbours:
            if key == key2:
                exists = [i in dinnerNeighbours[key2] for i in lunchNeighbours[key]]
                if exists == [True, True]:
                    return 0
    return 1

# returns 1 if it didn't find the same neighbour twice #

def noNeighbours(nr):
    lunch = [x for x in range(nr)]
    dinner = [x for x in range(nr)]
    shuffle(lunch); shuffle(dinner)
    if (check(nr, lunch, dinner)):
        return 1
    return 0

cnt = 0
for i in range(1000):
    # you can check for numbers bigger than 10 #
    cnt += noNeighbours(10);
print("The probability is %.1f%%" % (cnt / 10))

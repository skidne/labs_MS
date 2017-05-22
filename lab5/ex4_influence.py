################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB5--ex4  |--#
################################################################################

import start
from operator import itemgetter

def take_nr_friends():
    info = start.take_matrix()
    people = info[0]
    sum_line = info[2]

    friends = dict(zip(people, sum_line))
    return people, friends


def take_influence():
    fname = "./influence.txt"
    content = [line.strip('\n ') for line in open(fname)]
    raw_influence = [line.split(" : ") for line in content]
    influence = {name : float(infl) for (name, infl) in raw_influence}
    return influence


def compute_influence():
    people, friends = take_nr_friends()
    influence = take_influence()
    raw_infl = {}

    for person in people:
        raw_infl[person] = 0.5 * friends[person] * influence[person]

    new_infl = sorted(raw_infl.items(), key=itemgetter(1), reverse=True)
    return new_infl


def main():
    influence = compute_influence()
    to_print = "%-20s%13s" % ("Name", "Influence")
    print(to_print + "\n" + ("-" * len(to_print)))
    for person in influence:
        print("%-20s|%10.3f" % person)


################################################################################

if __name__ == "__main__":
    main()

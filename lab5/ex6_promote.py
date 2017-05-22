################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB5--ex6  |--#
################################################################################

from ex5_analyze import find_interests
from ex4_influence import compute_influence
from operator import itemgetter

def people_interests():
    fname = "./people_interests.txt"
    content = [line.strip('\n') for line in open(fname)]

    p_interests = {}
    for line in content:
        tmp = line.split(" : ")
        interests = [each.lower() for each in tmp[1].split()]
        p_interests[tmp[0]] = interests

    return p_interests


def find_common():
    title, key_interests = find_interests()
    interests = people_interests()

    for pers in interests:
        common = set(key_interests).intersection(interests[pers])
        interests[pers] = len(common)

    return interests


def compute_rating():
    influence = dict(compute_influence())
    common = find_common()

    promoters = {}
    for infl in influence:
        rating = influence[infl] * 0.2 * common[infl]
        promoters[infl] = rating

    promo = sorted(promoters.items(), key=itemgetter(1), reverse=True)
    return promo


################################################################################

print("The top 5 to promote my book:\n")

to_print = "%-20s%12s" % ("Name", "Rating")
print(to_print + "\n" + ("-" * len(to_print)))

promo = compute_rating()
for index in range(5):
    print("%-20s|%10.3f" % (promo[index][0], promo[index][1]))

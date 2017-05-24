################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex5  |--#
################################################################################

import nltk
import json as js
from operator import itemgetter

tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]
distribution = dict(nltk.FreqDist(words))
setwords = list(set(words))

start = str(input("Enter anything: ")).lower()

word_starts_with = [x for x in setwords if x.startswith(start)]

if word_starts_with == []:
    print("No such words found.")
    exit()

ret = [(x, distribution[x]) for x in word_starts_with]
sort = sorted(ret, key=itemgetter(1), reverse=True)[:3]

print("Predicted words:")
for i, item in enumerate(sort, 1):
    print("%d : %-15s | %-2d (times)" % (i, item[0], item[1]))

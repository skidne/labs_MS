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

# reusing the code from the previous exercises #
tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]
distribution = dict(nltk.FreqDist(words))
setwords = list(set(words))

start = str(input("Enter anything: ")).lower()

# finds words that start with the entered substring #
wordStartsWith = [x for x in setwords if x.startswith(start)]

if wordStartsWith == []:
    print("No such words found.")
    exit()

# makes a new list of tuples: (word, nr. of times it was encountered) and sorts it#
ret = [(x, distribution[x]) for x in wordStartsWith]
sort = sorted(ret, key=itemgetter(1), reverse=True)[:3]

# printing the results #
print("Predicted words:")
for i, item in enumerate(sort, 1):
    print("%d : %-15s | %-2d (times)" % (i, item[0], item[1]))

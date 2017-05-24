################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex2  |--#
################################################################################

import nltk
import json as js

tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]

tagged = nltk.pos_tag(words)

nouns = [x[0] for x in tagged if x[1] == 'NN' and x[0].isalpha()]

distribution = nltk.FreqDist(nouns).most_common(10)

print("Most common nouns:")
for i, item in enumerate(distribution, 1):
    print("%-2d : %-8s | %-3d (times)" % (i, item[0], item[1]))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex2  |--#
################################################################################

import nltk
import json as js

# reusing the code from the previous problem #
tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]

# tags all words #
tagged = nltk.pos_tag(words)

# finds only nouns #
nouns = [x[0] for x in tagged if x[1] == 'NN' and x[0].isalpha()]

# most common nouns #
distribution = nltk.FreqDist(nouns).most_common(10)

# printing the results #
print("Most common nouns:")
for i, item in enumerate(distribution, 1):
    print("%-2d : %-8s | %-3d (times)" % (i, item[0], item[1]))

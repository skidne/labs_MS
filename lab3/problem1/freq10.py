################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex1  |--#
################################################################################

import nltk
import json as js

# opens the tweets.json doc and reads it #
tw = js.loads(open("../tweets.json").read())

# splits all tweets into words #
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]

# finds the 10 most common words #
dist = nltk.FreqDist(words).most_common(10)

# printing the results #
print("Most common words:")
for i, item in enumerate(dist, 1):
    print("%-2d : %-6s | %-4d (times)" % (i, item[0], item[1]))

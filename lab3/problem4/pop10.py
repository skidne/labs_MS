################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex4  |--#
################################################################################

import nltk
import json as js
from operator import itemgetter

def foreachN(nouns, info, freq):
    ret = []
    for i in nouns:
        likes = 0; retweets = 0
        for j in info:
            if i in j[0]:
                likes += j[1]; retweets += j[2]
        rating = round(freq[i] * (1.4 + retweets) * (1.2 + likes))
        ret.append((i, rating))
    # a really nice way to sort a list of tuples with respect to a certain #
    # element in each tuple, found on stackoverflow #
    return sorted(ret, key=itemgetter(1), reverse=True)

################################################################################

# reusing the code from the previous exercises #
tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]
nouns = [x[0] for x in nltk.pos_tag(words) if x[1] == 'NN' and x[0].isalpha()]

# transforming a list of tuples of words and their frequencies to a dictionary #
freq = dict(nltk.FreqDist(nouns))

# eliminating any repeating nouns #
nouns = list(set(nouns))

# list of tuples with 3 elements: 1 - a list with distinct words in a tweet #
# 2 - int value of likes in a tweet, 3 - int value of retweets in a tweet #
info = [(list(set(x['text'].lower().split())), int(x['likes']), int(x['retweets'])) for x in tw]

# a sorted list of tuples: (1 - a noun, 2 - rating); sliced up to 10 #
pop10 = foreachN(nouns, info, freq)[:10]

# printing the results #
print("Most popular nouns:")
for i, item in enumerate(pop10, 1):
    print("%-2d : %-10s | %-13d (popularity)" % (i, item[0], item[1]))

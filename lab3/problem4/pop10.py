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

def foreach_noun(nouns, info, freq):
    ret = []
    for noun in nouns:
        likes = 0
        retweets = 0
        for inf in info:
            if noun in inf[0]:
                likes += inf[1]
                retweets += inf[2]
        rating = round(freq[noun] * (1.4 + retweets) * (1.2 + likes))
        ret.append((noun, rating))
    return sorted(ret, key=itemgetter(1), reverse=True)


################################################################################

tw = js.loads(open("../tweets.json").read())
words = [y for x in tw for y in x['text'].lower().split() if y.isalpha()]
nouns = [x[0] for x in nltk.pos_tag(words) if x[1] == 'NN' and x[0].isalpha()]

freq = dict(nltk.FreqDist(nouns))

nouns = list(set(nouns))

# list of tuples with 3 elements: 1 - a list with distinct words in a tweet #
# 2 - int value of likes in a tweet, 3 - int value of retweets in a tweet #
info = [(list(set(x['text'].lower().split())), int(x['likes']), int(x['retweets']))
    for x in tw]

# a sorted list of tuples: (1 - a noun, 2 - rating); sliced up to 10 #
pop10 = foreach_noun(nouns, info, freq)[:10]

print("Most popular nouns:")
for i, item in enumerate(pop10, 1):
    print("%-2d : %-10s | %-13d (popularity)" % (i, item[0], item[1]))

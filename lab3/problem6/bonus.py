################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex6  |--#
################################################################################

import nltk
import json as js

def findWord2(word1, tw):
    ret = []
    for i in tw:
        tmp = i['text'].lower().split()
        for j in range(len(tmp)):
            if tmp[j] == word1 and j + 1 < len(tmp):
                ret.append(tmp[j + 1])
    return ret

################################################################################

# reusing the code from the previous exercises #
tw = js.loads(open("../tweets.json").read())
word1 = str(input("Enter anything: ")).lower()

# finds words that follow the word1 in the tweets #
occurences = findWord2(word1, tw)
if occurences == []:
    print("Occurences not found.")
    exit()

# the most common occurences #
freq = nltk.FreqDist(occurences).most_common(3)

# printing the results #
print("Occurences:")
for i, item in enumerate(freq, 1):
    print("%d : %-10s | %-3d (times)" % (i, item[0], item[1]))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB3--ex3  |--#
################################################################################

import nltk
import datetime as dt, time
import matplotlib.pyplot as plt
import json as js, numpy as np

def cnt_word(word, sent):
    # finds the last day of a given month and replaces the time #
    def get_last_day(begin):
        nextM = begin.replace(day=28, hour=23, minute=59, second=59) + dt.timedelta(days=4)
        return nextM - dt.timedelta(days=nextM.day)

    all_wrd = [x[1] for x in sent if word in x[0]]
    if all_wrd == []:
        return []
    # reversing to have ascending dates #
    all_wrd.reverse()
    # a little bit ugly, but it's working #
    cnt = 1
    begin = all_wrd[0]
    end = get_last_day(begin)
    ret = []
    for i in all_wrd:
        if i <= end: cnt += 1
        else:
            ret.append([cnt, begin.year, begin.month])
            begin = i
            end = get_last_day(begin)
            cnt = 1
    # for the last elements that didn't append in the loop (didn't enter 'else') #
    if len(all_wrd) > sum(x[0] for x in ret):
        ret.append((cnt - 1, all_wrd[-1].year, all_wrd[-1].month))
    return ret


def plotbar(word, thatword):
    # simplifying the labels with dates on x-axis #
    labels = [str(dt.datetime(x[1], x[2], 1))[:7] for x in word if x[0] > 0]
    data = [x[0] for x in word if x[0] > 0]
    xlocations = np.array(range(len(data)))
    plt.bar(xlocations, data, width=1)
    plt.title("Frequency bar chart for the word" + thatword)
    plt.ylabel("Number of times encountered")
    plt.xticks(xlocations + 0.5, labels, rotation=30)
    plt.show()

################################################################################

# reusing the code from the previous exercises #
tw = js.loads(open("../tweets.json").read())

# sent a list of tuples: 1 - tweet, 2 - creation date of tweet #
sent = list(map(lambda x:
    (x['text'].lower(),
    # got rid of the utc, cuz it was problematic to work with #
    dt.datetime.strptime(x['created_at'][:19], "%Y-%m-%d %H:%M:%S")), tw))

word = " " + str(input("Enter a word: ")).lower() + " "

# a list of tuples with 3 elements: 1 - frequency of the word in a month, #
# 2 - the year, 3 - the month #
all_wrd = cnt_word(word, sent)

if all_wrd != []:
    print("Plotting the bar chart...")
    plotbar(all_wrd, word)
else:
    print("No such words found.")

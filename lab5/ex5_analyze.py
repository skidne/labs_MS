################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB5--ex5  |--#
################################################################################

def find_interests():
    fname = "./interests.txt"
    interests = [line.strip('\n').lower() for line in open(fname)]

    title = "From T-Rex to Justin Bieber: How Internet has changed the Politics, Art and cute Cats"
    separators = ",./?:;"
    keywords = [word.strip(separators).lower() for word in title.split()]

    specter_interest = set(interests).intersection(keywords)

    return title, specter_interest


################################################################################

if __name__ == "__main__":
    red = '\033[91m'
    ok = '\033[0m'

    title, specter = find_interests()
    print("The title \"%s\" has the following specter of interests:" % title)
    for interest in specter:
        print(interest.title(), end="")
        if interest == 'bieber':
            print(red + "\tDISCLAIMER: \"Bieber\" and \"Music\" are not related." + ok)
        else:
            print("")

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------| LAB5  start |--#
################################################################################

def take_matrix():
    fname = "./list.txt"
    content = [line.strip('\n ') for line in open(fname)]
    people = content.pop(0).split(' | ')
    matrix = []

    for line in content:
        connections = [int(word) for word in line.split() if word.isdigit()]
        matrix.append(connections)

    sum_line = [sum(line) for line in matrix]
    return (people, matrix, sum_line)

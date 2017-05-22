################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB5--ex3  |--#
################################################################################

import start
from operator import itemgetter

def find_min_dist(dist, queue):
    min_index = -1
    min_elem = float("Inf")

    for ind in range(len(dist)):
        if dist[ind] < min_elem and ind in queue:
            min_index = ind
            min_elem = dist[ind]
    return min_index


def dijkstra(matrix, node, rows):
    distance = [float("inf")] * rows
    prev = [-1] * rows
    distance[node] = 0
    queue = [row for row in range(rows)]

    while queue:
        vertex_u = find_min_dist(distance, queue)
        queue.remove(vertex_u)

        for col in range(rows):
            if matrix[vertex_u][col] and col in queue:

                if distance[vertex_u] + matrix[vertex_u][col] < distance[col]:
                    distance[col] = distance[vertex_u] + matrix[vertex_u][col]
                    prev[col] = vertex_u

    return distance


def find_rating(dist):
    list_points = [(points - 1) for points in dist if points > 0]
    return sum(list_points)


def print_sol(ratings):
    to_print = "%-20s%13s" % ("Name", "Rating")
    print(to_print + "\n" + ("-" * len(to_print)))

    for one in ratings:
        print("%-20s|%10d" % one)


def main():
    info = start.take_matrix()

    people = info[0]
    adj_matrix = info[1]

    len_matrix = len(adj_matrix)
    raw = {}
    for node in range(len_matrix):
        dist = dijkstra(adj_matrix, node, len_matrix)
        raw[people[node]] = find_rating(dist)

    ratings = sorted(raw.items(), key=itemgetter(1))
    print_sol(ratings)


################################################################################

if __name__ == "__main__":
    main()

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB1--ex2  |--#
################################################################################

from random import randint

def find_procent(spin, adjacent, maxi):

	def non_adjacent(bullet1):
		bullet2 = randint(0, maxi)
		if bullet2 is bullet1 - 1 or bullet2 is bullet1 or bullet2 is bullet1 + 1:
			bullet2 = non_adjacent(bullet1)
		return bullet2

	def put_current_slot():
		current = randint(0, maxi)
		before_curr = current - 1
		if before_curr == -1:
			before_curr = maxi
		if before_curr is bullet1 or before_curr is bullet2:
			current = put_current_slot()
		return current


	dead = 0
	bullet1 = 0; bullet2 = 0
	for i in range(1000):
		bullet1 = randint(0, maxi)
		bullet2 = bullet1 - 1 if adjacent else non_adjacent(bullet1)
		if bullet2 is -1:
			bullet2 = maxi
		current = put_current_slot()
		if spin:
			current = randint(0, maxi)
		if current is bullet1 or current is bullet2:
			dead += 1
		i += 1
	return (1 - dead / 1000) * 100

print("1) 6-slot barrel:")
print("\tadjacent bullets:\tnospin:\tP = %.1f%%" % find_procent(0, 1, 5))
print("\t\t\t\tspin:\tP = %.1f%%" % find_procent(1, 1, 5))
print("\tnon-adjacent bullets:\tnospin:\tP = %.1f%%" % find_procent(0, 0, 5))
print("\t\t\t\tspin:\tP = %.1f%%" % find_procent(1, 0, 5))
print("2) 5-slot barrel:")
print("\tadjacent bullets:\tnospin:\tP = %.1f%%" % find_procent(0, 1, 4))
print("\t\t\t\tspin:\tP = %.1f%%" % find_procent(1, 1, 4))
print("\tnon-adjacent bullets:\tnospin:\tP = %.1f%%" % find_procent(0, 0, 4))
print("\t\t\t\tspin:\tP = %.1f%%" % find_procent(1, 0, 4))

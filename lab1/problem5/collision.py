################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB1--ex5  |--#
################################################################################

from hashlib import md5
from random import randint
from uuid import uuid4

# be careful, this program is slow as f$$$ #

success = '\033[92m'
reset = '\x1b[0m'

print("Generating random inputs...")

nr = 0
while 1:
    inp = str(uuid4())
    collision = inp + str(randint(0, 4000))
    hashed_input = md5(inp.encode()).hexdigest()
    hashed_coll = md5(collision.encode()).hexdigest()
    if hashed_coll.startswith(hashed_input[:10]):
        break
    nr += 1

# if you're lucky, this program will exit this loop

print(success, "Collision!", reset)
print("Number of attempts = {}".format(nr))
print("first input - [{}] ; hash - [{}]".format(inp, hashed_input))
print("collision input - [{}] ; hash - [{}]".format(collision, hashed_coll))

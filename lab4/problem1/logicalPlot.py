################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB4--ex1  |--#
################################################################################

import numpy as np
import matplotlib.pyplot as plt

def switch(case):
    return {
    '1' : np.logical_xor(mat_x < 0, R > 100),
    '2' : np.logical_and(np.logical_or(R > 100, mat_y > 0), np.logical_or\
    (R < 100, mat_x > 0)),
    '3' : np.logical_not(np.logical_xor(mat_y < 0, mat_x < 0)),
    '4' : np.logical_or(R < nx / 2, np.logical_xor(mat_y < 0, mat_x > 0)),
    '5' : np.logical_xor(mat_y > 0, R > nx / 2),
    '6' : np.logical_and(mat_x > 0, R > nx / 2)
    }.get(case)


################################################################################

nx = 1024
x = np.linspace(-nx / 2 , nx / 2 , nx)
mat_x, mat_y = np.meshgrid(x, x)
R = np.sqrt(mat_x ** 2 + mat_y ** 2)

case = input("Enter the number of the plot: ")
if not case.isdigit(): print("A number, NUMBER, N-U-M-B-E-R."); exit()
if 1 < int(case) > 6: print("It should be between 1 and 6."); exit()
filter = switch(case)

plt.imshow(filter, cmap='gray')
plt.show()

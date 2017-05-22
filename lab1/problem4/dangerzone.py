################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB1--ex4  |--#
################################################################################

from PIL import Image as img
from random import randint

def compute(im, cases):
	width, height = im.size
	red = (254, 0, 0)
	areaRed = 0
	for i in range(cases):
		pixel = (randint(0, width - 1), randint(0, height - 1))
		areaRed += 1 if im.getpixel(pixel) == red else 0
	return 42 * areaRed / cases


################################################################################

img_file = "forlab.jpeg"
im = img.open(img_file)
cases = 1000
print("The mined area has %.2f miles." % compute(im, cases))

################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB2--ex10 |--#
################################################################################

plants = 100
BlackMesaProbab = 0.001

# Binomial Distribution ->
# (100 choose 99) * P(Success)^99 * P(Failure) +
# (100 choose 98) * P(Success)^98 * P(Failure)^2 +
#   + ... +
# (100 choose 1) * P(Success) * P(Failure)^99 +
# (100 choose 100) * P(Failure)^100 =
# = 1 - [(100 choose 100) * P(Success)^100] #

probability = 1 - ((1 - BlackMesaProbab) ** plants)

print("The probability of at least one Black Mesa is %f" % probability)

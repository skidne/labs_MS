################################################################################
#---------------- ####### ---- ## ---- ####### --------------------------------#
#---------------- ## ------- ##--## ------- ## ---------------|   FAF-161   |--#
#---------------- ##### --- ######## --- ##### ---------------| Gore-Polina |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|             |--#
#---------------- ## ------ ## -- ## ------ ## ---------------|  LAB4--ex3  |--#
################################################################################

from itertools import product
import re

def check_expr(expr):

    def check_parent():
        par = 0
        for char in expr:
            if char == '(': par += 1
            elif char == ')': par -= 1
            if par < 0:
                return False
        return par == 0

    # this regex doesn't handle correctly the nested parentheses #
    pat = ("^\s*\(*\s*\!*\s*\(*\s*[a-zA-Z]{1}(?:\s*[+*]\s*"
            "(?:[)(]*\s*\!*\s*[)(]*\s*[a-zA-Z]{1})\s*[)(]*)*\s*\)*\s*$")
    # that's why we parse them separately #
    if re.match(pat, expr, re.I) and check_parent():
        lst = list(set([x for x in list(expr) if x.isalpha()]))
    else:
        print("Error: \'" + expr + "\' cannot be parsed.")
        exit()
    return sorted(lst)


def logic_eval(expr):
    new = expr.replace('!', ' not ').replace('*', ' and ').replace('+', ' or ')
    return eval(new)


def pprint(var, expr):
    cnt = 0
    for i in var:
        print(i, "| ", end="")
        cnt += 4
    print(expr)
    return cnt + len(str(expr))


################################################################################

expr = input("Enter a valid logic expression: ")
var = check_expr(expr)
rez = pprint(var, expr)
print('-' * rez)
for i in list(product([0, 1], repeat=len(var))):
    tmp_expr = expr
    for j in range(len(var)):
        tmp_expr = tmp_expr.replace(var[j], str(i[j]))
    pprint(i, int(logic_eval(tmp_expr)))

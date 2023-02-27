# Oscar Fernando López Barrios
# Carné 20679

from afn import *

text = "((a|b)|b*)"

afn = AFN(text)
print(afn.postfix_expression)
print(afn.transitions)
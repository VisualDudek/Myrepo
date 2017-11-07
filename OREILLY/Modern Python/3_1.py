#  Jeszcze raz do rozgryzienia
#  INFO Check PycharmHelp Followinf PEP484

from typing import *
from collections import OrderedDict

x = 10.0 # :type: int

x: List[int] = []

x = ['abc']

def f(x: int, y: int) -> int:
    return x + y

f(5, 10.0)

y = OrderedDict()  # type: OrderedDict

def g(x: List[int]) -> None:
    print(len(x))
    print(x[0])
    for i in x:
        print(i)

g([10, 20, 30])
g(['asdfg'])

hts = [97.1, 102.5, 97.5]          # type: List[float]
person = ('Raymond', 5 * 12 + 11)  # type: Tuple[str, float]
info = ('Peatson','Course','Python', 10 ) # type: Tuple[str, ...]


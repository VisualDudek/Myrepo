
#  INFO Check PycharmHelp Followinf PEP484

from typing import *
from collections import OrderedDict

x = 10.0  # :type : str
x = 12.0

def f(x: int, y: int) -> int:
    return x + y

f(5, 10.0)

y = OrderedDict()  # type: OrderedDict

def g(x: list[int]) -> None:
    print(len(x))
    print(x[0])
    for i in x:
        print(i)

g([10, 20, 30])
g(['asdfg'])

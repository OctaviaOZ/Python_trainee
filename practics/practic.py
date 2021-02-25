#!/usr/bin/env python
# coding: utf-8
# import numpy as np
# import math
# x = 'first'
# y = x
# print(id(x))
# print(id(y))
# y += 'bar'
# print(id(x))
# print(id(y))
# x = [1,2,3]
# y = x
# y += [4,5,6]
# print(x)
#
# print(y+3)
from itertools import islice

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f = fib()
print(list(islice(f, 0, 10)))








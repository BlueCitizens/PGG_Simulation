# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 18:05
# @Author  : Xiangyu Dai
# @Email   : bluecitizens@163.com
# @File    : tools.py
# @Software: PyCharm
import itertools
import random
import numpy as np


# Generating a number with the power of 10 ** (-x).
def gen_step(x=3):
    num = 0
    for i in range(x):
        num += random.randint(1, 9) * 10 ** (-(i + 1))
    return num


# The function intended to generate random h1,h2 possible pairs in the power of 10 ^ -3
# as the lowest possible number the relevant.
def gen_steps():
    x, y = 0, 0
    while x in [1, 0] or y in [1, 0] or x == y:
        x = gen_step()
        y = gen_step()
    return (x, y) if x < y else (y, x)


def gen_h1_h2_possible_pairs():
    # All possible pairs of h1, h2 where h1 > h2, h1 == h2 and h1 < h2.
    # The values are between 0.95 to 0.1 as an initial trust with 0.05 as the step.
    return list(itertools.product(np.arange(0.95, 0.1, -0.05).round(2), np.arange(0.95, 0.1, -0.05).round(2)))


if __name__ == '__main__':
    # possible values
    for i in range(30):
        print(gen_steps())

    print(gen_h1_h2_possible_pairs())
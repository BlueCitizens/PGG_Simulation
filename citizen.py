# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 18:05
# @Author  : Xiangyu Dai
# @Email   : bluecitizens@163.com
# @File    : citizen.py
# @Software: PyCharm

"""
The class represents the general citizen for the regular Public Good Game (without Blockchain).
"""
import random


class Citizen():
    def __init__(self):
        self.trust = 0.85  # init Trust?
        self.money = []

    def set_steps(h1, h2):
        self.h1 = h1
        self.h2 = h2

    '''
    The function determines whether to invest the money on the shared account or not.
    It depends on the parameters: epsilon, irrationality, and trust. 
    '''

    def to_invest(self):
        # [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        epsilon = [1] * 9 + [0] * 1
        # [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        irrationality = [1] * 7 + [0] * 3
        return self.trust > random.random() and random.choice(epsilon) == 1 and random.choice(irrationality) == 1

    '''
    On future implementations, we can randomize the trust of each citizen instead of being equal.
    '''

    def randomize_trust(self):
        self.trust = random.random()
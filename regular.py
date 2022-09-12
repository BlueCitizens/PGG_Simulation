# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 18:19
# @Author  : Xiangyu Dai
# @Email   : bluecitizens@163.com
# @File    : regular.py
# @Software: PyCharm
import numpy as np
from citizen import Citizen as Citizen
import gol
import pandas as pd

if __name__ == '__main__':
    #  A computer simulation of the regular Public Good Game,
    # following the result of human simulation on the literature.

    gol.set_value("test", 1)
    CITY_NUM = gol.get_value("CITY_NUM")
    MONEY_EACH_DAY = gol.get_value("MONEY_EACH_DAY")
    INVEST_RATE = gol.get_value("INVEST_RATE")
    h1_h2_possible_pairs = gol.get_value("h1_h2_possible_pairs")

    # dict of mean trust under different initial trust, h1 and h2
    trust_lines = {}
    charity_profit = {}
    # Running the model on different initial trusts from 0.95 to 0.1.
    for initial_trust in np.arange(0.95, 0.1, -0.05):
        for h1, h2 in h1_h2_possible_pairs:
            city = [Citizen() for i in range(CITY_NUM)]
            # setting the same initial trust for all the citizen/agents/players.
            for c in city:
                c.trust = initial_trust

            mean_trust = [initial_trust]
            profit = [0]
            # Each initial trust has 1000 game iterations, i.e. rounds.
            for i in range(1000):
                invest = []
                not_invest = []
                for citizen in city:
                    if not citizen.to_invest():
                        not_invest.append(citizen)
                    else:
                        invest.append(citizen)
                # C-3PO get 1/6 of the fund's total
                charity_prof = (MONEY_EACH_DAY * len(invest))
                # Each citizen share the remaining fund evenly
                shared_profit = ((INVEST_RATE * MONEY_EACH_DAY * len(invest)) - charity_prof) / CITY_NUM

                # record trusts of all players in this round, meant to calculate the mean trust
                trusts = []
                # Updating the trust either up or down according to the rules.

                # Trust increase
                if charity_prof > profit[-1] or charity_prof == (MONEY_EACH_DAY * CITY_NUM):
                    for citizen in city:
                        citizen.trust = min(citizen.trust + h1, 1.0)
                        trusts.append(citizen.trust)
                # Trust decrease
                else:
                    for citizen in city:
                        citizen.trust = max(citizen.trust - h2, 0.00)
                        trusts.append(citizen.trust)
                # Updating the profit of each one of the players at the end of the round.
                for citizen in invest:
                    citizen.money.append(shared_profit)
                for citizen in not_invest:
                    citizen.money.append(MONEY_EACH_DAY + shared_profit)
                mean_trust.append(np.mean(trusts))
                profit.append(charity_prof)
            trust_lines[(initial_trust, h1, h2)] = mean_trust
            charity_profit[(initial_trust, h1, h2)] = profit[1:]
    data = pd.DataFrame.from_dict(trust_lines, orient='index')
    data.index = pd.MultiIndex.from_tuples(data.index, names=['initial_trust', 'h1', 'h2'])
    charity = pd.DataFrame.from_dict(charity_profit, orient='index')
    charity.index = pd.MultiIndex.from_tuples(charity.index, names=['initial_trust', 'h1', 'h2'])

    data.index = pd.MultiIndex.from_tuples(data.index, names=['initial_trust', 'h1', 'h2'])
    print(data)

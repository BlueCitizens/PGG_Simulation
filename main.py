# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from citizen import Citizen as Citizen


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # for initial_trust in np.arange(0.95, 0.1, -0.05).round(2):
    #     print(initial_trust)

    # pairs = []
    # for i in range(10):
    #     for j in range(10):
    #         pairs.append((i, j))
    #
    # print(pairs)
    #
    # for h1, h2 in pairs:
    #     print(h1, h2)

    CITY_NUM = 10
    initial_trust = 0.95
    h1, h2 = (0.95, 0.95)

    city = [Citizen() for i in range(CITY_NUM)]

    print(city)

    for c in city:
        c.trust = initial_trust

    mean_trust = [initial_trust]

    epsilon = [1] * 7 + [0] * 3
    print(epsilon)

    profit = [0, 1, 2]

    print(profit[1:4])

    test = {}

    test[(0, 0, 0)] = 1
    test[(0, 0, 1)] = 2
    test[(0, 0, 2)] = 3
    test[(0, 1, 0)] = 4

    print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

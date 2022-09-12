# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 11:43
# @Author  : Xiangyu Dai
# @Email   : bluecitizens@163.com
# @File    : gol.py
# @Software: PyCharm
import tools

# -*- coding: utf-8 -*-
_global_dict = {}


def _init():  # 初始化
    global _global_dict


def set_value(key, value):
    # 定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    # 获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except KeyError:
        print('读取' + key + '失败\r\n')


_init()
set_value("CITY_NUM", 10)
set_value("MONEY_EACH_DAY", 10)
set_value("INVEST_RATE", 6)
set_value("h1_h2_possible_pairs", tools.gen_h1_h2_possible_pairs())

if __name__ == '__main__':
    print(__name__)
import random
from functools import reduce
import random


class flow:
    # 所有随机生成的周期流的开始时间均是0时刻，时隙是事先设定好的
    def __init__(self, name, period, priority, start_time, slot):
        self.name = name
        self.period = period
        self.priority = priority
        self.start_time = start_time
        # self.end_time = end_time
        self.slot = slot  # 流的传输时间，即时隙
        self.ready = False
        self.next_deadline = start_time + period


# TODO:此函数用于计算流的超周期
def get_lcm(L):
    def lcm(a, b):
        gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
        return a * b // gcd(a, b)

    return reduce(lcm, L)


# TODO:随机生成一个流的集合
def  random_get_TT(TTFlow_num: int):
    TTFlow = []  # TT流集合
    periods = []  # 用于计算超周期
    TT_period = [10, 20, 30]  # TT流可能生成的周期
    TT_priority = [1, 2, 3]  # 可能的优先级
    TT_slot = [2, 3, 5]  # TT流时隙的选择可能
    for i in range(TTFlow_num):
        period = random.choice(TT_period)  # 随机选择一个流的周期
        if period not in periods:
            periods.append(period)
        # 向流列表中加入新的元素
        TTFlow.append(
            flow(
                i,
                period,
                random.choice(TT_priority),
                0,
                random.choice(TT_slot)
            )
        )
    hp = periods[0]
    if len(periods) > 1:
        hp = get_lcm(periods)

    return TTFlow, hp

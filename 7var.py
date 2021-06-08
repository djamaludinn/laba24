#!/usr/bin/env python3
# -*- config: utf-8 -*-

#Вариант 7

import math
from threading import Thread


def sm_first(x, n):
    return ((-1) ** (n + 1) * math.sin(n) * x) / n


def first(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_first(x, n)
    n += 1
    test = x / 2

    while math.fabs(current - previous) > eps:
        previous = current
        current = current + sm_first(x, n)
        n += 1
        # print(n)

    current = round(current, 6)
    test = round(test, 6)
    print(f'Сумма ряда {current} ~ проверочному значению {test}')



if __name__ == '__main__':
    th1 = Thread(target=first(-(math.pi/2), 1))

    th1.start()


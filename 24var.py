#!/usr/bin/env python3
# -*- config: utf-8 -*-

#Вариант 24

import math
from threading import Thread



def sm_first(x, n):
    return math.cos(n*x)*n/(4*(n**2)-1)


def first(x, n):
    n = n
    x = x
    eps = 1.0E-7
    previous = 0

    current = sm_first(x, n)
    n += 1
    test = - 1/4 - ((1 / 4) * math.cos(x/2) * (math.log(math.tan(x/4))))

    while math.fabs(math.fabs(current) - math.fabs(previous)) > eps:
        previous = current
        current = current + sm_first(x, n)
        n += 1
        print(current)

    current = round(current, 6)
    test = round(test, 6)
    print(f'Сумма ряда {current} ~ проверочному значению {test}')


if __name__ == '__main__':
    th1 = Thread(target=first(math.pi/6, 1))


    th1.start()

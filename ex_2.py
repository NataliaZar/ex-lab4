#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2
print('list: ', ' '.join(map(str, Unique(data1))))
print('random: ', ' '.join(map(str, Unique(data2))))
print('list ignore_case=False: ', ' '.join(map(str, Unique(data3))))
print('list ignore_case=True: ', ' '.join(map(str, Unique(data3, ignore_case='True'))))


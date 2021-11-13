import itertools as itt
import numpy as np
import timeit

inp = [int(i) for i in open('input.txt')]

# slow and ugly bruteforce not vecotrized
def bruteforce():
    for a, b in itt.combinations(inp, r=2):
        if a + b == 2020:
            # print(f'a:{a}, b:{b}, a*b:{a*b} ')
            return a, b, a*b
print(bruteforce())


# lets do something fancier to flex to Rich
def cuteforce():
    up = np.asarray(inp)
    up.sort()
    down = up[::-1]
    while True:
        idx = np.argwhere(up + down == 2020)
        if idx.size !=0: #found
            u, d = up[idx], down[idx]
            # print(f'u:{u}\nd:{d}\nu*d:{u*d}')
            return u[0], d[0], u[0]*d[0]
        down = np.roll(down,1)
print(cuteforce())


brute_time = timeit.timeit(bruteforce, number=1000)
cute_time = timeit.timeit(cuteforce, number=1000)

print(f'bruteforce:{brute_time}, cuteforce:{cute_time}, improvement:{cute_time/brute_time} times slower!'
      f'\n no wonder I dont get anything done in the lab')

# enough of this nonsense, part 2, back to business

for a, b, c in itt.combinations(inp, r=3):
    if a + b + c == 2020:
        print(f'a:{a}, b:{b}, c:{c} a*b*c:{a*b*c} ')

import numpy as np
import matplotlib.pyplot as plt
import re

with open('input.txt') as file:
    rules = dict()
    for ll, line in enumerate(file):
        if ll == 0:
            primer = line.strip()
        elif ll == 1:
            continue
        else:
            key, val = line.strip().split(' -> ')
            rules[key] = val


start = primer
ngens = 40

for gen in range(ngens):
    print(f'working step {gen+1}')

    triplets = list()
    for i in range(len(start)-1):
        pair = start[i:i+2]
        triplets.append(pair[0] + rules[pair] + pair[1])

    out = ''
    for tt, trip in enumerate(triplets):
        if tt == 0:
            out += trip
        else:
            out += trip[1:]

    # print(f'After step {gen+1}: {out}')
    start = out

out = np.asarray(list(out))

unique, count = np.unique(out,return_counts=True)

print(count.max() - count.min())

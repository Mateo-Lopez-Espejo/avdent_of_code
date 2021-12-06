import numpy as np

with open('input.txt') as file:
    coor_vctrs = list()
    for line in file:
        start, end = line.split('->')
        start = [int(s) for s in start.split(',')]
        end = [int(e) for e in end.split(',')]

        start.extend(end)
        coor_vctrs.append(start)

coor_vctrs = np.asarray(coor_vctrs)


# part 1

horizontal = coor_vctrs
subset = coor_vctrs
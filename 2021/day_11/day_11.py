import numpy as np
import itertools as itt


with open('test.txt') as file:
    octopus = list()
    for line in file:
        octopus.append([int(c) for c in line.strip()])

    octopus = np.asarray(octopus)


# gete slicers to find inmediate neigbor
lx, ly = octopus.shape
shifts = [np.s_[x:lx+x, y:ly+y] for x,y in itt.product([0,1,2],repeat=2) if not (x==1 and y==1) ]



for gen in range(1):
    # 1. increase all by 1 and check for flashing octopi
    octopus += 1

    flash_induced = np.full_like(octopus, False)

    changing = True
    while changing:
        flashed = np.full(np.asarray(octopus.shape)+2, False)
        flashed[1:-1, 1:-1] = octopus > 9

        for shift in shifts:
            octopus = octopus + flashed[shift]

        flash_induced = np.logical_and((octopus > 9), ~flashed[1:-1, 1:-1])

        if np.all(flash_induced == flashed[1:-1, 1:-1]):
            changing = False



        print(octopus)
        print((octopus>9).astype(int))

    octopus[octopus > 9] = 0



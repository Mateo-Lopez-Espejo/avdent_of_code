import numpy as np
import itertools as itt


with open('input.txt') as file:
    octopus = list()
    for line in file:
        octopus.append([int(c) for c in line.strip()])

    octopus = np.asarray(octopus)


# gete slicers to find inmediate neigbor
lx, ly = octopus.shape
shifts = [np.s_[x:lx+x, y:ly+y] for x,y in itt.product([0,1,2],repeat=2) if not (x==1 and y==1) ]


nsteps = 100
step_flashes = np.full((nsteps,) + octopus.shape, False)
step = 0

while True:
    # print(f'generation: {step}')
    # print(octopus)

    # 0. initializes the memory of cumulative flashes and some utility padding
    cumulative_flash = np.full(np.asarray(octopus.shape) + 2, False)
    pad_flash = np.full(np.asarray(octopus.shape) + 2, False)

    # 1. increase all by
    octopus += 1

    # primes the systems with the first round of flashes
    just_flashed = octopus > 9

    # keeps updating the octopy as long as there are no new flashes
    while True:
        # tracks the cumulative flashes so octopi dont stimulate others more than one
        cumulative_flash[1:-1, 1:-1] = np.logical_or(just_flashed, cumulative_flash[1:-1, 1:-1])

        # looks at adyacent octopy and adds one if flashed
        pad_flash[1:-1, 1:-1] = just_flashed
        for shift in shifts:
            octopus = octopus + pad_flash[shift]

        # updates any newly stimulated octopi for the next round of iteration
        just_flashed = np.logical_and((octopus > 9), ~cumulative_flash[1:-1, 1:-1])

        if np.all(~just_flashed):
            # terminates feed forward loop if no induced flashes
            break

        # print(octopus)
        # print((octopus>9).astype(int))

    # set tired octopi at rest
    octopus[octopus > 9] = 0

    # part 1
    # saves flashes for this step
    if step < nsteps:
        step_flashes[step, ...] = cumulative_flash[1:-1, 1:-1]
    elif step == nsteps:
        print(f'number of octopi flashes {np.sum(step_flashes)}')

    # part 2
    else:
        if np.all(cumulative_flash[1:-1, 1:-1]):
            print(f'number of steps to syncrhonization; {step+1}')
            break

    step += 1

import numpy as np
import matplotlib.pyplot as plt

with open('input.txt') as file:
    coor_vctrs = list()
    for line in file:
        start, end = line.split('->')
        start = [int(s) for s in start.split(',')]
        end = [int(e) for e in end.split(',')]

        start.extend(end)
        coor_vctrs.append(start)


# array with shape Lines x Coordinates, where Coordinates dimension has positions: x0,y0,x1,y1
coor_vctrs = np.asarray(coor_vctrs)

# transforms coordinates into grid positions
# init grid stack for speed
grid_stack = np.zeros((coor_vctrs.shape[0],               # coords
                       np.max(coor_vctrs[:,[0,2]])+1,     # x
                       np.max(coor_vctrs[:,[1,3]])+1))    # y

for vv, vctr in enumerate(coor_vctrs):
    # here is the magic, transforms the coordinates into vector indices
    x = np.linspace(vctr[0], vctr[2], np.abs(vctr[0]-vctr[2])+1, endpoint=True).astype(int)
    y = np.linspace(vctr[1], vctr[3], np.abs(vctr[1]-vctr[3])+1, endpoint=True).astype(int)
    # using vctr indices follow broadcast rules for numpy so if one vctr is a singleton broadcasts
    grid_stack[vv,x,y] = 1


# part 1
vert = coor_vctrs[:, 0] == coor_vctrs[:, 2]
hori = coor_vctrs[:, 1] == coor_vctrs[:, 3]

subset = grid_stack[vert | hori, ...]

overlaps = np.sum(subset, axis=0)
danger_zone_count = np.sum(overlaps>=2)
print(f'there is {danger_zone_count} DANGER ZONES!')


# part 2
overlaps = np.sum(grid_stack, axis=0)
danger_zone_count = np.sum(overlaps>=2)
print(f'even more!:{danger_zone_count} DANGER ZONES!')


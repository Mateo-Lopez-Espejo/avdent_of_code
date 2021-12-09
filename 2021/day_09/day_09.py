import numpy as np
import seaborn as sns


# with open('input.txt') as file:
with open('test.txt') as file:
    floormap = list()
    for line in file:
        floormap.append([int(i) for i in line.strip()])
    floormap = np.asarray(floormap)


padded = np.full(np.asarray(floormap.shape)+2, 10)
padded[1:-1, 1:-1] = floormap
islow = np.zeros_like(floormap).astype(bool)


# part 1
lows_sum = 0
for index in np.ndindex(floormap.shape):
    pad_index = np.asarray(index) + 1
    neighbour = {'up'    : padded[pad_index[0]-1, pad_index[1]],
                 'down'  : padded[pad_index[0]+1, pad_index[1]],
                 'left'  : padded[pad_index[0], pad_index[1]-1],
                 'right' : padded[pad_index[0], pad_index[1]+1]}

    neigh_vctr = np.asarray([v for v in neighbour.values()])

    if np.all(neigh_vctr > floormap[index]):
        lows_sum += floormap[index] + 1
        islow[index] = True

# sns.heatmap(islow,)

print(lows_sum)


# part 2
padded = np.full(np.asarray(floormap.shape)+2, 9)
padded[1:-1, 1:-1] = floormap
basin_map = np.full_like(padded, 0)
basin_map[padded == 9] = -1

basin_counter = 1

# has two make two passes, forwards and bakwards
# indices = list(np.ndindex(floormap.shape))
# indices = indices + indices[::-1]

for index in np.ndindex(floormap.shape):
    pad_index = np.asarray(index) + 1

    neig_idx = {'it'    : pad_index,
                'up'    : pad_index - [1, 0],
                'down'  : pad_index + [1, 0],
                'left'  : pad_index - [0, 1],
                'right' : pad_index + [0, 1]}

    arr_idx = np.asarray(list(neig_idx.values()))
    neig_idx = tuple(ii for ii in arr_idx.T)

    neigh_vctr = basin_map[neig_idx]


    if neigh_vctr[0] != -1:
        valid_idx = list()
        for vp in arr_idx:
            if basin_map[vp[0], vp[1]] != -1:
                valid_idx.append(vp)

        valid_idx = tuple(ii for ii in np.asarray(valid_idx).T)

        if min(basin_map[valid_idx]) == 0:
            basin_map[valid_idx] = basin_counter
            basin_counter += 1
        else:
            basin_map[valid_idx] = min(basin_map[valid_idx])

sns.heatmap(basin_map.astype(int), annot=True)




















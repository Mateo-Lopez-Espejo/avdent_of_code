import numpy as np

with open('input.txt') as file:
# with open('test.txt') as file:
    floormap = list()
    for line in file:
        floormap.append([int(i) for i in line.strip()])
    floormap = np.asarray(floormap)


padded = np.full(np.asarray(floormap.shape)+2, 9)
padded[1:-1, 1:-1] = floormap

# part 1
# movement relative to padded array
up, down, left, right = np.s_[1:-1,:-2], np.s_[1:-1,2:], np.s_[0:-2,1:-1], np.s_[2:,1:-1]
offsets = [up,down,left,right]

islow = np.full((4,)+floormap.shape, False)
for oo, offset in enumerate(offsets):
    islow[oo,...] = floormap < padded[offset]

islow = np.all(islow, axis=0)
print(f'sum risk of low points: {np.sum(floormap[islow]+1)}')

# part 2
# makes a map of basin sources and limits

edges = floormap == 9


basin_map = np.full_like(floormap, 0)
basin_map[floormap == 9] = -1
for nn, (xx, yy) in enumerate(np.argwhere(islow)):
    basin_map[xx, yy] = nn + 1

basin_pad = np.full(np.asarray(basin_map.shape)+2, -1)
basin_pad[1:-1, 1:-1] = basin_map

# inpired by rich.
changing = True
while changing:
    for offset in offsets:
        basin_map = np.maximum(basin_map, basin_pad[offset])
        basin_map[edges] = -1

    if np.all(basin_map == basin_pad[1:-1, 1:-1]):
        changing = False

    basin_pad[1:-1, 1:-1] = basin_map


basin_idx, basin_size = np.unique(basin_map[~edges], return_counts=True)
basin_size.sort()

print(np.prod(basin_size[-3:]))

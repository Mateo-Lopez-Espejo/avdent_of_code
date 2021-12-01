import numpy as np
with open('input.txt') as file:
    depths = np.asarray([int(line) for line in file])

# part 1
print(depths.shape, depths, )
print(f"measurmemetns greater than previous: {np.sum(np.diff(depths) > 0)}")

# part 2
windowed = np.stack([depths[i:i+3] for i in range(depths.size-2)], axis=0)
print(f"windowed greater than previous: {np.sum(np.diff(np.sum(windowed,axis=1)) > 0)}")
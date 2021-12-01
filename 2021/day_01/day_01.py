import numpy as np
import timeit
with open('input.txt') as file:
    depths = np.asarray([int(line) for line in file])

# part 1
print(depths.shape, depths, )
print(f"measurmemetns greater than previous: {np.sum(np.diff(depths) > 0)}")

# part 2
def non_vect():
    window_size = 3
    max_time = depths.size - window_size + 1
    windowed = np.stack([depths[i:i+window_size] for i in range(max_time)], axis=0)
    sum_increase = np.sum(np.diff(np.sum(windowed,axis=1)) > 0)
    return sum_increase

# alternative
def vect():
    window_size = 3
    max_time = depths.size - window_size + 1
    win_idx = (np.expand_dims(np.arange(window_size), axis=0) +
               np.expand_dims(np.arange(max_time), axis=1) )
    windowed = depths[win_idx]
    sum_increase = np.sum(np.diff(np.sum(windowed, axis=1)) > 0)
    return sum_increase

print(f"windowed greater than previous: {vect()}")



nv_time = timeit.timeit(non_vect, number=1000)
v_time = timeit.timeit(vect, number=1000)
print(f'non_vectorizes:{nv_time:.2f}, vectorized:{v_time:.2f}, improvement:{nv_time/v_time:.2f} times faster')


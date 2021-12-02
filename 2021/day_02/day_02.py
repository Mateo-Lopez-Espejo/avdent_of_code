import numpy as np

instructions = np.loadtxt('input.txt', dtype=object, delimiter=' ', usecols=0)
values = np.loadtxt('input.txt', dtype=int, delimiter=' ', usecols=1)

# part 1
forward = np.sum(values[instructions == 'forward'])
up_down = np.sum(values[instructions == 'down']) - np.sum(values[instructions == 'up'])

print(f'product horizontal position and depth: {forward * up_down}')

# part 2

aim, pos, depth = 0, 0, 0

for inst, val in zip(instructions, values):
    if inst == 'forward':
        pos += val
        depth += aim * val
    elif inst == 'up':
        aim -= val
    elif inst == 'down':
        aim += val
    else:
        print('wtf')
        break

print(f'product horizontal position and depth: {pos * depth}')


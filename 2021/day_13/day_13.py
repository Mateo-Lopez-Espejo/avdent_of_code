import numpy as np
import matplotlib.pyplot as plt

with open('input.txt') as file:
    coordinates = list()
    folds = list()
    for line in file:
        if line[0] == '\n':
            continue
        elif line[0] == 'f':
            _,_, fold = line.strip().split()
            folds.append(fold.split('='))
        else:
            coordinates.append(line.strip().split(','))

    coordinates = np.asarray(coordinates).astype(int)



def coords2sheet(coords):
    sheet = np.zeros((np.max(coords[:,1])+1, np.max(coords[:,0]+1)))
    sheet[(coords[:,1], coords[:,0])] = 1

    return sheet


def fold_along(coords, fold):
    direction = fold[0]
    mask = coords > int(fold[1])
    if direction == 'x':
        span = np.max(coords[:,0])
        mask[:,1] = False
    else:
        span = np.max(coords[:,1])
        mask[:,0] = False

    coords[mask] = span - coords[mask]

    return np.unique(coords, axis=0)


# part one
print(f'dots after first fold: {fold_along(coordinates, folds[0]).shape[0]}')

# part two
coords = coordinates
for fold in folds:
    coords = fold_along(coords, fold)
sheet = coords2sheet(coords)
plt.imshow(sheet)


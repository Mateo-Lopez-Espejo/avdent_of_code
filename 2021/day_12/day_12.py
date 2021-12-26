import numpy as np
import itertools as itt

with open('input.txt') as file:
    edges = list()
    for line in file:
        edges.append({c for c in line.strip().split('-')})



def get_paths(traversed=['start'], paths=[], repeat_small=None):
    # print(traversed)
    start = traversed[-1]
    #given start find valid nodes to step into
    valid_nodes = list()
    for edge in edges:
        # find conected nodes
        if start in edge:
            (node, ) = edge.difference({start})
            # cannot step on lowecase node more than once
            if node.islower() and node in traversed:
                if node == repeat_small:
                    n_small_visit = traversed.count(repeat_small)
                    if n_small_visit < 2:
                        valid_nodes.append(node)
                    else:
                        continue
                else:
                    continue
            else:
                valid_nodes.append(node)

    if not valid_nodes:
        # print('dead end, stepping back')
        traversed.pop()
        return paths
    else:
        for node in valid_nodes:
            traversed.append(node)
            if node == 'end':
                # print(f'path found {traversed}')
                paths.append(traversed.copy())
                traversed.pop()
            else:
                _ = get_paths(traversed=traversed, paths=paths, repeat_small=repeat_small)
        else:
            traversed.pop()
            return paths

# part 1
vp = get_paths(traversed=['start'], paths=[])
print(f'part 1 paths: {len(vp)}')

# part 2
all_small_caves = set()
for edge in edges:
    for node in edge:
        if node.islower():
            if node not in ('start','end'):
                all_small_caves.add(node)

# this is an unefficient hack since it will find the same path multiple times
# but this is day 12, and today is already december the 26th ...
vp = list()
for small_cave in all_small_caves:
    vp.extend(get_paths(traversed=['start'], paths=[], repeat_small=small_cave))

svp = set([','.join(ll) for ll in vp])
print(f'part 2 paths: {len(svp)}')




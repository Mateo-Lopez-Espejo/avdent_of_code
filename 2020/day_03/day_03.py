import numpy as np
# part 1
lines = list(open('input.txt'))

def count_collision(right, down):
    tree_count = 0
    for ll, line_idx in enumerate(range(0, len(lines), down)):
        line = lines[line_idx].strip()
        idx = (ll * right) % len(line)
        val = line[idx]
        if val == '#':
            tree_count += 1
            # line = ''.join(['X' if nn==idx else char for nn, char in enumerate(line)])
        elif val == '.':
            # line = ''.join(['O' if nn==idx else char for nn, char in enumerate(line)])
            pass
        # print(line)

    return tree_count


tree_count = count_collision(right=3, down=1)
print(tree_count)

# part 2
slopes = [(1,1),
          (3,1),
          (5,1),
          (7,1),
          (1,2)]

all_counts = list()

for right, down in slopes:
    all_counts.append(count_collision(right, down))

print(np.prod(all_counts))




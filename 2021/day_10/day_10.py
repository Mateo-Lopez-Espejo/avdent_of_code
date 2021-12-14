from queue import LifoQueue
from math import floor

with open('input.txt') as file:
# with open('test.txt') as file:
    lines = list()
    for line in file:
        lines.append(line.strip())


openers = [o for o in '([{<']
closers = [c for c in ')]}>']
CO = dict(zip(closers, openers))

sntx_err_scr = {')': 3,
               ']': 57,
               '}': 1197,
               '>': 25137}

cmpl_str_scr = {'(': 1,
                '[': 2,
                '{': 3,
                '<': 4}


# last in first out queue
# part 1
corr_chars = list()
close_scores = list()

for line in lines:
    q = LifoQueue()
    for cc, char in enumerate(line):
        if cc == 0 and char in closers:
            corr_chars.append(char)
            break

        if char in openers:
            q.put(char)

        if char in closers:
            lastchar = q.get()
            if lastchar != CO[char]:
                corr_chars.append(char)
                break

    # part 2
    else:

        if not q.empty():
            score = 0
            while not q.empty():
                score *= 5
                score += cmpl_str_scr[q.get()]
            close_scores.append(score)
            pass

# part 1
print(f'sum of weighted syntax errors: {sum([sntx_err_scr[se] for se in corr_chars])}')

# part 2
close_scores.sort()
print(f'median of closing string scores: {close_scores[int(floor(len(close_scores)/2))]}\n'
      f'Guido bless queues! stacked for success bitches')
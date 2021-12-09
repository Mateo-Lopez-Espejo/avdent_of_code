import numpy as np



# format as arrays of sets with shape Repetiton x Digits
with open('input.txt') as file:
    parsed = list()
    for line in file:
        this_line = list()
        for part in line.split('|'):
            for string in part.split():
                chars = [s for s in string]
                chars.sort()
                chars = set(chars)
                this_line.append(chars)
        parsed.append(this_line)

    parsed = np.asarray(parsed)


digits = parsed[:, :10]
code = parsed[:, 10:]

# part 1
strlen = np.vectorize(len)
str_lens = strlen(code)
EZ_count = np.sum(np.isin(str_lens, [2, 3, 4, 7]))
print(f'count of EZ numbers, {EZ_count}')

# part 2, satan help us
decoded = list()

for ee, (ddd, ccc) in enumerate(zip(digits, code)):

    map = dict.fromkeys(range(10))

    # find 1 4 7 8
    sl = strlen(ddd)
    for key, ll in zip([1, 4, 7, 8], [2, 4, 3, 7]):
        map[key] = ddd[sl == ll][0]

    # five letter numbers: 2 3 5
    fln = ddd[sl == 5]

    # 2 has 2 values not contained in 1 4 or 7, 3 and 5 have 1
    maindiff = map[1].union(map[4]).union(map[7])
    vctr_diff = np.vectorize(lambda x: len(x.difference(maindiff)))
    vd = vctr_diff(fln)
    map[2] = fln[vd == 2][0]

    # 5 has intersection with 1, 3 has 2
    vctr_int = np.vectorize(lambda x: len(x.intersection(map[1])))
    no2 = fln[vd != 2]
    vi = vctr_int(no2)
    map[5] = no2[vi == 1][0]
    map[3] = no2[vi == 2][0]


    # six letter numbers: 6, 9, 0
    sln = ddd[sl == 6]

    # 4 has no difference with 9, but 1 with 6 and 0
    vctr_not_9 = np.vectorize(lambda x: len(map[4].difference(x)))
    not9 = vctr_not_9(sln)
    map[9] = sln[not9 == 0][0]


    # 1 has no difference with 0, but 1 with 6
    vctr_not_0 = np.vectorize(lambda x: len(map[1].difference(x)))
    no9 = sln[not9 == 1]
    not0 = vctr_not_0(no9)
    map[6] = no9[not0][0]
    map[0] = no9[~not0][0]

    # reverses the map, trasfroms int to str for ease 4 digit number creation
    # transforms sets to str to use as kesy
    revmap = {''.join(s for s in val):str(key) for key, val in map.items()}

    decoded.append(int(''.join([revmap[''.join(c for c in cc)] for cc in ccc])))

print(sum(decoded))













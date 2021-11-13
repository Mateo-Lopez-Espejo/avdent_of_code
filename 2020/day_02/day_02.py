
goodies = list()
for line in open('input.txt'):
    line = line.strip()
    rule, password = line.split(':')
    minmax, letter = rule.split(' ')
    minim, maxim = minmax.split('-')

    ocnum = password.count(letter)
    if int(minim)<= ocnum and ocnum <= int(maxim):
        goodies.append(line)

print(f'{len(goodies)} valid passwords, damn! those are some satanic toboggans, I like it')

# part two
goodies = list()
for line in open('input.txt'):
    line = line.strip()
    rule, password = line.split(':')
    password = password.strip()
    idxs, letter = rule.split(' ')
    vil = [password[int(i)-1] for i in idxs.split('-')] # very important letters

    ocnum = vil.count(letter)
    if ocnum == 1:
        goodies.append(line)

print(f'{len(goodies)} valid passwords, less cool')

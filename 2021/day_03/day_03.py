import numpy as np
import scipy.stats as st

with open('input.txt') as file:
    diagnostics = np.stack([[int(i) for i in line.strip()] for line in file], axis=1)

# Part 1
# the most common bool i.e. the mode, and I am to lazy to reinvent the wheel so lets import it
gamma_rate_bin, _ = st.mode(diagnostics, axis=1)
epsilon_rate_bin = np.logical_not(gamma_rate_bin).astype(int)

def bool2dec(bool_vctr):
    # format vectors of bools into str of binary for easy conversion into decimal
    bool_vctr = bool_vctr.squeeze().astype(str)
    bin_str = ''.join(bool_vctr)
    dec = int(bin_str, 2)
    return dec


gamma_rate = bool2dec(gamma_rate_bin)
epsilon_rate = bool2dec(epsilon_rate_bin)

print(f'power output : {gamma_rate * epsilon_rate}') # power output: 3009600

# part 2

def my_mode(array, rating):
    """
    special mode or antymode keeping 1 or 0 when tie
    """
    sum = np.sum(array, axis=1)
    total = array.shape[1]

    mode = []

    for s in sum:
        if s > total-s:
            m = 1
        elif s < total-s:
            m = 0
        else:
            m = 1

        # mode with 1 when tie
        if rating == 'O2':
            mode.append(m)

        # anty mode with 0 when tie
        elif rating == 'CO2':
            # logical not
            mode.append(m * -1 + 1)

        else:
            raise ValueError('dont be a scrub')

    return np.asarray(mode)


# power of recursion bitches!
def find_value(array, rating, position=0):

    bit_criteria = my_mode(array, rating=rating)[position]

    subset = array[:,array[position,:]==bit_criteria]

    if subset.shape[1] == 1:
        return subset
    else:
        return find_value(subset, rating=rating, position=position+1)


O2_bin = find_value(diagnostics, rating='O2')
CO2_bin = find_value(diagnostics, rating='CO2')

O2 = bool2dec(O2_bin)
CO2 = bool2dec(CO2_bin)

print(f'life support: {O2 * CO2}') # life support: 6940518


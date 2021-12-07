import numpy as np
import matplotlib.pyplot as plt
start_pop_vctr = np.loadtxt('input.txt', dtype=int, delimiter=',')


def sim_generatiosn(pop_vctr, n_days):
    for d in range(n_days):

        # 1. cycly clocks
        pop_vctr = pop_vctr - 1

        # 2. find spawning fishes
        parents = np.where(pop_vctr == -1)

        # 3. reset parent timers
        pop_vctr[parents] = 6

        # 4. create and append children
        children = np.full(parents[0].shape, 8)
        pop_vctr = np.concatenate([pop_vctr, children])

    return pop_vctr


# part 1
days = 80
sim_vctr = sim_generatiosn(start_pop_vctr, days)
print(f'there is {sim_vctr.shape[0]} fish after {days}')

# part 2
# define a function to calculate direct offspring given n days
def direct_offspring(pop, stage, time):
    cycle_raw = (time-stage+5)/6
    cycle_poss = np.maximum(np.zeros_like(cycle_raw), cycle_raw) # negatives to zero
    cycle_int = np.floor(cycle_poss) # integers for discrete time points
    offspring = pop * cycle_int # took me a while, empirically tested
    return offspring


# # empirical test, dont ask me, Im a shitty data scientist
# fig , ax = plt.subplots()
# for ss in range(9):
#     ofp = list()
#     for tt in range(30):
#         ofp.append(direct_offspring(1, ss, tt))
#
#     ax.plot(ofp,label=f'{ss}')
# ax.legend()
# fig.show()


# reccursively call offspring function for children


def recurse_linearity(pop, stage, time, cum_pop=0):
    for tt in range(time):
        do = direct_offspring(pop, stage, tt)
        if any(do > 0):
            cum_pop += recurse_linearity(do[do>0],8,time-tt, cum_pop=cum_pop)
    else:
        return np.sum(pop) + cum_pop


yyy = list()
for t in range(5):
    yyy.append(recurse_linearity(np.asarray([1]),
                      np.asarray([0]),
                      t))


fig, ax = plt.subplots()
ax.plot(yyy)
fig.show()
















days = 256
sim_vctr = sim_generatiosn(start_pop_vctr, days)
print(f'there is {sim_vctr.shape[0]} fish after {days}')



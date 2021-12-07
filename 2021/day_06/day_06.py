import numpy as np
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
days = 256
sim_vctr = sim_generatiosn(start_pop_vctr, days)
print(f'there is {sim_vctr.shape[0]} fish after {days}')



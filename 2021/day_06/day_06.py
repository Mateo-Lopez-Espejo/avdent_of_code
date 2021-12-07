import timeit
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

# this shit took me more time that I would like to admit

def fish_cycles(start_vctr, generations, print_gen=False):

    # summarizes initial vector as a count of fishes in each cycle stage
    stage, count = np.unique(start_vctr, return_counts=True)

    # pads the count vctr for stages with no fishes i.e. adds zeros
    pop_vctr = np.zeros(7)
    for ss, cc in zip(stage,count):
        pop_vctr[ss] = cc

    # instead of moving the fishes througn cycles, move the cycle (stage idx) through fishes, defines cycle
    normal_cycle = np.arange(7)

    # simple hack to account for two extra juvenile days
    juv_vctr = np.zeros(2)

    for i in range(generations):
        if print_gen:
            print(np.concatenate((pop_vctr[np.argsort(normal_cycle)], juv_vctr)))

        # juvenile about to enter main cycle
        new_adults = juv_vctr[0]
        # juveniles growing
        juv_vctr[0] = juv_vctr[1]

        # new juveniles
        juv_vctr[1] = pop_vctr[normal_cycle == 0]

        # update the stage in the adult population
        normal_cycle = np.roll(normal_cycle, shift=1)

        # coming of age
        pop_vctr[normal_cycle == 6] = pop_vctr[normal_cycle == 6] + new_adults


    return np.sum(pop_vctr) + np.sum(juv_vctr)

fish_cycles(start_pop_vctr, 256)

timeit.timeit(lambda: fish_cycles(start_pop_vctr, 256), number=1) # 0.0067524379119277 seconds








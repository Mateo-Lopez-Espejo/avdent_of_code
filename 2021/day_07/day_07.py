import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

crab_positions = np.loadtxt('input.txt', dtype=int, delimiter=',')

def fuel_usage(crab_positions, fuel_profile):
    # crab_poss =crab_positions
    crab_poss, crab_count = np.unique(crab_positions, return_counts=True)
    # initialilzese a fuel usage plot with shape N_Uniqu_poss x Range_Poss
    fuel_usage = np.full((crab_poss.size, fuel_profile.size), np.nan)
    # now uses the crab positions to define 0 and increase fuel in both directions
    for cc, poss in enumerate(crab_poss):
        fuel_usage[cc, :poss] = fuel_profile[1:poss+1][::-1]
        fuel_usage[cc, poss:] = fuel_profile[:fuel_profile.size - poss]

    # as always I end up doing stupid stuff and need to debug
    # fig, ax = plt.subplots()
    # ax = sns.heatmap(fuel_usage.astype(int), annot=True, fmt="d", ax=ax)

    # multiply by the number of crabs in tha position
    fuel_usage = fuel_usage * crab_count[:, None]
    # sums across all crabs, and finds the minimum
    total_fuel = np.sum(fuel_usage, axis=0)
    optimal_poss = np.argmin(total_fuel)
    min_fuel = int(total_fuel[optimal_poss])

    return min_fuel

#part 1
lin_profile = np.arange(np.min(crab_positions), np.max(crab_positions)+1)
fuel = fuel_usage(crab_positions, lin_profile)
print(f'optimal blast postion at fuel cost {fuel}\n suck it whale! ')

# part 2
exp_profile = np.cumsum(lin_profile)
fuel = fuel_usage(crab_positions, exp_profile)
print(f'optimal blast postion at fuel cost {fuel}\n suck it whale! ')

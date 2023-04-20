import random
import statistics

# CONSTANTS -- from impractical python projects
GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500


def main():
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print(f"initial population weights = {parents}")
    pop_fitness = fitness(parents, GOAL)
    print(f"initial population fitness = {pop_fitness}")

    avg_wt = []

    while pop_fitness < 1 and generations < GENERATION_LIMIT:
        selected_rats = select(parents, NUM_RATS)
        children = breed(selected_rats, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_rats + children
        pop_fitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, pop_fitness))
        avg_wt.append(int(statistics.mean(parents)))
        generations += 1

    print(f"average weight per generation:\n{avg_wt}")
    print(f"\nnumber of generations = {generations}")
    print(f"number of years = {int(generations / LITTERS_PER_YEAR)}")


def populate(num_rats, min_wt, max_wt, mode_wt):
    rats = []
    while num_rats > 0:
        rats.append(random.triangular(min_wt, max_wt, mode_wt))
        num_rats -= 1
    return rats


def fitness(population, goal):
    avg = statistics.mean(population)
    return avg / goal


def select(population, num_to_retain):
    sorted_population = sorted(population)
    return sorted_population[-num_to_retain:]


def breed(rats, litter_size):
    small_pop = rats[int(len(rats) / 2) :]
    random.shuffle(small_pop)
    large_pop = rats[: int(len(rats) / 2)]
    random.shuffle(large_pop)

    children = []
    for rat1, rat2 in zip(small_pop, large_pop):
        for child in range(litter_size):
            if rat1 < rat2:
                child = random.randint(int(rat1), int(rat2))
            else:
                child = random.randint(int(rat2), int(rat1))
            children.append(child)

    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    for idx, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[idx] = round(rat * random.uniform(mutate_min, mutate_max))
    return children


if __name__ == "__main__":
    main()

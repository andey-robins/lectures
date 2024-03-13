import random
import collections
from tqdm import tqdm

# CONSTANTS -- from impractical python projects

# rate of star formation
R_STAR = 3
# fraction of stars with planets
F_P = 1
# planets per solar system suitable for life
N_E = 0.2
# fraction of suitable planets where life appears
F_E = 0.13
# fraction of planets with life where intelligent life appears
F_I = 0.01
# fraction of civilizations that develop technology which releases
# evidence of their existence to the galaxy at large
F_C = 0.2
# the length of time they emit this evidence
L = 10**8

RADIO_BUBBLE_RADIUS = 100


def main():
    cube_count = radio_cubes_in_galaxy(RADIO_BUBBLE_RADIUS)
    civilization_count = drake_estimation()
    locations = []

    print("Populating galaxy")
    for i in tqdm(range(civilization_count)):
        locations.append(random.randint(1, cube_count))

    print("Counting civs per cube")
    counts = {}
    for val in tqdm(locations):
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1

    print("Counting overlapping civs")
    detected_civs = 0
    for val in tqdm(counts.values()):
        if val > 1:
            detected_civs += val

    print(
        f"The number of civs who could have detected each other = {detected_civs}")
    print("This is a rate of {:.4f}%".format(
        detected_civs / civilization_count * 100))


def radio_cubes_in_galaxy(radio_bubble_radius):
    galaxy_volume = 3.14 * 50_000 * 50_000 * 1_000
    bubble_volume = 3.14 * (4 / 3) * (radio_bubble_radius**3)
    return galaxy_volume / bubble_volume


def drake_estimation():
    return int(R_STAR * F_P * N_E * F_E * F_I * F_C * L)


if __name__ == "__main__":
    main()

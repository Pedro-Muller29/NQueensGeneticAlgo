from sliders import *
from random import sample
from logger import Logger
from random import sample
from crossover import *

class GenerationMaker:
    def __init__(self, logger=Logger, crossover_func = one_point):
        self.logger = logger
        self.crossover = crossover_func

    def generateStartingPopulation(self):
        population = sample(range(0, 2**24), POPULATION_SIZE)
        return population

    def getNewGeneration(self, ranked_generation):
        ranked_generation.sort()

        new_generation = []

        if APPLY_ELITISM:
            new_generation.append(ranked_generation[0][1])

        while len(new_generation) != POPULATION_SIZE:
            four_sample = sample(range(0, len(ranked_generation)), 4)

            father_pos = min(four_sample[0], four_sample[1])
            father = ranked_generation[father_pos][1]

            mother_pos = min(four_sample[2], four_sample[3])
            mother = ranked_generation[mother_pos][1]

            new_generation += eval(f"{self.crossover}(father, mother)")
            new_generation = new_generation[:POPULATION_SIZE]

        return new_generation

if __name__ == "__main__":
    gm = GenerationMaker(Logger())
    print(gm.generateStartingPopulation())
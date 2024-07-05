from evaluation import *
from population import *
from logger import Logger
import sys

def main():
    logger = Logger()
    
    crossover_func = sys.argv[1] if len(sys.argv) > 1 else "one_point"
    
    generation_maker = GenerationMaker(logger=logger, crossover_func=crossover_func)
    initial_population = generation_maker.generateStartingPopulation()

    evolve_generations(logger, generation_maker, initial_population)

def evolve_generations(logger, generation_maker, population):
    generation_number = 0

    while True:
        generation_number += 1
        logger.generation_started(generation_number)
        
        ranked_population = evaluate_population(logger, population, generation_number)

        # Check if a winning solution is found
        for rank, (evaluation, individual) in enumerate(ranked_population, start=1):
            if evaluation == 0:
                logger.found_winner(generation_number, individual)
                return

        # Generate the next population based on rankings
        population = generation_maker.getNewGeneration(ranked_population)

def evaluate_population(logger, population, generation_number):
    ranked_population = []

    for index, individual in enumerate(population, start=1):
        evaluation = evaluate(individual)
        logger.generation_child(index, individual, evaluation)
        ranked_population.append((evaluation, individual))

    return ranked_population

if __name__ == "__main__":
    main()
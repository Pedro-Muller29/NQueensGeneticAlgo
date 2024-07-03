from evaluation import *
from population import *
from logger import Logger

def main():
    logger = Logger()
    gm = GenerationMaker(logger=logger)
    generation = gm.generateStartingPopulation()
    
    generation_number = 0
    while True:
        generation_number += 1

        logger.generation_started(generation_number)

        ranked_generation = []

        for n in range(1, len(generation) + 1):
            child = generation[n-1]
            child_eval = evaluate(child)

            logger.generation_child(n, child, child_eval)

            if child_eval == 0:
                logger.found_winner(generation_number, child)
                return
            
            ranked_generation.append((child_eval, child))
        
        generation = gm.getNewGeneration(ranked_generation)

        

if __name__ == "__main__":
    main()
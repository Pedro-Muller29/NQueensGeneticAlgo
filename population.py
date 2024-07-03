from sliders import *
from random import sample

def generateStartingPopulation():
    population = sample(range(0, 2**24), 8)
    return population

if __name__ == "__main__":
    print(generateStartingPopulation())
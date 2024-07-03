from evaluation import *
from population import *

def main():
    generation = generateStartingPopulation()
    
    generation_number = 0
    while True:
        generation_number += 1
        print("\n=============================================")
        print(f"Generation Number: {generation_number}")
        for n in range(1, len(generation) + 1):
            child = generation[n-1]
            child_eval = evaluate(child)

            print(f"{n} - {format(child, '024b')}, eval -> {child_eval}")

            if child_eval == 0:
                print("\n\n\n=============================================")
                print("Found Answer: ")
                print(f"{format(child, '024b')}")
                print(f"\nTook: {generation_number} Generations")
                return
            
            

if __name__ == "__main__":
    main()
from sliders import *

class Logger:
    def __init__(self):
        self.verbose = VERBOSE

    def generation_started(self, generation_number):
        if self.verbose:
            print("\n=============================================\n")
            print(f"Generation Number: {generation_number}")

    def generation_child(self, child_number, child, child_eval):
        if self.verbose:
            print(f"{child_number} - {format(child, '024b')}, eval -> {child_eval}")
    
    def found_winner(self, generation_number, child):
        if self.verbose:
            print("\n\n\n=============================================")
            print("Found Answer: ")
        print(f"{format(child, '024b')}")
        print(f"\nTook:\n{generation_number} Generations")

    
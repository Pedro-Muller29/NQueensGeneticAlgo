# Genetic Algorithm Crossover Study

This project focuses on experimenting with crossover functions in genetic algorithms to solve the n-queens problem using 24-bit integer representations of queen positions on a chessboard.

Every 3-bit blocks represents the position of a queen in a column of the board. For example, 101 011 (...) represents that the queen on the first column is at the 101 -> 5 position (positions range from 0 to 7).

## Getting Started

### Installation

	1.	Clone this repository:
```bash
git clone https://github.com/Pedro-Muller29/NQueensGeneticAlgo.git
cd  NQueensGeneticAlgo
```

### Usage

	1.	Implement your crossover function in crossover.py. The function should:
	•	Receive two 24-bit integers.
	•	Return a list of 24-bit integers.

Example:
```python
def my_crossover_function(parent1, parent2):
    #divides the 8 column exactly at half
    crossover_point = 12 
    mask = (1 << crossover_point) - 1
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return [child1, child2]
```

	2.	Run the program with your function name:
```bash
python3 main.py my_crossover_function
```

## Example Crossover Function

```python
def example_unipoint(parent1, parent2):
    unipoint_destination = 12
    mask = (1 << crossover_point) - 1
    child1 = (parent1 & mask) | (parent2 & ~mask)
    child2 = (parent2 & mask) | (parent1 & ~mask)
    return [child1, child2]
```

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
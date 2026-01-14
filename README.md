# Genetic Algorithm

A Python implementation of a genetic algorithm designed to evolve a random population of strings until it matches a user-defined target.

## Features

- **Genetic Operators**: Implements selection (elitism), one-point crossover, and random mutation.
- **Dynamic Character Sets**: Automatically detects if the target is numeric, alphabetic, or alphanumeric to optimize the search space.
- **Real-time Progress**: Displays the best candidate and fitness score for every generation in the console.

## Parameters

The following constants in app.py can be tuned for different performance results:

| **Constant** | **Description** | **Default** |
| --- | --- | --- |
| MAX_LEN | Maximum allowed length for the target string | 20  |
| POP_SIZE | Total individuals per generation | 200 |
| MUT_RATE | Probability of a single character mutating (0.0 - 1.0) | 0.02 |
| ELITE | Fraction of the top performers kept for the next generation | 0.1 |

## Installation

- Ensure you have [Python 3.x](https://www.python.org/downloads/) installed.
- Clone this repository:
```bash
git clone https://github.com/Igriscodes/genetic-algorithm.git
cd genetic-algorithm
```

## Usage

Run the script directly from your terminal:

```bash
python app.py
```

Upon running, the program will prompt you to enter a target string (up to 20 characters). The algorithm will then begin evolving strings until a perfect match is found.

**How it Works**

- **Initialization**: Generates a population of 200 random strings.
- **Fitness Evaluation**: Calculates how many characters match the target string at the correct index.
- **Selection**: Keeps the top 10% (elites) to ensure the best traits are never lost.
- **Crossover**: Pairs up parents from the top 50% of the population to create offspring.
- **Mutation**: Small random changes are introduced to maintain genetic diversity and prevent local optima.
- **Iteration**: Repeats until the fitness score equals the length of the target string.

**License**

[GNU Lesser General Public License v2.1](LICENSE) - Feel free to use and modify

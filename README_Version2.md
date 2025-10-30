# Genetic Algorithm Simulation for Genome Mutation and Fitness

This project implements a genetic algorithm in Python to simulate genome mutations, calculate fitness, and analyze population dynamics over multiple generations. The algorithm models random mutations, crossover, insertion, and deletion within a population of individuals, each with a DNA sequence. Fitness is evaluated based on the presence of hydrophilic, hydrophobic, neutral, and stop amino acids.

## Features

- Random genome generation and mutation
- Crossover, insertion, and deletion genetic operators
- Fitness calculation based on amino acid composition
- Population evolution over multiple generations
- Data export to CSV files for further analysis
- Visualization of average and best fitness over time

## Requirements

- Python 3.x
- numpy
- matplotlib

## Usage

Run `CS515_project_2.py` to execute the simulation. Results and statistics are printed to the console and saved as CSV files. Fitness trends are visualized using matplotlib.

## Output

- `gen_array.csv` — Amino acid sequences of selected genomes across generations
- `pop_array.csv` — Amino acid sequences for the whole population at intervals
- Fitness plots saved as PNG images

## License

MIT License

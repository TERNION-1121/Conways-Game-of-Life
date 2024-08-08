# Conway's Game of Life

Welcome to the Conway's Game of Life project! This is a simple implementation of the classic cellular automaton game using Pygame.

## About the Game

The Game of Life, also known simply as Life, is a cellular automaton devised by John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves over time.

The game is played on a two-dimensional grid of cells, where each cell can be in one of two states: alive or dead. The state of each cell in the next generation is determined by the states of the cell and its eight neighbors in the current generation, according to the following rules:

1. Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Getting Started

To run the game, you'll need to have Python and Pygame installed. Then just execute the main.py script.

## Usage

- Press the `Space` key to start/stop the simulation.
- Click on the cells to toggle their state (alive or dead).

## Customization

You can customize the game by modifying the following constants at the beginning of the `main.py` file:

- `COLOR_BG`: The background color of the grid.
- `COLOR_GRID`: The color of the grid lines.
- `COLOR_DIE_NEXT`: The color of cells that will die in the next generation.
- `COLOR_ALIVE_NEXT`: The color of cells that will be alive in the next generation.
- `WINDOW_SIZE`: The size of the game window.
- `GRID_SIZE`: The size of the game grid.
- `CELL_SIZE`: The size of each cell.
- `TICK_SPEED`: The speed of the game simulation (frames per second).

## Contributing

If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request. Contributions are always welcome!

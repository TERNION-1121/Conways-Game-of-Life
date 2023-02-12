<h1 align = "center"><a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"> Conway's Game of Life </a> </h1>

... is a [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton) devised by Mathematician John Conway.  It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

![image](https://user-images.githubusercontent.com/97667653/218299233-55d3968e-003c-48af-a9b5-30a146951a86.png)

## Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, (in this project a 60 x 80 grid of square cells) each of which is in one of two possible states, live `(1)` or dead `(0)` (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time _(or simply generation)_ , the following transitions occur:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Implementation in Python

For the game's implementation we have made use of the `pygame` and `numpy` modules.

The **`update()`** method takes an array of cells (60 x 80 in size), and returns an array of cells of the corresponding next generation, after applying the above mentioned rules.

#### `main()`

As the program begins, it is paused, i.e. by click-dragging your mouse over the square cells, you can make them alive.
As soon as `SPACEBAR` is pressed, it resumes and the generations begin to change.

<img src="https://user-images.githubusercontent.com/97667653/218299007-6a1142a1-f267-4372-8d87-986b4a798816.png" width=400 height=300>


https://user-images.githubusercontent.com/97667653/218298998-000afe24-1a7c-406d-87e1-44ed4e660ed9.mp4
> Example gameplay


<hr>

Big thanks to [Neural Nine](https://www.youtube.com/watch?v=cRWg2SWuXtM)! Was really helpful in Understanding the game mechanics and efficient implementation

import pygame
import numpy as np

COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

WINDOW_SIZE = (800, 600)
GRID_SIZE = (WINDOW_SIZE[1] // 10, WINDOW_SIZE[0] // 10)
CELL_SIZE = 10
TICK_SPEED = 30

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

cells = np.zeros(GRID_SIZE, dtype=np.int8)

def get_neighbor_sum(cells, row, col):
    rows, cols = cells.shape
    neighbors = cells[(row-1)%rows:(row+2)%rows, (col-1)%cols:(col+2)%cols]
    return np.sum(neighbors) - cells[row, col]

def update_cell_state(cells, row, col):
    alive_neighbors = get_neighbor_sum(cells, row, col)
    if cells[row, col] == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if alive_neighbors == 3:
            return 1
        else:
            return 0

def update_grid(screen, cells, with_progress=False):
    updated_cells = np.zeros_like(cells)
    rows, cols = cells.shape

    for row in range(rows):
        for col in range(cols):
            updated_cells[row, col] = update_cell_state(cells, row, col)
            if cells[row, col] != updated_cells[row, col]:
                color = COLOR_DIE_NEXT if updated_cells[row, col] == 0 else COLOR_ALIVE_NEXT
            else:
                color = COLOR_BG if updated_cells[row, col] == 0 else COLOR_ALIVE_NEXT

            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

    return updated_cells

def main():
    global cells
    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                cells[row, col] = 1 - cells[row, col]  # Toggle the cell state

        screen.fill(COLOR_GRID)

        if running:
            cells = update_grid(screen, cells, with_progress=True)
        else:
            update_grid(screen, cells)

        pygame.display.update()
        clock.tick(TICK_SPEED)

if __name__ == "__main__":
    main()

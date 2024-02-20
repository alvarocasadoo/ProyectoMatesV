import pygame
import random

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Tamaño del laberinto
CELL_WIDTH = 40
CELL_HEIGHT = 40
COLS = SCREEN_WIDTH // CELL_WIDTH
ROWS = SCREEN_HEIGHT // CELL_HEIGHT

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Laberinto")

# Definir la clase del laberinto
class Maze:
    def __init__(self):
        self.grid = [[1] * COLS for _ in range(ROWS)]
        self.generate_maze()
        self.start = (1, 1)
        self.end = (ROWS - 2, COLS - 2)
        self.goal = (ROWS // 2, COLS // 2)

    def generate_maze(self):
        stack = []
        current_cell = (1, 1)
        self.grid[current_cell[0]][current_cell[1]] = 0
        stack.append(current_cell)

        while stack:
            current_cell = stack[-1]
            neighbors = []
            for direction in [(0, 2), (2, 0), (-2, 0), (0, -2)]:
                next_row = current_cell[0] + direction[0]
                next_col = current_cell[1] + direction[1]
                if 0 < next_row < ROWS - 1 and 0 < next_col < COLS - 1:
                    if self.grid[next_row][next_col] == 1:
                        neighbors.append((next_row, next_col))
            if neighbors:
                chosen_cell = random.choice(neighbors)
                self.grid[chosen_cell[0]][chosen_cell[1]] = 0
                self.grid[current_cell[0] + (chosen_cell[0] - current_cell[0]) // 2][current_cell[1] + (chosen_cell[1] - current_cell[1]) // 2] = 0
                stack.append(chosen_cell)
            else:
                stack.pop()

    def draw(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.grid[row][col] == 1:
                    pygame.draw.rect(screen, BLACK, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                elif (row, col) == self.start:
                    pygame.draw.rect(screen, RED, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                elif (row, col) == self.end:
                    pygame.draw.rect(screen, RED, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                elif (row, col) == self.goal:
                    pygame.draw.rect(screen, GREEN, (col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

maze = Maze()

# Función principal del juego
def main():
    running = True
    player_position = maze.start
    reached_goal = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Obtener la dirección deseada del movimiento
                move_direction = None
                if event.key == pygame.K_UP:
                    move_direction = (-1, 0)
                elif event.key == pygame.K_DOWN:
                    move_direction = (1, 0)
                elif event.key == pygame.K_LEFT:
                    move_direction = (0, -1)
                elif event.key == pygame.K_RIGHT:
                    move_direction = (0, 1)

                # Verificar si la celda objetivo está vacía y dentro de los límites
                if move_direction:
                    next_row = player_position[0] + move_direction[0]
                    next_col = player_position[1] + move_direction[1]
                    if 0 <= next_row < ROWS and 0 <= next_col < COLS and maze.grid[next_row][next_col] == 0:
                        player_position = (next_row, next_col)
                        if player_position == maze.goal:
                            reached_goal = True

        screen.fill(WHITE)
        maze.draw()
        pygame.draw.rect(screen, RED, (player_position[1] * CELL_WIDTH, player_position[0] * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
        if reached_goal:
            font = pygame.font.SysFont(None, 36)
            text = font.render("¡Felicidades!", True, BLACK)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

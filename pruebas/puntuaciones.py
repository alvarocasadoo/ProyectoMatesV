import pygame
import pymongo
from pygame.locals import *

# Inicializar pygame
pygame.init()

# Crear la ventana de pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tabla de Puntuaciones")

# Definir colores para el fondo y los elementos
background_color = (30, 30, 80)  # Azul oscuro
text_color = (255, 255, 255)  # Blanco

# Definir fuentes y tamaños de texto
font = pygame.font.Font(None, 36)

# Texto para la etiqueta de la tabla de puntuaciones
label_text = "Tabla de Puntuaciones"
label_surface = font.render(label_text, True, text_color)
label_rect = label_surface.get_rect(center=(width // 2, height // 6))  # Aumentar la separación vertical

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["prueba"]
mycollection = mydb["usuarios"]

# Obtener datos de la tabla de puntuaciones desde la base de datos
scores_data = []
for user in mycollection.find():
    if "puntuacion" in user:
        scores_data.append((user["nombre"], user["puntuacion"]))
    else:
        scores_data.append((user["nombre"], 0))  # Asignar puntuación 0 si el campo "puntuacion" no está presente

# Altura y margen de las filas de la tabla de puntuaciones
row_height = 50
row_margin = 10

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Dibujar el fondo
    screen.fill(background_color)

    # Dibujar la etiqueta de la tabla de puntuaciones
    screen.blit(label_surface, label_rect)

    # Dibujar los datos de la tabla de puntuaciones
    for i, (player, score) in enumerate(scores_data):
        # Calcular la posición y el rectángulo de cada fila
        row_y = height // 2 + i * (row_height + row_margin) - len(scores_data) * (row_height + row_margin) // 2
        row_rect = pygame.Rect(100, row_y, width - 200, row_height)

        # Dibujar el rectángulo de la fila
        pygame.draw.rect(screen, text_color, row_rect, border_radius=10)

        # Dibujar el texto del jugador y su puntuación
        player_surface = font.render(player, True, background_color)
        player_rect = player_surface.get_rect(midleft=(row_rect.left + 20, row_rect.centery))
        screen.blit(player_surface, player_rect)

        score_surface = font.render(str(score), True, background_color)
        score_rect = score_surface.get_rect(midright=(row_rect.right - 20, row_rect.centery))
        screen.blit(score_surface, score_rect)

    pygame.display.flip()

pygame.quit()

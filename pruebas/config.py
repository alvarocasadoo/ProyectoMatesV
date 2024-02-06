import pygame
from pygame.locals import *

# Inicializar pygame
pygame.init()

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)

# Crear la ventana de pygame
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menú de Configuración")

# Definir fuentes y tamaños de texto
font_size = 36
font = pygame.font.Font(None, font_size)

# Definir texto para las opciones del menú
menu_options = ["Cambiar Resolución", "Opción 2", "Opción 3", "Opción 4"]

# Definir la resolución actual de la ventana
current_resolution = f"Resolución actual: {width}x{height}"
text_surface = font.render(current_resolution, True, black)

# Inicializar el índice seleccionado
selected_option = 0

# Función para cambiar la resolución
def change_resolution(new_width, new_height):
    global width, height, screen, font, text_surface
    width, height = new_width, new_height
    screen = pygame.display.set_mode((width, height))
    font_size = int(min(width, height) * 0.05)  # Ajustar el tamaño del texto en función de la nueva resolución
    font = pygame.font.Font(None, font_size)
    current_resolution = f"Resolución actual: {width}x{height}"
    text_surface = font.render(current_resolution, True, black)
    print(f"Cambiando la resolución del juego a {width}x{height}")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == K_RETURN:
                # Acción basada en la opción seleccionada
                if selected_option == 0:
                    # Aumentar la resolución al presionar un botón
                    new_width = min(width + 100, 1920)  # Aumentar en 100, con un máximo de 1920
                    new_height = min(height + 100, 1080)  # Aumentar en 100, con un máximo de 1080
                    change_resolution(new_width, new_height)
                elif selected_option == 1:
                    # Agregar acción para la opción 2
                    print("Realizando la acción de la opción 2")
                # Agregar acciones para las otras opciones

    # Dibujar el fondo y el texto
    screen.fill(white)
    screen.blit(text_surface, (10, 10))

    # Dibujar las opciones del menú
    for i, option_text in enumerate(menu_options):
        text_surface = font.render(option_text, True, black if i != selected_option else white)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 40 - len(menu_options) * 20))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()

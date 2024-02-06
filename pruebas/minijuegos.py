import pygame
from pygame.locals import *

# Inicializar pygame
pygame.init()

# Crear la ventana de pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minijuegos")

# Cargar la imagen de fondo
background_image = pygame.image.load("fondoPantallaJuegos.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Definir colores
yellow_orange_dark = (255, 165, 0)
yellow_orange_light = (255, 200, 100)

# Definir fuentes y tamaños de texto
font = pygame.font.Font(None, 36)

# Definir texto para cada botón y funciones para los juegos
button_texts = ["Problemas", "Puzzles", "Laberintos", "Memoria"]

def abrir_ventana_problemas():
    # Aquí va la lógica para abrir la ventana del juego de problemas
    import elegirDificultadProblemas
    elegirDificultadProblemas.main()
    print("Abriendo juego de problemas")

def abrir_ventana_puzzles():
    # Aquí va la lógica para abrir la ventana del juego de puzzles
    print("Abriendo juego de puzzles")

def abrir_ventana_laberintos():
    # Aquí va la lógica para abrir la ventana del juego de laberintos
    print("Abriendo juego de laberintos")

def abrir_ventana_memoria():
    # Aquí va la lógica para abrir la ventana del juego de memoria
    print("Abriendo juego de memoria")

# Inicializar los botones y otros elementos
button_width, button_height = 150, 150
button_padding_x = 20
button_padding_y = 20
button_margin_x = 20
button_margin_y = 20

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, button_text in enumerate(button_texts):
                row = i // 2
                col = i % 2
                button_x = (width - (2 * button_width + button_margin_x)) // 2 + col * (button_width + button_margin_x)
                button_y = (height - (2 * button_height + button_margin_y)) // 2 + row * (button_height + button_margin_y)
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    if button_text == "Problemas":
                        abrir_ventana_problemas()
                    elif button_text == "Puzzles":
                        abrir_ventana_puzzles()
                    elif button_text == "Laberintos":
                        abrir_ventana_laberintos()
                    elif button_text == "Memoria":
                        abrir_ventana_memoria()

    # Dibujar la imagen de fondo
    screen.blit(background_image, (0, 0))

    # Dibujar los botones con degradado de color y esquinas redondeadas
    for i, button_text in enumerate(button_texts):
        row = i // 2
        col = i % 2
        button_x = (width - (2 * button_width + button_margin_x)) // 2 + col * (button_width + button_margin_x)
        button_y = (height - (2 * button_height + button_margin_y)) // 2 + row * (button_height + button_margin_y)

        # Calcular el color de fondo con degradado en función de la posición vertical del botón
        progress = (button_y - ((height - (2 * button_height + button_margin_y)) // 2)) / (2 * button_height + button_margin_y)
        color = (
            int(yellow_orange_dark[0] + progress * (yellow_orange_light[0] - yellow_orange_dark[0])),
            int(yellow_orange_dark[1] + progress * (yellow_orange_light[1] - yellow_orange_dark[1])),
            int(yellow_orange_dark[2] + progress * (yellow_orange_light[2] - yellow_orange_dark[2]))
        )

        # Dibujar el botón con el fondo degradado y esquinas redondeadas
        button_surface = pygame.Surface((button_width, button_height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, button_width, button_height), border_radius=20)
        screen.blit(button_surface, (button_x, button_y))

        # Dibujar el texto del botón
        text_surface = font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(button_x + button_width / 2, button_y + button_height / 2))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()

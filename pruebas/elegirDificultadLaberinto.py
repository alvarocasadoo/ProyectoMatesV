import pygame
from pygame.locals import *

# Inicializar pygame
pygame.init()

# Crear la ventana de pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pantalla de Selección de Dificultad")

# Definir colores para el degradado
color1 = (30, 30, 80)  # Azul oscuro
color2 = (50, 50, 120)  # Azul más claro

# Definir colores para los botones
button_color = (100, 100, 200)  # Color que sintoniza con el degradado

# Definir fuentes y tamaños de texto
font = pygame.font.Font(None, 36)

# Definir texto para los botones
button_texts = ["Fácil", "Media", "Difícil"]

# Altura y margen de los botones
button_height = 50
button_margin = 20

# Texto para la etiqueta de selección de dificultad
label_text = "Elige la dificultad del laberinto"

# Obtener el rectángulo de la etiqueta de selección de dificultad
label_surface = font.render(label_text, True, (255, 255, 255))
label_rect = label_surface.get_rect(center=(width // 2, height // 4))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Obtener la posición del clic
            x, y = event.pos

            # Verificar si se hizo clic en algún botón
            for i, button_text in enumerate(button_texts):
                button_y = height // 2 + i * (button_height + button_margin) - len(button_texts) * (button_height + button_margin) // 2
                button_rect = pygame.Rect(width // 2 - 100, button_y, 200, button_height)

                if button_rect.collidepoint(x, y):
                    print(f"Dificultad seleccionada: {button_text}")

                    # Lógica para abrir el juego correspondiente según la dificultad seleccionada
                    if button_text == "Fácil":
                        import laberintoFacil
                        laberintoFacil.main()  # Llamar a la función main() del script problemasFacil.py
                    elif button_text == "Media":
                        import laberintoMedio
                        laberintoMedio.main()  # Llamar a la función main() del script problemasMedia.py
                    elif button_text == "Difícil":
                        import laberintoDificil
                        laberintoDificil.main()  # Llamar a la función main() del script problemasDificil.py

    # Dibujar el degradado en el fondo
    for y in range(height):
        progress = y / height
        color = (
            int(color1[0] + progress * (color2[0] - color1[0])),
            int(color1[1] + progress * (color2[1] - color1[1])),
            int(color1[2] + progress * (color2[2] - color1[2]))
        )
        pygame.draw.line(screen, color, (0, y), (width, y))

    # Dibujar la etiqueta de selección de dificultad
    screen.blit(label_surface, label_rect)

    # Dibujar los botones
    for i, button_text in enumerate(button_texts):
        button_y = height // 2 + i * (button_height + button_margin) - len(button_texts) * (button_height + button_margin) // 2
        button_rect = pygame.Rect(width // 2 - 100, button_y, 200, button_height)

        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

        text_surface = font.render(button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()

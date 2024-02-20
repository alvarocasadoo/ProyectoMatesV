import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la ventana del juego
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minijuego de Problemas Matemáticos")

# Fuente y tamaño de texto
font = pygame.font.Font(None, 36)

# Función para generar un problema matemático aleatorio
def generar_problema():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operador = random.choice(['+', '-', 'x', '/'])
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == 'x':
        resultado = num1 * num2
    else:
        resultado = num1
        num1 = num1 * num2  # Para la división, intercambiamos los valores de num1 y resultado
    return f"{num1} {operador} {num2} =", resultado

# Función para mostrar el problema actual en la pantalla
def mostrar_problema(problema):
    text_surface = font.render(problema, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(text_surface, text_rect)

# Función principal del juego
def main():
    clock = pygame.time.Clock()

    puntuacion = 0
    tiempo_restante = 500  # Reducir el tiempo restante a 30 segundos
    problema, respuesta = generar_problema()
    input_text = ''
    input_rect = pygame.Rect(250, 300, 100, 36)

    while tiempo_restante > 0:
        screen.fill(WHITE)

        # Mostrar puntuación y tiempo restante
        texto_puntuacion = font.render(f"Puntuación: {puntuacion}", True, BLACK)
        screen.blit(texto_puntuacion, (10, 10))
        texto_tiempo = font.render(f"Tiempo: {tiempo_restante}", True, BLACK)
        screen.blit(texto_tiempo, (WIDTH - texto_tiempo.get_width() - 10, 10))

        mostrar_problema(problema)

        # Dibujar el cuadro de entrada de texto
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()

        # Actualizar el temporizador
        tiempo_restante -= 1
        if tiempo_restante == 0:
            print("Tiempo agotado!")
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.lstrip('-').isdigit():  # Permitir números negativos
                        respuesta_usuario = int(input_text)
                        if respuesta_usuario == respuesta:
                            print("Respuesta correcta!")
                            puntuacion += 10
                            problema, respuesta = generar_problema()
                            input_text = ''
                        else:
                            print("Respuesta incorrecta. Inténtalo de nuevo.")
                            puntuacion -= 5
                            input_text = ''
                    else:
                        print("Por favor, introduce un número válido.")
                        input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        clock.tick(30)

    print("Fin del juego. Puntuación final:", puntuacion)

if __name__ == "__main__":
    main()
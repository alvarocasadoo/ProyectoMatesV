import pygame
import random
import sys
import math

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la ventana del juego
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minijuego de Problemas Matemáticos")

# Fuente y tamaño de texto
font = pygame.font.Font(None, 36)

# Función para generar un problema matemático aleatorio
def generar_problema():
    problema = ''
    respuesta = None

    tipo_problema = random.choice(['suma', 'resta', 'multiplicacion', 'division', 'ecuacion', 'raiz_cuadrada'])
    
    if tipo_problema == 'suma':
        num1 = random.randint(-20, 20)
        num2 = random.randint(-20, 20)
        problema = f"{num1} + {num2} ="
        respuesta = num1 + num2
    elif tipo_problema == 'resta':
        num1 = random.randint(-20, 20)
        num2 = random.randint(-20, 20)
        problema = f"{num1} - {num2} ="
        respuesta = num1 - num2
    elif tipo_problema == 'multiplicacion':
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        problema = f"{num1} x {num2} ="
        respuesta = num1 * num2
    elif tipo_problema == 'division':
        divisor = random.randint(1, 10)
        resultado = random.randint(-10, 10)
        num1 = divisor * resultado
        problema = f"{num1} / {divisor} ="
        respuesta = resultado
    elif tipo_problema == 'ecuacion':
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        problema = f"{a}x^2 + {b}x + {c} = 0"
        respuesta = None  # No verificamos la respuesta automáticamente en ecuaciones
    elif tipo_problema == 'raiz_cuadrada':
        num = random.randint(1, 100)
        problema = f"√{num} ="
        respuesta = math.isqrt(num)

    return problema, respuesta

# Función para mostrar el problema actual en la pantalla
def mostrar_problema(problema):
    text_surface = font.render(problema, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(text_surface, text_rect)

# Función principal del juego
def main():
    clock = pygame.time.Clock()

    puntuacion = 0
    tiempo_restante = 300  # Reducir el tiempo restante a 20 segundos
    problema, respuesta = generar_problema()
    input_text = ''
    input_rect = pygame.Rect(250, 500, 100, 36)

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
                    if respuesta is not None:  # Verificar respuesta solo si está definida
                        try:
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
                        except ValueError:
                            print("Por favor, introduce un número válido.")
                            input_text = ''
                    else:
                        print("Respuesta libre. Revisa manualmente.")
                        puntuacion += 5
                        problema, respuesta = generar_problema()
                        input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        clock.tick(30)

    print("Fin del juego. Puntuación final:", puntuacion)

if __name__ == "__main__":
    main()
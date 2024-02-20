import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Memoria de Números")

# Crear reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Números para el juego
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
secuencia_numeros = []

# Generar una secuencia aleatoria de números
for i in range(5):
    secuencia_numeros.append(random.choice(numeros))

# Mostrar la secuencia de números durante 5 segundos
for numero in secuencia_numeros:
    pantalla.fill(BLANCO)
    fuente = pygame.font.Font(None, 100)
    texto = fuente.render(str(numero), True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    time.sleep(1)  # Mostrar cada número durante 1 segundo

# Limpiar la pantalla
pantalla.fill(BLANCO)
pygame.display.flip()

# Mostrar la secuencia al jugador y esperar su entrada
input_secuencia = []
for numero in secuencia_numeros:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if num in numeros:
                        input_secuencia.append(num)
                elif event.key == pygame.K_BACKSPACE:
                    if input_secuencia:
                        input_secuencia.pop()

        pantalla.fill(BLANCO)
        fuente = pygame.font.Font(None, 36)
        texto_secuencia = "Tu secuencia: " + " ".join(map(str, input_secuencia))
        texto = fuente.render(texto_secuencia, True, NEGRO)
        pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
        pygame.display.flip()

        if len(input_secuencia) == len(secuencia_numeros):
            break

# Mostrar el resultado en la pantalla con texto más pequeño
pantalla.fill(BLANCO)
fuente_resultado = pygame.font.Font(None, 30)  # Tamaño de fuente más pequeño (30)
if input_secuencia == secuencia_numeros:
    texto_resultado = "¡Felicidades! Has recordado la secuencia correctamente."
else:
    texto_resultado = "Lo siento, la secuencia ingresada no es correcta."
texto = fuente_resultado.render(texto_resultado, True, NEGRO)
pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
pygame.display.flip()

# Mantener el mensaje en pantalla durante unos segundos antes de cerrar la ventana
time.sleep(3)

# Cerrar la ventana de Pygame
pygame.quit()

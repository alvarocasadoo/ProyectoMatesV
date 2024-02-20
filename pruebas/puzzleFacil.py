import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Descifra el Mensaje")

# Diccionario de letras y números correspondientes
criptograma = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
    26: 'Z'
}

# Mensaje cifrado y palabra correspondiente
mensaje_cifrado = [5, 14, 20, 15]  # Representa la palabra "NETO"

# Función para descifrar el mensaje cifrado
def descifrar_mensaje(mensaje_cifrado):
    mensaje_descifrado = ""
    for numero in mensaje_cifrado:
        mensaje_descifrado += criptograma[numero]

    return mensaje_descifrado

# Descifrar el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)

# Loop del juego
jugando = True
input_texto = ""
fuente_letras = pygame.font.Font(None, 24)

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_texto.upper() == mensaje_descifrado:
                    print("¡Respuesta correcta!")
                else:
                    print("Respuesta incorrecta. Inténtalo de nuevo.")
                input_texto = ""
            elif event.key == pygame.K_BACKSPACE:
                input_texto = input_texto[:-1]
            else:
                input_texto += event.unicode

    # Limpiar la pantalla
    pantalla.fill(BLANCO)

    # Mostrar instrucciones y mensaje cifrado
    fuente_instrucciones = pygame.font.Font(None, 36)
    texto_instrucciones = fuente_instrucciones.render("Introduce la palabra correspondiente al mensaje cifrado:", True, NEGRO)
    pantalla.blit(texto_instrucciones, (50, 50))

    fuente_mensaje = pygame.font.Font(None, 48)
    texto_mensaje = fuente_mensaje.render("Mensaje cifrado: " + "-".join(map(str, mensaje_cifrado)), True, NEGRO)
    pantalla.blit(texto_mensaje, (50, 100))

    # Mostrar el texto introducido por el usuario
    texto_usuario = fuente_instrucciones.render("Tu respuesta: " + input_texto.upper(), True, NEGRO)
    pantalla.blit(texto_usuario, (50, 150))

    # Mostrar la equivalencia de números a letras en dos columnas
    y_pos = 200
    column_width = ANCHO // 2

    for i, (numero, letra) in enumerate(criptograma.items()):
        if i < len(criptograma) // 2:
            columna = 0
        else:
            columna = column_width

        texto_letra_numero = fuente_letras.render(f"{letra}: {numero}", True, NEGRO)
        pantalla.blit(texto_letra_numero, (columna, y_pos))
        
        if i == len(criptograma) // 2 - 1:
            y_pos = 200
        
        y_pos += 30

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()

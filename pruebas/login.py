import pygame
import sys
import pymongo
 

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de la ventana
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Inicio de Sesión")

# Fuente y tamaño
font = pygame.font.Font(None, 36)

def realizar_login(usuario, contraseña):
    try:
        # Conexión a MongoDB local
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Seleccionar la base de datos y colección
        mydb = client["prueba"]
        mycollection = mydb["usuarios"]

        # Buscar el usuario en la colección
        usuario_encontrado = mycollection.find_one({"nombre": usuario, "contraseña": contraseña})

        if usuario_encontrado:
            print(f"Login exitoso para el usuario {usuario}.")
            # Si el login es exitoso, abre la pantalla de minijuegos
            import minijuegos 
            minijuegos.main()  # Llama a la función main() del script minijuegos.py
            pygame.quit()  # Cierra Pygame después de salir de minijuegos
            sys.exit()  # Sal del script
        else:
            print("Credenciales incorrectas. Login fallido.")

    except Exception as e:
        print(f"Error al conectar a MongoDB local: {str(e)}")

def main():
    clock = pygame.time.Clock()

    usuario_input = ""
    contraseña_input = ""
    input_field = None

    # Coordenadas y dimensiones del botón de inicio de sesión
    button_rect = pygame.Rect(150, 180, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_field == "usuario":
                        input_field = "contraseña"
                    else:
                        realizar_login(usuario_input, contraseña_input)
                elif event.key == pygame.K_BACKSPACE:
                    if input_field == "usuario" and len(usuario_input) > 0:
                        usuario_input = usuario_input[:-1]
                    elif input_field == "contraseña" and len(contraseña_input) > 0:
                        contraseña_input = contraseña_input[:-1]
                else:
                    if event.unicode.isprintable():
                        if input_field == "usuario":
                            usuario_input += event.unicode
                        elif input_field == "contraseña":
                            contraseña_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en el campo de usuario
                if 150 <= event.pos[0] <= 350 and 50 <= event.pos[1] <= 80:
                    input_field = "usuario"
                # Verificar si se hizo clic en el campo de contraseña
                elif 150 <= event.pos[0] <= 350 and 120 <= event.pos[1] <= 150:
                    input_field = "contraseña"
                # Verificar si se hizo clic en el botón de inicio de sesión
                elif button_rect.collidepoint(event.pos):
                    realizar_login(usuario_input, contraseña_input)

        screen.fill(WHITE)

        # Dibujar cajas de entrada de texto con padding
        pygame.draw.rect(screen, BLACK, (150, 50, 200, 30))
        pygame.draw.rect(screen, BLACK, (150, 120, 200, 30))

        # Dibujar texto al lado de cada input con padding
        usuario_label = font.render("Usuario:", True, BLACK)
        contraseña_label = font.render("Contraseña:", True, BLACK)

        screen.blit(usuario_label, (50, 55))
        screen.blit(contraseña_label, (50, 125))

        # Dibujar texto
        usuario_text = font.render(usuario_input, True, WHITE)
        contraseña_text = font.render("*" * len(contraseña_input), True, WHITE)

        screen.blit(usuario_text, (160, 55))
        screen.blit(contraseña_text, (160, 125))

        # Dibujar botón de inicio de sesión
        pygame.draw.rect(screen, BLACK, button_rect)
        button_text = font.render("Iniciar Sesión", True, WHITE)
        screen.blit(button_text, (WIDTH // 2 - button_text.get_width() // 2, 195))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

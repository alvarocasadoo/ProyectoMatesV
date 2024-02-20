import pygame
import sys
import pymongo

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)  # Cambiar el color a negro

# Configuración de la ventana
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Registro e Inicio de Sesión")

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
        else:
            print("Credenciales incorrectas. Login fallido.")

    except Exception as e:
        print(f"Error al conectar a MongoDB local: {str(e)}")

def realizar_registro(usuario, contraseña, email):
    try:
        # Conexión a MongoDB local
        client = pymongo.MongoClient("mongodb://localhost:27017/")

        # Seleccionar la base de datos y colección
        mydb = client["prueba"]
        mycollection = mydb["usuarios"]

        # Verificar si el usuario ya existe
        usuario_existente = mycollection.find_one({"nombre": usuario})

        if usuario_existente:
            print("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            # Insertar nuevo usuario
            nuevo_usuario = {"nombre": usuario, "contraseña": contraseña, "email": email, "puntuacion": 0}
            mycollection.insert_one(nuevo_usuario)
            print(f"Registro exitoso para el usuario {usuario}.")
            switch_to_login()  # Cambiar a la pantalla de inicio de sesión después del registro

    except Exception as e:
        print(f"Error al conectar a MongoDB local: {str(e)}")


def switch_to_login():
    import login as login  
    login.main()  

def main():
    clock = pygame.time.Clock()

    usuario_input = ""
    contraseña_input = ""
    email_input = ""
    input_field = None

    # Coordenadas y dimensiones del botón de registro
    button_rect = pygame.Rect(50, 250, 300, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_field == "usuario":
                        input_field = "contraseña"
                    elif input_field == "contraseña":
                        input_field = "email"
                    elif input_field == "email":
                        realizar_registro(usuario_input, contraseña_input, email_input)
                elif event.key == pygame.K_BACKSPACE:
                    if input_field == "usuario" and len(usuario_input) > 0:
                        usuario_input = usuario_input[:-1]
                    elif input_field == "contraseña" and len(contraseña_input) > 0:
                        contraseña_input = contraseña_input[:-1]
                    elif input_field == "email" and len(email_input) > 0:
                        email_input = email_input[:-1]
                else:
                    if event.unicode.isprintable():
                        if input_field == "usuario":
                            usuario_input += event.unicode
                        elif input_field == "contraseña":
                            contraseña_input += event.unicode
                        elif input_field == "email":
                            email_input += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= event.pos[0] <= 350 and 50 <= event.pos[1] <= 80:
                    input_field = "usuario"
                elif 50 <= event.pos[0] <= 350 and 120 <= event.pos[1] <= 150:
                    input_field = "contraseña"
                elif 50 <= event.pos[0] <= 350 and 190 <= event.pos[1] <= 220:
                    input_field = "email"
                elif button_rect.collidepoint(event.pos):
                    realizar_registro(usuario_input, contraseña_input, email_input)
                elif 50 <= event.pos[0] <= 350 and 310 <= event.pos[1] <= 330:
                    switch_to_login()

        screen.fill(WHITE)

        # Dibujar cajas de entrada de texto con padding
        pygame.draw.rect(screen, BLACK, (50, 50, 300, 30))
        pygame.draw.rect(screen, BLACK, (50, 120, 300, 30))
        pygame.draw.rect(screen, BLACK, (50, 190, 300, 30))

        # Dibujar texto al lado de cada input con padding
        usuario_label = font.render("Usuario:", True, BLACK)
        contraseña_label = font.render("Contraseña:", True, BLACK)
        email_label = font.render("Email:", True, BLACK)

        screen.blit(usuario_label, (10, 55))
        screen.blit(contraseña_label, (10, 125))
        screen.blit(email_label, (10, 195))

        # Dibujar texto
        usuario_text = font.render(usuario_input, True, WHITE)
        contraseña_text = font.render("*" * len(contraseña_input), True, WHITE)
        email_text = font.render(email_input, True, WHITE)

        screen.blit(usuario_text, (120, 55))
        screen.blit(contraseña_text, (160, 125))
        screen.blit(email_text, (70, 195))

        # Dibujar botón de registro
        pygame.draw.rect(screen, BLACK, button_rect)
        button_text = font.render("Registrar", True, WHITE)
        screen.blit(button_text, (WIDTH // 2 - button_text.get_width() // 2, 260))

        # Dibujar texto "¿Estás registrado? Inicia sesión" en negro
        texto_registro = font.render("¿Estás registrado? Inicia sesión", True, BLACK)
        screen.blit(texto_registro, (WIDTH // 2 - texto_registro.get_width() // 2, 320))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

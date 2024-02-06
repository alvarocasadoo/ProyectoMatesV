import cv2
import pygame
from pygame.locals import *
from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

# Función para mostrar el popup de confirmación
def show_confirmation_popup():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askquestion("Confirmación", "¿Desea salir?")
    root.destroy()
    return result

# Inicializar pygame
pygame.init()

# Crear la ventana de pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ventana con Video")

# Cargar la imagen "logoprov.png"
logo_image = pygame.image.load("logoprov.png")

# Obtener las dimensiones de la imagen
logo_width, logo_height = logo_image.get_width(), logo_image.get_height()

# Calcular la posición para centrar la imagen en la ventana
logo_x = (width - logo_width) // 2
logo_y = (height - logo_height) // 2

# Inicializar la captura de video
cap = cv2.VideoCapture("fondo.mp4")  # Reemplaza con la ruta de tu propio archivo MP4

# Inicializar los botones y otros elementos
button_width, button_height = 120, 50
button_padding = 20

button1_rect = pygame.Rect(button_padding, height - button_height - button_padding, button_width, button_height)
button2_rect = pygame.Rect(width // 2 - button_width // 2, height - button_height - button_padding, button_width, button_height)
button3_rect = pygame.Rect(width - button_width - button_padding, height - button_height - button_padding, button_width, button_height)

# Definir colores
red = (255, 0, 0)
button_color = red
shadow_color = (150, 0, 0)

# Definir fuentes y tamaños de texto
font = pygame.font.Font(None, 24)

# Definir texto para cada botón
button1_text = font.render("Jugar", True, (255, 255, 255))
button2_text = font.render("Puntuaciones", True, (255, 255, 255))
button3_text = font.render("Salir", True, (255, 255, 255))

# Conectar a la base de datos MongoDB Atlas
mongo_uri = "mongodb+srv://alemaciasee64:<password>@proyecto.weoesgf.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(mongo_uri)

# Seleccionar la base de datos y la colección
db = mongo_client["nombre_de_tu_base_de_datos"]
users_collection = db["users"]

def switch_to_puntuaciones():
    import puntuaciones
    puntuaciones.main()

# Función para cambiar a la pantalla de minijuegos
def switch_to_registro():
    import registro  # Importa el módulo que contiene la pantalla de minijuegos
    registro.main()  # Llama a la función main() del módulo minijuegos



# Función para verificar las credenciales del usuario
def login_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and user["password"] == password:
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Inicio de sesión fallido")
        return False

# Función para registrar un nuevo usuario
def register_user(username, password):
    if not users_collection.find_one({"username": username}):
        users_collection.insert_one({"username": username, "password": password})
        print("Usuario registrado exitosamente")
        return True
    else:
        print("Nombre de usuario ya existe")
        return False

# Función para mostrar una ventana de texto y obtener la entrada del usuario
def show_text_input(prompt):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                cap.release()
                mongo_client.close()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        return text
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            # Mostrar el popup de confirmación al intentar salir
            confirmation_result = show_confirmation_popup()
            if confirmation_result == 'yes':
                running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if button3_rect.collidepoint(mouse_pos):  # Verifica si el mouse está sobre el botón "Salir"
                # Mostrar el popup de confirmación al presionar el botón "Salir"
                confirmation_result = show_confirmation_popup()
                if confirmation_result == 'yes':
                    running = False
            elif button2_rect.collidepoint(mouse_pos):  # Verifica si el mouse está sobre el botón "Iniciar Sesión"
                switch_to_puntuaciones()
            elif button1_rect.collidepoint(mouse_pos):  # Verifica si el mouse está sobre el botón "Jugar"
                switch_to_registro()
    ret, frame = cap.read()
    if ret:
        # Rotar el video para que se muestre en vertical
        frame = cv2.flip(frame, 0)  # 0 indica voltear verticalmente

        # Convertir la imagen de formato BGR a RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Escalar la imagen para que ocupe toda la ventana
        img_rgb = cv2.resize(img_rgb, (width, height))

        # Convertir la imagen de OpenCV a un objeto de la clase Surface de pygame
        img_pygame = pygame.image.fromstring(img_rgb.tobytes(), img_rgb.shape[:2][::-1], 'RGB')

        # Mostrar el video en la ventana de pygame
        screen.blit(img_pygame, (0, 0))

        # Mostrar la imagen centrada en la ventana
        screen.blit(logo_image, (logo_x, logo_y))

        # Dibujar los botones con efecto 3D
        pygame.draw.rect(screen, shadow_color, (button1_rect.x + 2, button1_rect.y + 2, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, button_color, button1_rect, border_radius=10)

        text_x = button1_rect.x + (button_width - button1_text.get_width()) // 2
        text_y = button1_rect.y + (button_height - button1_text.get_height()) // 2
        screen.blit(button1_text, (text_x, text_y))

        pygame.draw.rect(screen, shadow_color, (button2_rect.x + 2, button2_rect.y + 2, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, button_color, button2_rect, border_radius=10)

        text_x = button2_rect.x + (button_width - button2_text.get_width()) // 2
        text_y = button2_rect.y + (button_height - button2_text.get_height()) // 2
        screen.blit(button2_text, (text_x, text_y))

        pygame.draw.rect(screen, shadow_color, (button3_rect.x + 2, button3_rect.y + 2, button_width, button_height), border_radius=10)
        pygame.draw.rect(screen, button_color, button3_rect, border_radius=10)

        text_x = button3_rect.x + (button_width - button3_text.get_width()) // 2
        text_y = button3_rect.y + (button_height - button3_text.get_height()) // 2
        screen.blit(button3_text, (text_x, text_y))

        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        clock.tick(30)

# Salir del juego al finalizar
pygame.quit()
cap.release()
mongo_client.close()  # Cierra la conexión a MongoDB al finalizar

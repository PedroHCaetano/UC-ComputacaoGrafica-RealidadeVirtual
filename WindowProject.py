import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("GLFW não pode ser executado")
window = glfw.create_window(1000, 600, "Uma janela para o seu bruxo", None, None)
# Eu diminui a dimensão da janela

glfw.set_window_pos(window, 400, 100)
glfw.make_context_current(window)

def center_window(window):
    # Obter dimensões da tela
    monitor = glfw.get_primary_monitor()
    video = glfw.get_video_mode(monitor)
    screen_width, screen_heigth = video.size

    # Obter dimensões da janela
    window_width, window_heigth = glfw.get_window_size(window)

    # Calcular as coordenadas x e y do canto superior esquerdo da janela
    x_pos = (screen_width - window_width) // 2
    y_pos = (screen_heigth - window_heigth) // 2

    # Configurar a posição da janela
    glfw.set_window_pos(window, x_pos, y_pos)

center_window(window)

glClearColor(0.4, 0.2, 0.1, 1.0)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    glfw.poll_events()
    glfw.swap_buffers(window)
glfw.terminate()
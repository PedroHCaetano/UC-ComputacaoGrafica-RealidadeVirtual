import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("GLFW can not be initialized")
window = glfw.create_window(1000, 600, "Uma janela para o seu bruxo", None, None)
# Eu diminui a dimensão da janela

if not window:
    glfw.terminate()
    raise Exception("GLFW can not be created")
glfw.set_window_pos(window, 400, 100)

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

glfw.make_context_current(window)
vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.5, 0.5, 0.0
            ]
colors = [1.0, 0.5, 0.6,
          0.3, 0.6, 1.0,
          0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)
glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)
glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)
glClearColor(0, 0.1, 0.1, 1)
while not glfw.window_should_close(window):

    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)
glfw.terminate()
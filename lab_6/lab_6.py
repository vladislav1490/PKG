import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (0.2, -0.4, -0.3), 
  (0.2, -0.3, -0.1),
  (0.2, -0.3, 0.1),
  (0.2, -0.4, 0.3),
  (0.2, -0.2, 0.3),
  (0.2, -0.1, 0.1),
  (0.2, -0.1, 0.3),
  (0.2, 0.1, 0.3),
  (0.2, 0.1, 0.1),
  (0.2, 0.2, 0.3),
  (0.2, 0.4, 0.3),
  (0.2, 0.3, 0.1),
  (0.2, 0.3, -0.1),
  (0.2, 0.4, -0.3),
  (0.2, 0.2, -0.3),
  (0.2, 0.1, -0.1),
  (0.2, 0.1, -0.3),
  (0.2, -0.1, -0.3),
  (0.2, -0.1, -0.1),
  (0.2, -0.2, -0.3),

  (-0.2, -0.4, -0.3), 
  (-0.2, -0.3, -0.1),
  (-0.2, -0.3, 0.1),
  (-0.2, -0.4, 0.3),
  (-0.2, -0.2, 0.3),
  (-0.2, -0.1, 0.1),
  (-0.2, -0.1, 0.3),
  (-0.2, 0.1, 0.3),
  (-0.2, 0.1, 0.1),
  (-0.2, 0.2, 0.3),
  (-0.2, 0.4, 0.3),
  (-0.2, 0.3, 0.1),
  (-0.2, 0.3, -0.1),
  (-0.2, 0.4, -0.3),
  (-0.2, 0.2, -0.3),
  (-0.2, 0.1, -0.1),
  (-0.2, 0.1, -0.3),
  (-0.2, -0.1, -0.3),
  (-0.2, -0.1, -0.1),
  (-0.2, -0.2, -0.3),
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 12),
    (12, 13),
    (13, 14),
    (14, 15),
    (15, 16),
    (16, 17),
    (17, 18),
    (18, 19),
    (19, 0),

    (0, 20),
    (1, 21),
    (2, 22),
    (3, 23),
    (4, 24),
    (5, 25),
    (6, 26),
    (7, 27),
    (8, 28),
    (9, 29),
    (10, 30),
    (11, 31),
    (12, 32),
    (13, 33),
    (14, 34),
    (15, 35),
    (16, 36),
    (17, 37),
    (18, 38),
    (19, 39),

    (20, 21),
    (21, 22),
    (22, 23),
    (23, 24),
    (24, 25),
    (25, 26),
    (26, 27),
    (27, 28),
    (28, 29),
    (29, 30),
    (30, 31),
    (31, 32),
    (32, 33),
    (33, 34),
    (34, 35),
    (35, 36),
    (36, 37),
    (37, 38),
    (20, 39)
)   

faces = (
  (17, 6, 7, 16),
  (1, 2, 11, 12),
  (2, 3, 4, 5),
  (8, 9, 10, 11),
  (0, 1, 18, 19),
  (13, 12, 15, 14),
  (37, 26, 27, 36),
  (21, 22, 31, 32),
  (22, 23, 24, 25),
  (28, 29, 30, 31),
  (20, 21, 38, 39),
  (34, 35, 32, 33)
  )

face_colors = (
    (1.0, 0.5, 0.5),  # Цвет первой грани
)

edge_colors = (
    (0.0, 0.5, 1.0),  # Голубой цвет для всех рёбер
)

rotation_speed = 15.0

def draw_colored_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(face_colors[0])  # Установка цвета для грани (розовый цвет)
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for i, edge in enumerate(edges):
        glColor3fv(edge_colors[0])  # Установка голубого цвета для каждого ребра
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(rotation_speed, 0, 2, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(-rotation_speed, 0, 2, 0)
                elif event.key == pygame.K_UP:
                    glRotatef(rotation_speed, 2, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(-rotation_speed, 2, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_colored_cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
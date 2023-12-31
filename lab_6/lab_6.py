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

rotation_speed = 1.0
movement_speed = 0.1  # Define the movement speed

rotate_x = 0.0
rotate_y = 0.0
rotate_z = 0.0
rotate_custom = 0.0


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

def handle_movement(keys):
    if keys[pygame.K_w]:  # Move forward
        glTranslatef(0, 0, -movement_speed)
    if keys[pygame.K_s]:  # Move backward
        glTranslatef(0, 0, movement_speed)
    if keys[pygame.K_a]:  # Move left
        glTranslatef(-movement_speed, 0, 0)
    if keys[pygame.K_d]:  # Move right
        glTranslatef(movement_speed, 0, 0)
    if keys[pygame.K_UP]:  # Move up
        glTranslatef(0, movement_speed, 0)
    if keys[pygame.K_DOWN]:  # Move down
        glTranslatef(0, -movement_speed, 0)

def handle_rotation(keys):
    global rotate_x, rotate_y, rotate_z, rotate_custom

    if keys[pygame.K_LEFT]:  # Rotate left around Y-axis
        rotate_y -= rotation_speed
    elif keys[pygame.K_RIGHT]:  # Rotate right around Y-axis
        rotate_y += rotation_speed
    elif keys[pygame.K_UP]:  # Rotate up around X-axis
        rotate_x -= rotation_speed
    elif keys[pygame.K_DOWN]:  # Rotate down around X-axis
        rotate_x += rotation_speed
    elif keys[pygame.K_q]:  # Rotate left around Z-axis
        rotate_z -= rotation_speed
    elif keys[pygame.K_e]:  # Rotate right around Z-axis
        rotate_z += rotation_speed
    elif keys[pygame.K_r]:  # Rotate around custom axis (Y-axis in this case)
        rotate_custom += rotation_speed

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

        keys = pygame.key.get_pressed()  # Get currently pressed keys
        handle_movement(keys)
        handle_rotation(keys)

        glPushMatrix()
        glRotatef(rotate_x, 1, 0, 0)
        glRotatef(rotate_y, 0, 1, 0)
        glRotatef(rotate_z, 0, 0, 1)
        glRotatef(rotate_custom, 0, 1, 0)  # Additional rotation around Y-axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_colored_cube()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
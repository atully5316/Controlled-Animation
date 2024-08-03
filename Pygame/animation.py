# animation.py
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Cube
from rotation import Rotation

def animate_cube(serial_reader, use_pitch_rotation=True):
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    cube = Cube()
    rotation_drag = Rotation()
    rotation_angle = Rotation()  # Separate rotation for pitch angles

    dragging = False  # Track if mouse is being dragged

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                serial_reader.close()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    rotation_drag.reset()  # Reset dragging rotation
                    dragging = True
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    dragging = False
            elif event.type == MOUSEMOTION:
                if dragging:
                    rotation_drag.update(event.pos[0], event.pos[1])

        if use_pitch_rotation:
            # Read pitch angle from Arduino
            pitch = serial_reader.read_pitch()
            if pitch is not None:
                rotation_angle.x_rot = pitch * (180 / 3.14159)  # Convert radians to degrees for rotation

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply rotation from dragging
        glPushMatrix()  # Save the current matrix state
        glRotatef(rotation_drag.y_rot, 0, 1, 0)  # Rotate around y-axis from dragging
        glRotatef(rotation_drag.x_rot, 1, 0, 0)  # Rotate around x-axis from dragging

        # Apply rotation from pitch angle if enabled
        if use_pitch_rotation:
            glPushMatrix()  # Save the matrix state before applying pitch rotation
            glRotatef(rotation_angle.x_rot, 1, 0, 0)  # Rotate around x-axis based on pitch angle

        # Draw the cube
        cube.draw()
        pygame.display.flip()
        pygame.time.wait(10)

        if use_pitch_rotation:
            glPopMatrix()  # Restore matrix state after pitch rotation
        glPopMatrix()  # Restore matrix state after dragging rotation

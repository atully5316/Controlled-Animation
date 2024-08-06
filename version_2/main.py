import pygame
from cube import Cube
from serial_reader import SerialReader

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create Cube instance
cube = Cube()

# Create SerialReader instance
serial_reader = SerialReader('COM7', 9600)

angle_x = 0
angle_y = 0
rotation_speed = 0.05  # Adjust rotation speed as needed
dragging = False
last_mouse_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                dragging = True
                last_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
                last_mouse_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                if last_mouse_pos is not None:
                    dx, dy = event.pos[0] - last_mouse_pos[0], event.pos[1] - last_mouse_pos[1]
                    angle_x -= dy * rotation_speed * 0.1
                    angle_y -= dx * rotation_speed * 0.1
                    last_mouse_pos = event.pos

    # Check connection and read joystick data from serial
    if serial_reader.check_connection():
        values = serial_reader.read_data()
        if len(values) >= 2:
            x_direction, y_direction = values[0], values[1]
            angle_y += x_direction * rotation_speed
            angle_x += y_direction * rotation_speed
    else:
        # Optionally handle the case where the serial port is not connected
        pass

    # Clear screen
    screen.fill((0, 0, 0))

    # Rotate and draw the cube
    cube.draw(screen, angle_x, angle_y)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
serial_reader.close()

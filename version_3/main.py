import pygame
from cube import Cube
from serial_reader import SerialReader
from rotation import Rotation

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create Cube instance
cube = Cube()

# Create SerialReader instance
serial_reader = SerialReader('COM7', 9600)

# Create Rotation instances
drag_rotation = Rotation()
joystick_rotation = Rotation()

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
                    drag_rotation.apply_x_rotation(-dy * rotation_speed * 0.1)
                    drag_rotation.apply_y_rotation(-dx * rotation_speed * 0.1)
                    last_mouse_pos = event.pos

    # Check connection and read joystick data from serial
    if serial_reader.check_connection():
        values = serial_reader.read_data()
        if len(values) >= 2:
            x_direction, y_direction = values[0], values[1]
            joystick_rotation.apply_y_rotation(x_direction * rotation_speed)
            joystick_rotation.apply_x_rotation(y_direction * rotation_speed)
    else:
        # Optionally handle the case where the serial port is not connected
        pass

    # Clear screen
    screen.fill((0, 0, 0))

    # Get rotation angles from both sources
    angle_x = drag_rotation.angle_x + joystick_rotation.angle_x
    angle_y = drag_rotation.angle_y + joystick_rotation.angle_y

    # Rotate and draw the cube
    cube.draw(screen, angle_x, angle_y)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
serial_reader.close()

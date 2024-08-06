import pygame
import serial
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Initialize serial connection
ser = serial.Serial('COM7', 9600)  # Adjust port as needed

# Cube vertices and edges
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

def rotate(vertices, angle_x, angle_y):
    rotated = []
    for v in vertices:
        # Rotation around x-axis
        y = v[1] * math.cos(angle_x) - v[2] * math.sin(angle_x)
        z = v[1] * math.sin(angle_x) + v[2] * math.cos(angle_x)
        x = v[0]
        
        # Rotation around y-axis
        x_new = x * math.cos(angle_y) + z * math.sin(angle_y)
        z = -x * math.sin(angle_y) + z * math.cos(angle_y)
        x = x_new
        
        rotated.append((x, y, z))
    return rotated

def project(v):
    scale = 400 / (v[2] + 4)
    x = v[0] * scale + 400
    y = -v[1] * scale + 300
    return (x, y)

def draw_cube(screen, vertices, edges):
    for edge in edges:
        v1 = project(vertices[edge[0]])
        v2 = project(vertices[edge[1]])
        pygame.draw.line(screen, (255, 255, 255), v1, v2, 1)

angle_x = 0
angle_y = 0
rotation_speed = 0.05  # Adjust rotation speed as needed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read joystick data from serial
    if ser.in_waiting:
        data = ser.readline().decode(errors='ignore').strip()
        try:
            x_direction, y_direction = map(int, data.split(','))
            angle_y += x_direction * rotation_speed
            angle_x += y_direction * rotation_speed
        except ValueError:
            pass

    # Clear screen
    screen.fill((0, 0, 0))

    # Rotate and draw the cube
    rotated_vertices = rotate(vertices, angle_x, angle_y)
    draw_cube(screen, rotated_vertices, edges)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
ser.close()

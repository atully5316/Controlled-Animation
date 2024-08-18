import pygame
import math

class Cube:
    def __init__(self, center=(0, 0, 0)):
        self.center = center
        self.vertices = [
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]
        ]
        
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

    def rotate(self, angle_x, angle_y):
        rotated = []
        for v in self.vertices:
            # Rotation around x-axis
            y = v[1] * math.cos(angle_x) - v[2] * math.sin(angle_x)
            z = v[1] * math.sin(angle_x) + v[2] * math.cos(angle_x)
            x = v[0]
            
            # Rotation around y-axis
            x_new = x * math.cos(angle_y) + z * math.sin(angle_y)
            z = -x * math.sin(angle_y) + z * math.cos(angle_y)
            x = x_new
            
            # Translate vertices based on center
            x += self.center[0]
            y += self.center[1]
            z += self.center[2]
            
            rotated.append((x, y, z))
        return rotated

    def project(self, v):
        scale = 400 / (v[2] + 4)
        x = v[0] * scale + 400
        y = -v[1] * scale + 300
        return (x, y)

    def draw(self, screen, angle_x=0, angle_y=0):
        rotated_vertices = self.rotate(angle_x, angle_y)
        for edge in self.edges:
            v1 = self.project(rotated_vertices[edge[0]])
            v2 = self.project(rotated_vertices[edge[1]])
            pygame.draw.line(screen, (255, 255, 255), v1, v2, 1)

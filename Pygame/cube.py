# cube.py
from OpenGL.GL import *

class Cube:
    def __init__(self):
        self.vertices = [
            [1, 1, -1], [-1, 1, -1], [-1, -1, -1], [1, -1, -1],  # Front face
            [1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1]       # Back face
        ]
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),  # Front face edges
            (4, 5), (5, 6), (6, 7), (7, 4),  # Back face edges
            (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
        ]
        self.faces = [
            (0, 1, 2, 3),  # Front face
            (4, 5, 6, 7),  # Back face
            (0, 1, 5, 4),  # Top face
            (2, 3, 7, 6),  # Bottom face
            (0, 3, 7, 4),  # Left face
            (1, 2, 6, 5)   # Right face
        ]
        # Define colors for each face (each pair of parallel sides has the same color)
        self.colors = [
            (1, 0, 0),  # Red for Front face
            (1, 0, 0),  # Red for Back face
            (0, 1, 0),  # Green for Top face
            (0, 1, 0),  # Green for Bottom face
            (0, 0, 1),  # Blue for Left face
            (0, 0, 1)   # Blue for Right face
        ]

        # Enable depth testing for proper rendering of opaque objects
        glEnable(GL_DEPTH_TEST)
        # Disable blending to ensure solid colors are used
        glDisable(GL_BLEND)
        glClearColor(1, 1, 1, 1)  # Set clear color to white

    def draw(self):
        glBegin(GL_QUADS)
        for face in self.faces:
            color = self.colors[self.faces.index(face)]
            glColor3fv(color)
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            glColor3fv((0, 0, 0))  # Black color for edges
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

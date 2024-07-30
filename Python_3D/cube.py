import numpy as np

def create_cube():
    """Define vertices of the cube"""
    r = [-0.5, 0.5]  # Cube will be centered at (0,0,0)
    X, Y, Z = np.meshgrid(r, r, r)
    vertices = np.array([X.flatten(), Y.flatten(), Z.flatten()])
    return vertices.T

def rotate_cube(vertices, angle):
    """Rotate the cube around the y-axis"""
    # Rotation matrix around y-axis
    R_y = np.array([[np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)]])

    # Rotate the vertices
    rotated = vertices @ R_y.T
    return rotated

def get_cube_faces(vertices):
    """Get cube faces with colors"""
    # Define the vertices of the cube
    faces = [[vertices[j] for j in [0, 1, 3, 2]],
             [vertices[j] for j in [4, 5, 7, 6]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]],
             [vertices[j] for j in [0, 2, 6, 4]],
             [vertices[j] for j in [1, 3, 7, 5]]]
    colors = ['red', 'red', 'green', 'green', 'blue', 'blue']
    return faces, colors

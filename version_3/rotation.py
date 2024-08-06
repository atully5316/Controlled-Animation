import math

class Rotation:
    def __init__(self):
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def apply_x_rotation(self, angle):
        self.angle_x += angle

    def apply_y_rotation(self, angle):
        self.angle_y += angle

    def apply_z_rotation(self, angle):
        self.angle_z += angle

    def get_angles(self):
        return self.angle_x, self.angle_y, self.angle_z

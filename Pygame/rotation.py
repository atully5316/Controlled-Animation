# rotation.py
class Rotation:
    def __init__(self):
        self.x_rot = 0
        self.y_rot = 0
        self.last_x = None
        self.last_y = None

    def update(self, x, y):
        if self.last_x is not None and self.last_y is not None:
            dx = x - self.last_x
            dy = y - self.last_y

            self.y_rot += dx * 0.1
            self.x_rot += dy * 0.1

        self.last_x = x
        self.last_y = y

    def reset(self):
        self.last_x = None
        self.last_y = None

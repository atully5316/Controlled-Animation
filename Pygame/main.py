# main.py
import pygame
from pygame.locals import *
from serial_reader import SerialReader
from animation import animate_cube

def main():
    # Initialize SerialReader
    serial_reader = SerialReader()
    
    # Initialize Pygame and other settings
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    # Call the animate_cube function from animation.py
    animate_cube(serial_reader)

if __name__ == "__main__":
    main()

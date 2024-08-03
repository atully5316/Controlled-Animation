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
    
    # Set to True or False based on whether you want pitch rotation
    use_pitch_rotation = True
    
    # Call the animate_cube function from animation.py
    animate_cube(serial_reader, use_pitch_rotation)

if __name__ == "__main__":
    main()

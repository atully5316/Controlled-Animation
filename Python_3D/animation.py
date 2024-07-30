import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from cube import create_cube, rotate_cube, get_cube_faces
import serial
import time
from matplotlib.animation import FuncAnimation

def read_angle_from_serial(serial_port):
    """Read angle data from the serial port.
    
    Args:
        serial_port (serial.Serial): The serial port object to read from.
        
    Returns:
        float or None: The pitch angle in radians if available, else None.
    """
    if serial_port.in_waiting > 0:
        try:
            line = serial_port.readline().decode().strip()
            if "Pitch (radians):" in line:
                angle = float(line.split(': ')[1])
                return angle
        except Exception as e:
            print(f"Error reading serial data: {e}")
    return None

def animate_cube():
    """Animate the 3D cube based on data read from the serial port.
    
    Creates a 3D plot, reads pitch angle data from the serial port, and animates
    the cube by rotating it based on the received angle data. Updates the plot 
    in real-time and displays the pitch angle in radians and degrees.
    """
    vertices = create_cube()  # Create cube vertices
    fig = plt.figure()  # Create a new figure
    ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot

    try:
        ser = serial.Serial('COM7', 57600, timeout=0)  # Open serial port
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    poly3d = None  # Variable to hold the poly3DCollection object
    text = ax.text2D(0.05, 0.95, "Initializing...", transform=ax.transAxes, fontsize=12)  # Text for displaying angles
    last_angle = None  # Variable to keep track of the last angle to avoid unnecessary updates

    def update(frame):
        """Update function for the animation.
        
        Args:
            frame (int): The current frame number.
        """
        nonlocal last_angle, poly3d

        angle_radians = read_angle_from_serial(ser)  # Read angle from serial
        if angle_radians is None:
            return

        angle_degrees = np.degrees(angle_radians)  # Convert angle to degrees

        # Update the plot only if the angle has changed significantly
        if last_angle is None or abs(angle_radians - last_angle) > 0.01:
            last_angle = angle_radians  # Update last_angle

            rotated_vertices = rotate_cube(vertices, angle_radians)  # Rotate the cube
            faces, colors = get_cube_faces(rotated_vertices)  # Get cube faces and colors

            if poly3d:
                poly3d.remove()  # Remove previous poly3DCollection if it exists

            poly3d = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='k', alpha=.75)  # Create new Poly3DCollection
            ax.add_collection3d(poly3d)  # Add the new Poly3DCollection to the plot

            # Draw coordinate axes
            ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
            ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
            ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

            # Set limits and labels
            ax.set_xlim([-1, 1])
            ax.set_ylim([-1, 1])
            ax.set_zlim([-1, 1])
            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')

            # Update the displayed text with the current angle
            text.set_text(f"Pitch (radians): {angle_radians:.4f}\nPitch (degrees): {angle_degrees:.2f}")
            fig.canvas.draw_idle()  # Efficient redraw

    # Create an animation object that updates every 50 ms
    ani = FuncAnimation(fig, update, interval=50, cache_frame_data=False)

    plt.show()  # Display the plot
    ser.close()  # Close the serial port

if __name__ == '__main__':
    animate_cube()  # Run the animation

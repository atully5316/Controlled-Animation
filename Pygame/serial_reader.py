# serial_reader.py
import serial

class SerialReader:
    def __init__(self, port='COM7', baud_rate=57600):
        self.serial_port = serial.Serial(port, baud_rate)
        self.serial_port.flushInput()
    
    def read_pitch(self):
        if self.serial_port.in_waiting > 0:
            try:
                line = self.serial_port.readline().decode('utf-8').strip()
                if line.startswith("Pitch (radians): "):
                    pitch_str = line.split(": ")[1]
                    pitch = float(pitch_str)
                    return pitch
            except ValueError:
                return None
        return None

    def close(self):
        self.serial_port.close()

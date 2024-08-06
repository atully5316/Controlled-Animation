import serial
import time

class SerialReader:
    def __init__(self, port='COM7', baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.connect()

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
        except serial.SerialException:
            self.ser = None

    def read_data(self):
        if self.ser:
            try:
                if self.ser.in_waiting:
                    data = self.ser.readline().decode(errors='ignore').strip()
                    try:
                        # Split the data by commas and convert to integers
                        values = list(map(int, data.split(',')))
                        return values
                    except ValueError:
                        return []
            except serial.SerialException:
                self.ser.close()
                self.ser = None
        return []

    def check_connection(self):
        if self.ser is None:
            self.connect()
        return self.ser is not None

    def close(self):
        if self.ser:
            self.ser.close()

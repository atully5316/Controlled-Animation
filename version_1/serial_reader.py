import serial

class SerialReader:
    def __init__(self, port='COM7', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)

    def read_data(self):
        if self.ser.in_waiting:
            data = self.ser.readline().decode(errors='ignore').strip()
            try:
                # Split the data by commas and convert to integers
                values = list(map(int, data.split(',')))
                return values
            except ValueError:
                return []
        return []

    def close(self):
        self.ser.close()

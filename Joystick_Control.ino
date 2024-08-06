void setup() {
  Serial.begin(9600);
}

void loop() {
  int x = analogRead(A0); // Read joystick x-axis
  int y = analogRead(A1); // Read joystick y-axis

  // Define thresholds
  int threshold = 200; // Adjust as needed
  int neutral = 512;

  int x_direction = 0;
  int y_direction = 0;

  if (x < neutral - threshold) {
    x_direction = -1;
  } else if (x > neutral + threshold) {
    x_direction = 1;
  } else {
    x_direction = 0;
  }

  if (y < neutral - threshold) {
    y_direction = -1;
  } else if (y > neutral + threshold) {
    y_direction = 1;
  } else {
    y_direction = 0;
  }

  Serial.print(x_direction);
  Serial.print(",");
  Serial.println(y_direction);

  delay(100); // Adjust delay as needed
}

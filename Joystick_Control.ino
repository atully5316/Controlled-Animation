#include <Wire.h>

// Joystick analog pins
const int joystickXPin = A0;  // X-axis pin
const int joystickYPin = A1;  // Y-axis pin

// Define thresholds for mapping joystick values
const int threshold = 100;  // Threshold for detecting movement

void setup() {
  // Initialize serial communication
  Serial.begin(57600);
}

void loop() {
  // Read joystick X and Y values
  int xValue = analogRead(joystickXPin);
  int yValue = analogRead(joystickYPin);

  // Map joystick values to -1, 0, 1
  int xMovement = mapToMovement(xValue);
  int yMovement = mapToMovement(yValue);

  // Print the movement values as a comma-separated list
  Serial.print(xMovement);
  Serial.print(",");
  Serial.println(yMovement);

  // Delay for a short period
  delay(100);  // Adjust delay if needed
}

// Function to map joystick values to -1, 0, or 1
int mapToMovement(int value) {
  // Map the analog reading to movement values
  if (value < (512 - threshold)) {
    return -1;  // Movement in the negative direction
  } else if (value > (512 + threshold)) {
    return 1;   // Movement in the positive direction
  } else {
    return 0;   // No movement
  }
}

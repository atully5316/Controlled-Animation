#include <Wire.h>
#include <MPU6050.h>

// Create an MPU6050 object
MPU6050 mpu;

// Variable to hold the pitch angle
float pitch;

void setup() {
  // Initialize serial communication
  Serial.begin(57600);
  Wire.begin();

  // Initialize MPU6050
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed!");
    while (1);
  }

  Serial.println("MPU6050 initialized.");
}

void loop() {
  // Read accelerometer data
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

  // Convert raw accelerometer data to g (gravity units)
  float ax_g = ax / 16384.0; // MPU6050 has a sensitivity of 16384 LSB/g
  float ay_g = ay / 16384.0;
  float az_g = az / 16384.0;

  // Calculate pitch (in radians)
  pitch = atan(-ax_g / sqrt(ay_g * ay_g + az_g * az_g));

  // Print the pitch angle
  Serial.print("Pitch (radians): ");
  Serial.println(pitch, 4);

  delay(100);
}

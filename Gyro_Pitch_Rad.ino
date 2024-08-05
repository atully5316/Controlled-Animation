#include <Wire.h>
#include <MPU6050.h>

// Create an MPU6050 object
MPU6050 mpu;

// Variables to hold pitch and roll angles
float pitch, roll;

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

  // Calculate roll (in radians)
  roll = atan2(ay_g, az_g);

  // Calculate pitch (in radians)
  pitch = atan2(-ax_g, sqrt(ay_g * ay_g + az_g * az_g));

  // Print angles as comma-separated values
  Serial.print(roll, 4); // Print roll first
  Serial.print(", ");
  Serial.print(pitch, 4); // Print pitch second
  Serial.println();

  delay(100);
}

#include <Servo.h>

#define FAN_PIN 5
#define LED_PIN 6
#define SERVO_PIN 9

Servo door;
char mode = 'F';  // Default mode

void setup() {
  Serial.begin(9600);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  door.attach(SERVO_PIN);
  door.write(0);
}

void loop() {
  if (Serial.available() >= 2) {
    mode = Serial.read();          // 'F', 'L', 'S'
    int value = Serial.read();     // 0-255 or 0/180 for servo

    switch (mode) {
      case 'F':
        analogWrite(FAN_PIN, value);
        break;
      case 'L':
        analogWrite(LED_PIN, value);
        break;
      case 'S':
        if(value==0)
        door.write(0);
        else
        door.write(180);
        break;
    }
  }
}
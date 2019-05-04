#include <Servo.h>

//Define Servo Signal Pins
#define S1 9
#define S2 10
#define S3 11

//Creating Servo Objects
Servo Servo1;
Servo Servo2;
Servo Servo3;

//define motors variables
volatile int th1;
volatile int th2;
volatile int th3;

//define data recieved
volatile int data[3];

void setup() {
    Serial.begin(9600);

    //Attach servo motors to corresponding pins
    Servo1.attach(S1);
    Servo2.attach(S2);
    Servo3.attach(S3);
}

void loop() {
  if (Serial.available()){
    //read data from python code through serial comm.
    data = Serial.read(); 
    //assign motors' variables
    th1 = data[0];
    th2 = data[1];
    th3 = data[2];
    //move motors to angles
    Servo1.write(th1);
    Servo2.write(th2);
    Servo3.write(th3);
  }
}

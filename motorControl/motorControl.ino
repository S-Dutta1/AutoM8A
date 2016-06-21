#include <Arduino.h>
#include "BasicStepperDriver.h"
#include <Servo.h>

#define motorSteps 200
#define microSteps 1 // determines speed of stepper, to be kept full, i.e. 1

//to be filled in....
int dirPin[4]={1,2,3,4};//arbit values to be replaced later
int stepPin[4]={5,6,7,8};//arbit values to be replaced later
BasicStepperDriver steppers[4] = {
      BasicStepperDriver(motorSteps, dirPin[0], stepPin[0]),
      BasicStepperDriver(motorSteps, dirPin[1], stepPin[1]),
      BasicStepperDriver(motorSteps, dirPin[2], stepPin[2]),
      BasicStepperDriver(motorSteps, dirPin[3], stepPin[3])
    };//stepper motor array
int servoPosition[4]={90,90,90,90}; //initial arbit setting, to be replaced later
Servo servos[4]; //array of servos

long incomingInt = 0;   // for incoming serial data
int motorNum,val;

void setup()
{
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  for(int i=0;i<4;i++){
    servos[i].attach(9+i); //arbit pin attachment, reset later
    servos[i].write(servoPosition[i]);
    steppers[i].setRPM(200); //set to desired value later
    steppers[i].setMicrostep(microSteps);
  }
}

void loop()
{
  if (Serial.available() > 0) {
    // read the incoming integer:
    incomingInt = Serial.parseInt();
    motorNum=((int) abs(incomingInt))%10;
//I'm going to number steppers as odd numbers, and servos even 
    val=(int)incomingInt/10;
    
    switch(motorNum){
      case 1:
      case 3:
      case 5:
      case 7:steppers[motorNum/2].rotate(val);
            break;
      case 2:
      case 4:
      case 6:
      case 8:servoPosition[motorNum/2-1]=val;
            break;
    }
    
    for(int i=0;i<4;i++){
      servos[i].write(servoPosition[i]);
    }
  }
}

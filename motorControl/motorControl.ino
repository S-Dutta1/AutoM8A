#include <Arduino.h>
#include "BasicStepperDriver.h"
#include <Servo.h>

#define motorSteps 200
#define microSteps 1 // determines speed of stepper, to be kept full, i.e. 1

//to be filled in....
int dirPin[4]={22,23,24,25};//arbit values to be replaced later
int stepPin[4]={26,27,28,29};//arbit values to be replaced later
int stepperPos[4]={127,0,0,0};
BasicStepperDriver steppers[4] = {
      BasicStepperDriver(motorSteps, dirPin[0], stepPin[0]),
      BasicStepperDriver(motorSteps, dirPin[1], stepPin[1]),
      BasicStepperDriver(motorSteps, dirPin[2], stepPin[2]),
      BasicStepperDriver(motorSteps, dirPin[3], stepPin[3])
    };//stepper motor array
int servoPosition[4]={90,90,90,90}; //initial arbit setting, to be replaced later
Servo servos[4]; //array of servos

unsigned int incomingInt = 0;   // for incoming serial data
char incomingByte;
int motorNum,val;


void setup()
{
  Serial.begin(57600); // opens serial port, sets data rate to 9600 bps
  for(int i=0;i<4;i++){
    servos[i].attach(9+i); //arbit pin attachment, reset later
    servos[i].write(servoPosition[i]);
    steppers[i].setRPM(300); //set to desired value later
    steppers[i].setMicrostep(microSteps);
  }
}

void loop()
{
  if (Serial.available() > 0) {
    // read the incoming integer:
    incomingInt = 0;         // throw away previous incomingInt
    while(1) {            // force into a loop until 'n' is received
      incomingByte = Serial.read();
      if (incomingByte == '\n') break;   // exit the while(1), we're done receiving
      if (incomingByte == -1) continue;  // if no characters are in the buffer read() returns -1
      incomingInt *= 10;  // shift left 1 decimal place
      // convert ASCII to integer, add, and shift left 1 decimal place
      incomingInt = ((incomingByte - 48) + incomingInt);
    }
    
    motorNum=((int) abs(incomingInt))%10;
    val=(int)incomingInt/10;
    Serial.println(val);
//I'm going to number steppers as odd numbers, and servos even 
    switch(motorNum){
      case 1:
      case 3:
      case 5:
      case 7:
              if(abs(val-stepperPos[motorNum/2])>5){
                steppers[motorNum/2].rotate((int)(-val+stepperPos[motorNum/2])*1700/110);
                //steppers[motorNum/2].rotate(100);
                stepperPos[motorNum/2]=val;
                //delay(20);
              }
              break;
      case 2:
      case 4:
      case 6:
      case 8:servoPosition[motorNum/2-1]=val;
      //delay(5);
            break;
    }
    
    /*for(int i=0;i<4;i++){
      servos[i].write(servoPosition[i]);
      delay(10);
    }*/
  }
}

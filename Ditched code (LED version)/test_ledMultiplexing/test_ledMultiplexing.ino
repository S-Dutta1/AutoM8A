int c=8,b=7,a=4,d=13;
int thresh=950,delay_mili=100;
void setup() {
  // put your setup code here, to run once:
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  pinMode(d,OUTPUT);
  Serial.begin(9600);
}
void select(int pin1,int pin2,int pin3,int pin4){
  digitalWrite(d,pin1);
  digitalWrite(c,pin2);
  digitalWrite(b,pin3);
  digitalWrite(a,pin4);
}

void loop() {
  // put your main code here, to run repeatedly:
  select(0,0,0,0);//1st
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  /*
  select(0,0,0,1);//2nd
  Serial.print(analogRead(A0));
  Serial.print("   ");
  //sensorOut();
  delay(delay_mili);
  
  select(0,0,1,0);//3rd
  Serial.print(analogRead(A0));
  Serial.print("   ");
  //sensorOut();
  delay(delay_mili);
  
  select(0,0,1,1);//4th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  //sensorOut();
  delay(delay_mili);
  
  select(0,1,0,0);//5th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  //sensorOut();
  delay(delay_mili);
  
  select(0,1,0,1);//6th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  
  select(0,1,1,0);//7th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  
  select(0,1,1,1);//8th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  
  select(1,0,0,0);//9th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  
  select(1,0,0,1);//10th
  Serial.print(analogRead(A0));
  Serial.print("   ");
  delay(delay_mili);
  */
  Serial.println();
  
}

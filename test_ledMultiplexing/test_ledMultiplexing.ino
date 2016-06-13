int c=4,b=3,a=2;
int thresh=950,delay_mili=1000;
void setup() {
  // put your setup code here, to run once:
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  Serial.begin(9600);
}
void select(int pin1,int pin2,int pin3){
  digitalWrite(c,pin1);
  digitalWrite(b,pin2);
  digitalWrite(a,pin3);
}
void sensorOut(){
  /*if(analogRead(A0)>thresh) Serial.print(1);
  else Serial.print(0);
  if(analogRead(A1)>thresh) Serial.print(1);
  else Serial.print(0);
  if(analogRead(A2)>thresh) Serial.print(1);
  else Serial.print(0);
  if(analogRead(A3)>thresh) Serial.print(1);
  else Serial.print(0);
  if(analogRead(A4)>thresh) Serial.print(1);
  else Serial.print(0);
  Serial.println();*/

  Serial.print(analogRead(A0));
  Serial.print("   ");
  Serial.print(analogRead(A1));
  Serial.print("   ");
    Serial.print(analogRead(A2));
  Serial.print("   ");
    Serial.print(analogRead(A3));
  Serial.print("   ");
    Serial.print(analogRead(A4));
  Serial.print("   ");

  Serial.println();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  select(0,0,0);
  sensorOut();
  delay(delay_mili);
  select(0,0,1);
  sensorOut();
  delay(delay_mili);
  select(0,1,0);
  sensorOut();
  delay(delay_mili);
  select(0,1,1);
  sensorOut();
  delay(delay_mili);
  select(1,0,0);
  sensorOut();
  delay(delay_mili);  
}

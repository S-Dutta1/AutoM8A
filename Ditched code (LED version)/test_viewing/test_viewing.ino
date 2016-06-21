int sensor1=A0;
int sensor2=A1;
int led=13;
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  digitalWrite(led,HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  Serial.print(analogRead(sensor1));
  Serial.print("        ");
  Serial.println(analogRead(sensor2));
  delay(200);
  
}

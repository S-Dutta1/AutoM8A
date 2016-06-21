int x=A0,y=A1,prev,ctr;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
ctr=0;
}

void loop() {
  // put your main code here, to run repeatedly:
  int curr=analogRead(x);
  if(ctr==0){
    prev=curr;
    Serial.print(curr);
    Serial.print("     ");
    //Serial.print(analogRead(y));
    Serial.println();
  }
  else{
    if(curr-prev<100&&prev-curr<100){
      Serial.print(curr);
      Serial.print("     ");
      //Serial.print(analogRead(y));
      Serial.println();
      prev=curr;
    }
  }

delay(200);
ctr++;
}

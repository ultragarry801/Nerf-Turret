//look through this page for info on the transistor motor controll https://itp.nyu.edu/physcomp/labs/motors-and-transistors/using-a-transistor-to-control-high-current-loads-with-an-arduino/

#include<Servo.h>

Servo servoHor; //Horizontal Servo

int motorPin = 13;
int x;
int z = 20;
int prevX;
int track;
int panSpeed = 60;

void setup()
{
  pinMode(motorPin, OUTPUT);
  Serial.begin(9600); 
  servoHor.attach(4); //Attach Servo to Pin 6, change this to the pin your servo is attached to
  servoHor.write(servoHor.read());
}

void Pos()
{
  if(prevX != x)
  {
    if (x > 50){
    
      z = z + 1;     
      servoHor.write(z);
      delay(30);

    }else if(x < 50){
      z = z - 1;
      servoHor.write(z);
      delay(30);

    }else if(x == 50){
      digitalWrite(motorPin, HIGH);
      delay(900);
      analogWrite(motorPin, 0);
    }  
  }
  
}

void loop()
{
  if(Serial.available() > 0)
  {
    
   x = Serial.read();
   if(Serial.read() != 0 and Serial.read() != 50){
    track = Serial.read();
   }
   Pos();
    while(Serial.available() > 0)
    {
      Serial.read();
    }
}else if (track>=50 and !Serial.available()>0){
  for (int i = servoHor.read(); i < 180; i++){
    servoHor.write(i);
    z = i;
    delay(panSpeed);
    if(Serial.available()>0){
      break;
    }
  }
  track = 20;
}else if (track <= 50 and !Serial.available()>0){
  for (int i = servoHor.read(); i > 0; i--){
    servoHor.write(i);
    z = i;
    delay(panSpeed);
    if(Serial.available()>0){
      break;
    }
  }
  track = 60;
}
}

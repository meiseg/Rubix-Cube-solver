// Include the Arduino Stepper Library

#include <AccelStepper.h>

// Define the AccelStepper interface type:
// Include the Arduino Stepper Library

#include <AccelStepper.h>

// Define the AccelStepper interface type:

// Create Instance of AccelStepper library
//U
AccelStepper motor1(AccelStepper::DRIVER, 12, 13);
//R
AccelStepper motor2(AccelStepper::DRIVER, 2, 3);
//F
AccelStepper motor3(AccelStepper::DRIVER, 4, 5);
//B
AccelStepper motor4(AccelStepper::DRIVER, 6, 7);
//D
AccelStepper motor5(AccelStepper::DRIVER, 8, 9);

//L
AccelStepper motor6(AccelStepper::DRIVER, 10, 11);

int steps = 1;

int check_count_time = millis();
int check_count_time1 = millis();
int count = 0;
int count1 = 0;
char test[20];
int i=0;
int v= 0;
int speedt;
int x = 50;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(57600);
  motor1.setMaxSpeed(50000);
  motor1.setAcceleration(13500);
  motor2.setMaxSpeed(50000);
  motor2.setAcceleration(13500);
  motor3.setMaxSpeed(50000);
  motor3.setAcceleration(13500);
  motor4.setMaxSpeed(50000);
  motor4.setAcceleration(13500);
  motor5.setMaxSpeed(50000);
  motor5.setAcceleration(13500);
  motor6.setMaxSpeed(50000);
  motor6.setAcceleration(13500);
  motor1.setCurrentPosition(50);
  motor2.setCurrentPosition(50);
  motor3.setCurrentPosition(50);
  motor4.setCurrentPosition(50);
  motor5.setCurrentPosition(50);
  motor6.setCurrentPosition(50);
  
 
}
void processString(char* str) {
  int i = 0;
  while (str[i] != '\0') { // Iterate through each character in the string until the null terminator is encountered
    char direction = str[i];
     steps = 1;
    if (str[i + 1] == '\'') { // Check for prime notation (')
      steps = -1;
      i++; // Skip the prime notation character
    }
    // Move the motor based on the direction and steps
    if (direction == 'U') {
      
      motor1.move(steps * x);
      motor1.runToPosition();
    } else if (direction == 'R') {
    
      motor2.move(-steps * x);
      motor2.runToPosition();
    } else if (direction == 'F') {
    
      motor3.move(steps * x);
      motor3.runToPosition();
    } else if (direction == 'B') {
          
      motor4.move(-steps * x);
      motor4.runToPosition();
    } else if (direction == 'D') {
           
      motor5.move(-steps * x);
      motor5.runToPosition();
    } else if (direction == 'L') {
  
      motor6.move(steps * x);
      motor6.runToPosition();
    } else {
      Serial.println("Error occurred: Unknown direction");
    }
    Serial.println(i);
    i++;
    
  }
}
void loop() {
  // put your main code here, to run repeatedly:

  
 if(millis() - check_count_time1 >= 10){ 
  check_count_time1 = check_count_time1 + 10;
  count1++;
  count1 = count1 %10;
  if(count1 == 0){
  while(Serial.available() > 0){
        String inputString = Serial.readStringUntil('\n');
      char inputCharArray[40]; // Adjust the size as needed
      inputString.toCharArray(inputCharArray, 40); // Adjust the size as needed
      processString(inputCharArray);

    }
  }
  
 }
//motor1.run();
}

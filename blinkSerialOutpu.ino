const int led = 2;
const int button = 31;

int buttonClosed = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);
  buttonClosed = digitalRead(button);
  if (buttonClosed == HIGH) {
    Serial.println("on");
    digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
    delay(500);
  } else {
    Serial.println("off");
  }
}
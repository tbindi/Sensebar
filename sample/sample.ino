
void setup() { Serial.begin(9600); Keyboard.begin();}
void loop() {
  float sensor = 
0
;
  int sensorValueD8 = digitalRead(8); 
  int sensorValueD9 = digitalRead(9); 
  int sensorValueD10 = digitalRead(10);
  int sensorValueD11 = digitalRead(11);
  int sensorValueD12 = digitalRead(12);
  
  int sensorValueD2 = digitalRead(2);
  int sensorValueD3 = digitalRead(3);
  int sensorValueD4 = digitalRead(4);
  int sensorValueD5 = digitalRead(5);
  int sensorValueD6 = digitalRead(6);
  int sensorValueD7 = digitalRead(7);
  
  float voltageD8 = sensorValueD8 * (500.0 / 1023.0);
  float voltageD9 = sensorValueD9 * (500.0 / 1023.0);
  float voltageD10 = sensorValueD10 * (500.0 / 1023.0);
  float voltageD11 = sensorValueD11 * (500.0 / 1023.0);
  float voltageD12 = sensorValueD12 * (500.0 / 1023.0);
  
  float voltageD2 = sensorValueD2 * (5.0 / 1023.0);
  float voltageD3 = sensorValueD3 * (5.0 / 1023.0);
  float voltageD4 = sensorValueD4 * (5.0 / 1023.0);
  float voltageD5 = sensorValueD5 * (5.0 / 1023.0);
  float voltageD6 = sensorValueD6 * (5.0 / 1023.0);
  float voltageD7 = sensorValueD7 * (5.0 / 1023.0);

  if(voltageD11 > sensor){ // L TOP
Serial.println("D11");
Keyboard.press('q');
  }
  if(voltageD8 > sensor){ // UP
Serial.println("D8");
Keyboard.press('w');
  }
  if(voltageD10 > sensor){ // DOWN
Serial.println("D10");
Keyboard.press('s');
  }
  if(voltageD9 > sensor){ // LEFT
Serial.println("D9");
Keyboard.press('a');
  }
  if(voltageD12 > sensor){ // RIGHT
Serial.println("D12");
Keyboard.press('d');
  }
  if(voltageD4 > 0){ // RETURN
Serial.println("D4");
Keyboard.press(KEY_RETURN);
  }
  if(voltageD7 > 0){ // R TOP
Serial.println("D7");
Keyboard.press(KEY_RIGHT_SHIFT);
  }
  if(voltageD5 > 0){ // UP
Serial.println("D5");
Keyboard.press(KEY_UP_ARROW);
  }
  if(voltageD2 > 0){ // LEFT
Serial.println("D2");
Keyboard.press(KEY_LEFT_ARROW);
  }
  if(voltageD3 > 0){ // DOWN
Serial.println("D3");
Keyboard.press(KEY_DOWN_ARROW);
  }
  if(voltageD6 > 0){ // RIGHT
Serial.println("D6");
Keyboard.press(KEY_RIGHT_ARROW);
  }

  delay(100);
  Keyboard.releaseAll();
}

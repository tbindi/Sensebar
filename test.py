mapp = {
    13: "KEY_RETURN",
    8: "KEY_BACKSPACE",
    9: "KEY_TAB",
    273: "KEY_UP_ARROW",
    274: "KEY_DOWN_ARROW",
    276: "KEY_LEFT_ARROW",
    275: "KEY_RIGHT_ARROW",
    303: "KEY_RIGHT_SHIFT",
    304: "KEY_LEFT_SHIFT",
    305: "KEY_RIGHT_CTRL",
    306: "KEY_LEFT_CTRL",
    307: "KEY_RIGHT_ALT",
    308: "KEY_LEFT_ALT",
    301: "KEY_CAPS_LOCK",
}

points = ["[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[10]", ]

leonardo = """
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
[0]
  }
  if(voltageD8 > sensor){ // UP
Serial.println("D8");
[1]
  }
  if(voltageD10 > sensor){ // DOWN
Serial.println("D10");
[2]
  }
  if(voltageD9 > sensor){ // LEFT
Serial.println("D9");
[3]
  }
  if(voltageD12 > sensor){ // RIGHT
Serial.println("D12");
[4]
  }
  if(voltageD4 > 0){ // RETURN
Serial.println("D4");
[5]
  }
  if(voltageD7 > 0){ // R TOP
Serial.println("D7");
[6]
  }
  if(voltageD5 > 0){ // UP
Serial.println("D5");
[7]
  }
  if(voltageD2 > 0){ // LEFT
Serial.println("D2");
[8]
  }
  if(voltageD3 > 0){ // DOWN
Serial.println("D3");
[9]
  }
  if(voltageD6 > 0){ // RIGHT
Serial.println("D6");
[10]
  }

  delay(100);
  Keyboard.releaseAll();
}"""

int input_pins[3] = {11, 12, 13};
int pressure_btn = 0;
int stream_btn = 1;
uint8_t pin_state[3]={0,0,0};
int output_pins[3] = {5, 6, 7};
int pin = 0;

/* Initialize CmdMessenger -- this should match PyCmdMessenger instance */
const int BAUD_RATE = 9600;

uint8_t debounce2() {
  static uint8_t y_old[3]={0,0,0}, flag[3]={0,0,0};
  uint8_t temp[3];

  for(pin=0;pin<3;pin++){
    temp[pin] = (y_old[pin] >> 2);
    y_old[pin] = y_old[pin] - temp[pin];

    if(digitalRead(input_pins[pin])){y_old[pin] = y_old[pin] + 0x3F;}

    if((y_old[pin] > 0xF0)&&(flag[pin]==0)){flag[pin]=1; pin_state[pin]=1;}
    if((y_old[pin] < 0x0F)&&(flag[pin]==1)){flag[pin]=0; pin_state[pin]=0;}
   }
}

void setup() {
    Serial.begin(BAUD_RATE);
    for(pin=0; pin<3; pin++) {
        pinMode(input_pins[pin], INPUT_PULLUP);
        pinMode(output_pins[pin], OUTPUT);
        digitalWrite(output_pins[pin], LOW);
    }
}

void loop() {
  delay(100);
  debounce2();

  for(pin=0;pin<3;pin++){
    digitalWrite(output_pins[pin], pin_state[pin]);
  }
}

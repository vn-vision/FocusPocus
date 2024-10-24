#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 13     // Digital pin connected to the DHT sensor 
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.

// Uncomment the type of sensor in use:
//#define DHTTYPE    DHT11     // DHT 11
#define DHTTYPE    DHT22     // DHT 22 (AM2302)
//#define DHTTYPE    DHT21     // DHT 21 (AM2301)

// See guide for details on sensor wiring and usage:
//   https://learn.adafruit.com/dht/overview

DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS = 800;
int fan = 5;
int heatPin1 = 16;
void setup() {
  Serial.begin(9600);
  pinMode(16, OUTPUT);
  pinMode(5, OUTPUT);
  dht.begin(); 
}

void loop() {
  /**
   * Get readings for both temperature and humidity,
   * focusing on temperature:
   * if tmp is below 
  */

  // put your main code here, to run repeatedly:
  Serial.println("Sensors activated ...");
  delay(delayMS);
  // Get temperature event and print its value.
  sensors_event_t event;
  dht.temperature().getEvent(&event);

  if (isnan(event.temperature)) {
    Serial.println(F("Error reading temperature!"));
  }
  else {
    if(event.temperature <30){
      Serial.print(F("Temperature: "));
      Serial.print(event.temperature);
      Serial.println("   fan off, heatpin1 on");
      digitalWrite(fan, LOW);
      digitalWrite(heatPin1, HIGH);
    }
    else if(event.temperature >35){
      Serial.print(F("Temperature: "));
      Serial.print(event.temperature);
      Serial.println("   fan on, heater off");
      digitalWrite(fan, HIGH);
      digitalWrite(heatPin1, LOW);
    }
  }
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    Serial.println(F("Error reading humidity!"));
  }
  else {
    Serial.print(F("Humidity: "));
    Serial.print(event.relative_humidity);
    Serial.println(F("%"));
  }
  


}


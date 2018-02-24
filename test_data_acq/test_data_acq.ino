#include <DallasTemperature.h>
#include <OneWire.h>


#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}
  
void loop() {
  sensors.requestTemperatures();
  Serial.print("temperature;1;");
  Serial.println(sensors.getTempCByIndex(0));
  delay(5000);
}

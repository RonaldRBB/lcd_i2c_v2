#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#include <ArduinoJson.h>

// ...
LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7);

unsigned long lastMessageTime = 0;
int backlightSatus = HIGH;

void setup()
{
    Serial.begin(9600);
    lcd.setBacklightPin(3, POSITIVE);
    lcd.setBacklight(HIGH);
    lcd.begin(16, 2);
    lcd.clear();
    lcd.print("Hello World!");
}
void loop()
{
    while (Serial.available() > 0)
    {
        String jsonMessage = Serial.readStringUntil('\n');
        DynamicJsonDocument jsonDoc(1024);
        deserializeJson(jsonDoc, jsonMessage);
        int cpuUsage = jsonDoc["cpu_usage"];
        int ramUsage = jsonDoc["ram_usage"];
        int cpuTemp = jsonDoc["cpu_temperature"];
        String cpuUsageStr = String(cpuUsage);
        String ramUsageStr = String(ramUsage);
        String cpuTempStr = String(cpuTemp);
        if (cpuUsageStr.length() == 1) {
            cpuUsageStr = "0" + cpuUsageStr;
        }
        if (ramUsageStr.length() == 1) {
            ramUsageStr = "0" + ramUsageStr;
        }
        if (cpuTempStr.length() == 1) {
            cpuTempStr = "0" + cpuTempStr;
        }
        lcd.clear();
        lcd.print("C:" + cpuUsageStr + " R:" + ramUsageStr + " T:" + cpuTempStr + "");
        // lcd.setCursor(0, 1);
    }
}

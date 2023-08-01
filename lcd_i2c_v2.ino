#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7);

bool isConnected = true;
unsigned long lastMessageTime = 0;
int backlightSatus = HIGH;
void blinkScreen(bool isOn)
{
    if (!isOn)
    {
        if (millis() - lastMessageTime > 1000)
        {
            lastMessageTime = millis();
            if (backlightSatus == HIGH)
            {
                lcd.setBacklight(LOW);
            }
            else
            {
                lcd.setBacklight(HIGH);
            }
        }
    }
    else
    {
        lcd.setBacklight(HIGH);
    }
}
void setup()
{
    Serial.begin(9600);
    lcd.setBacklightPin(3, POSITIVE);
    lcd.setBacklight(HIGH);
    lcd.begin(16, 2);
    lcd.clear();
}
void loop()
{
    isConnected = false;
    while (Serial.available() > 0)
    {
        String message = Serial.readStringUntil('\n');
        lcd.clear();
        lcd.print(message);
        isConnected = true;
    }
    // blinkScreen(isConnected);
}

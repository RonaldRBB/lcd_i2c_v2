#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 2, 1, 0, 4, 5, 6, 7);
String getDate(String data)
{
    String year = data.substring(0, 4);
    String month = data.substring(4, 6);
    String day = data.substring(6, 8);
    String hour = data.substring(8, 10);
    String minute = data.substring(10, 12);
    return year + "-" + month + "-" + day + " " + hour + ":" + minute;
}
String getCpuUsage(String data)
{
    String cpu_usage = data.substring(12, 14);
    return cpu_usage;
}
String getRamUsage(String data)
{
    String ram_usage = data.substring(14, 16);
    return ram_usage;
}
String getCpuTemp(String data)
{
    String cpu_temp = data.substring(16, 18);
    return cpu_temp;
}
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
        String data = Serial.readStringUntil('\n');
        String date = getDate(data);
        String cpu_usage = getCpuUsage(data);
        String ram_usage = getRamUsage(data);
        String cpu_temp = getCpuTemp(data);
        lcd.setCursor(0, 0);
        lcd.print(date);
        lcd.setCursor(0, 1);
        lcd.print("C:" + cpu_usage + "  R:" + ram_usage + "  T:" + cpu_temp);
    }
}

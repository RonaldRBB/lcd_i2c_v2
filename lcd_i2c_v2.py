import serial
import time
import subprocess
import psutil

def setup_serial():
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    time.sleep(1)
    return arduino

def send_message(arduino, message):
    arduino.write(message.encode())

def close_serial(arduino):
    arduino.close()

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def main():
    arduino = setup_serial()
    try:
        while True:
            cpu_usage = get_cpu_usage()
            mensaje = f"CPU: {cpu_usage:.2f}%\n"
            send_message(arduino, mensaje)
            time.sleep(1)
    except KeyboardInterrupt:
        exit()
    finally:
        close_serial(arduino)

if __name__ == "__main__":
    main()

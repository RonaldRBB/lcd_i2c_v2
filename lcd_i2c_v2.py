import time
import serial
from classes.pc_info import PcInfo


def setup_serial():
    """Setup serial communication with Arduino."""
    try:
        arduino = serial.Serial("/dev/ttyUSB0", 9600)
        time.sleep(1)
        return arduino
    except serial.SerialException as e:
        print("Error al establecer la comunicación con el Arduino:", e)
        return None


def send_message(arduino, message):
    """Send message to Arduino."""
    if arduino is not None:
        arduino.write(message.encode())


def close_serial(arduino):
    """Close serial communication with Arduino."""
    if arduino is not None:
        arduino.close()


def get_cpu_usage():
    """Get CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage


def main():
    """Main function."""
    arduino = setup_serial()
    pc_info = PcInfo()
    while True:
        try:
            if arduino is None:
                arduino = setup_serial()
                if arduino is None:
                    time.sleep(1)
                    continue
            cpu_usage = pc_info.get_all_info()
            mensaje = f"{cpu_usage}\n"
            send_message(arduino, mensaje)
            time.sleep(1)
        except KeyboardInterrupt:
            break
        except serial.SerialException:
            print("Arduino desconectado. Esperando a que sea conectado nuevamente...")
            arduino = None


if __name__ == "__main__":
    main()

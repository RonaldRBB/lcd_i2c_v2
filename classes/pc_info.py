"""PC info class."""
import psutil
import os
import datetime


class PcInfo:
    """PC info class."""

    def __init__(self):
        """Constructor."""
        self.__cpu_name = os.environ.get("cpu_name")

    def get_device_datetime(self):
        """Get current device datetime."""
        current_datetime = datetime.datetime.now()
        return current_datetime.strftime("%Y%m%d%H%M")

    def get_cpu_usage(self):
        """Get CPU usage."""
        cpu_usage = int(psutil.cpu_percent(interval=1))
        return cpu_usage

    def get_ram_usage(self):
        """Get RAM usage."""
        ram_usage = int(psutil.virtual_memory().percent)
        print("RAM usage: ", ram_usage)
        return ram_usage

    def get_disk_usage(self):
        """Get disk usage."""
        disk_usage = int(psutil.disk_usage("/").percent)
        return disk_usage

    def get_cpu_temperature(self):
        """Get CPU temperature."""
        temperatures = psutil.sensors_temperatures()
        if self.__cpu_name in temperatures:
            temperature = int(temperatures[self.__cpu_name][0].current)
            return temperature
        else:
            return "N/A"

    def get_all_info(self):
        """Get all info."""
        device_datetime = str(self.get_device_datetime()).replace(".", "")
        cpu_usage = str(self.get_cpu_usage()).replace(".", "")
        ram_usage = str(self.get_ram_usage()).replace(".", "")
        cpu_temperature = str(self.get_cpu_temperature()).replace(".", "")
        disk_usage = str(self.get_disk_usage()).replace(".", "")
        return f"{device_datetime}{cpu_usage}{ram_usage}{cpu_temperature}{disk_usage}"

    def elements_with_temps(self):
        """Get elements with temperature."""
        temperatures = psutil.sensors_temperatures()
        for sensor, data in temperatures.items():
            print(f"Sensor: {sensor}")
            for entry in data:
                label = entry.label if entry.label else "N/A"
                current_temp = entry.current if entry.current else "N/A"
                high = entry.high if entry.high else "N/A"
                critical = entry.critical if entry.critical else "N/A"
                print(f"  Label: {label}")
                print(f"  Current Temperature: {current_temp}")
                print(f"  High Temperature: {high}")
                print(f"  Critical Temperature: {critical}")
                print("-" * 30)

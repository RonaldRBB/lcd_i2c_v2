"""PC info class."""
import psutil
import os


class PcInfo:
    """PC info class."""

    def __init__(self):
        """Constructor."""
        self.__cpu_name = os.environ.get("cpu_name")

    def get_cpu_usage(self):
        """Get CPU usage."""
        cpu_usage = psutil.cpu_percent(interval=1)
        return cpu_usage

    def get_ram_usage(self):
        """Get RAM usage."""
        ram_usage = psutil.virtual_memory().percent
        return ram_usage

    def get_disk_usage(self):
        """Get disk usage."""
        disk_usage = psutil.disk_usage("/").percent
        return disk_usage

    def get_cpu_temperature(self):
        """Get CPU temperature."""
        temperatures = psutil.sensors_temperatures()
        if self.__cpu_name in temperatures:
            temperature = temperatures[self.__cpu_name][0].current
            return temperature
        else:
            return "N/A"

    def get_all_info(self):
        """Get all info."""
        cpu_usage = self.get_cpu_usage()
        ram_usage = self.get_ram_usage()
        disk_usage = self.get_disk_usage()
        cpu_temperature = self.get_cpu_temperature()
        info = {
            "cpu_usage": cpu_usage,
            "ram_usage": ram_usage,
            "disk_usage": disk_usage,
            "cpu_temperature": cpu_temperature,
        }
        return info

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

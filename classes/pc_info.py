"""PC info class."""
import psutil


class PcInfo:
    """PC info class."""

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

    def get_temperature(self):
        """Get temperature."""
        temperature = psutil.sensors_temperatures()["coretemp"][0].current
        return temperature

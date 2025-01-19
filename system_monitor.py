import psutil
import time
from datetime import datetime

# Thresholds for alerts
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def display_metrics():
    """Display system performance metrics."""
    print("\nSystem Monitoring Dashboard")
    print("-" * 30)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")
    if cpu_percent > CPU_THRESHOLD:
        print("ALERT: High CPU Usage!")

    # Memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}% (Used: {memory.used // (1024**2)} MB)")
    if memory.percent > MEMORY_THRESHOLD:
        print("ALERT: High Memory Usage!")

    # Disk usage
    disk = psutil.disk_usage('/')
    print(f"Disk Usage: {disk.percent}% (Free: {disk.free // (1024**3)} GB)")
    if disk.percent > DISK_THRESHOLD:
        print("ALERT: Low Disk Space!")

    # Network activity
    net = psutil.net_io_counters()
    print(f"Data Sent: {net.bytes_sent // (1024**2)} MB, Received: {net.bytes_recv // (1024**2)} MB")

def main():
    """Main monitoring loop with graceful exit."""
    print("Starting System Monitoring Dashboard...")
    print("Press 'Ctrl + C' to stop monitoring.\n")

    try:
        while True:
            display_metrics()
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Goodbye!")

if __name__ == "__main__":
    main()

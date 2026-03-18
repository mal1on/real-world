import csv
import os
import time

import psutil


def comp_metrics_get():
    """Get computer metrics such as CPU usage, memory usage, and disk usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    vm = psutil.virtual_memory()
    du = psutil.disk_usage("/")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return {
        "timestamp": timestamp,
        "cpu_usage": cpu_usage,
        "memory_total_mb": vm.total / (1024 * 1024),
        "memory_used_mb": vm.used / (1024 * 1024),
        "disk_total_gb": du.total / (1024 * 1024 * 1024),
        "disk_used_gb": du.used / (1024 * 1024 * 1024),
    }


if __name__ == "__main__":
    csv_path = "computer_metrics.csv"
    fieldnames = [
        "timestamp",
        "cpu_usage",
        "memory_total_mb",
        "memory_used_mb",
        "disk_total_gb",
        "disk_used_gb",
    ]

    file_exists = os.path.exists(csv_path)
    with open(csv_path, mode="a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header only if file is new/empty
        if not file_exists or os.stat(csv_path).st_size == 0:
            writer.writeheader()

        metrics = comp_metrics_get()
        writer.writerow(metrics)

    print(f"Metrics recorded at {metrics['timestamp']}")

import csv
import os
import time
import threading
from datetime import datetime, timezone
import pygetwindow as gw


class ActivityTracker:

    def __init__(self, interval=5):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOG_DIR = os.path.join(BASE_DIR, "logs")

        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self.window_log = os.path.join(self.LOG_DIR, "windows.csv")
        self.interval = interval
        self.previous_window = None

        if not os.path.exists(self.window_log):
            with open(self.window_log, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["local_time", "utc_time", "unix_time", "active_window"])

    def get_timestamps(self):
        unix_time = time.time()
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return local_time, utc_time, unix_time

    def track_activity(self):
        while True:
            time.sleep(self.interval)
            current_window = gw.getActiveWindowTitle()

            if current_window != self.previous_window:
                self.previous_window = current_window
                local_time, utc_time, unix_time = self.get_timestamps()

                with open(self.window_log, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        local_time,
                        utc_time,
                        unix_time,
                        current_window
                    ])

    def start(self):
        thread = threading.Thread(target=self.track_activity)
        thread.daemon = True
        thread.start()
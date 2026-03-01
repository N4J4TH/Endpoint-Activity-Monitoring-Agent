import csv
import os
import time
from datetime import datetime, timezone
from pynput import keyboard


class KeyLogger:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOG_DIR = os.path.join(BASE_DIR, "logs")

        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self.key_log = os.path.join(self.LOG_DIR, "keystrokes.csv")
        self.alert_log = os.path.join(self.LOG_DIR, "alerts.csv")

        self.key_times = []

        # Create CSV headers
        if not os.path.exists(self.key_log):
            with open(self.key_log, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["local_time", "utc_time", "unix_time", "key"])

        if not os.path.exists(self.alert_log):
            with open(self.alert_log, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["local_time", "utc_time", "unix_time", "alert_type", "details"])

        self.listener = keyboard.Listener(on_press=self.when_press)

    def get_timestamps(self):
        unix_time = time.time()
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return local_time, utc_time, unix_time

    def when_press(self, key):
        local_time, utc_time, unix_time = self.get_timestamps()

        self.key_times.append(unix_time)
        self.key_times = [t for t in self.key_times if unix_time - t <= 1]

        # High keystroke rate detection
        if len(self.key_times) > 50:
            with open(self.alert_log, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    local_time,
                    utc_time,
                    unix_time,
                    "High Keystroke Rate",
                    "More than 50 keys pressed within 1 second"
                ])

        try:
            key_value = key.char
        except AttributeError:
            key_value = str(key)

        with open(self.key_log, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                local_time,
                utc_time,
                unix_time,
                key_value
            ])

    def start(self):
        self.listener.start()

    def join(self):
        self.listener.join()
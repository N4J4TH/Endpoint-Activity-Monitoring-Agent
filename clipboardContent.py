import csv
import os
import time
import threading
from datetime import datetime, timezone
import pyperclip


class ClipboardLogger:

    def __init__(self, interval=5):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.LOG_DIR = os.path.join(BASE_DIR, "logs")

        if not os.path.exists(self.LOG_DIR):
            os.makedirs(self.LOG_DIR)

        self.clipboard_log = os.path.join(self.LOG_DIR, "clipboard.csv")
        self.interval = interval
        self.recent_value = ""

        if not os.path.exists(self.clipboard_log):
            with open(self.clipboard_log, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["local_time", "utc_time", "unix_time", "clipboard_content"])

    def get_timestamps(self):
        unix_time = time.time()
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return local_time, utc_time, unix_time

    def log_clipboard(self):
        while True:
            time.sleep(self.interval)
            current_value = pyperclip.paste()

            if current_value != self.recent_value:
                self.recent_value = current_value
                local_time, utc_time, unix_time = self.get_timestamps()

                with open(self.clipboard_log, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        local_time,
                        utc_time,
                        unix_time,
                        self.recent_value
                    ])

    def start(self):
        thread = threading.Thread(target=self.log_clipboard)
        thread.daemon = True
        thread.start()
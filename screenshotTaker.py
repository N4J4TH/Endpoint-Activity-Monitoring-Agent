import os
import time
import threading
from PIL import ImageGrab


class ScreenCapture:

    def __init__(self, interval=60):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.SCREEN_DIR = os.path.join(BASE_DIR, "screenshots")

        if not os.path.exists(self.SCREEN_DIR):
            os.makedirs(self.SCREEN_DIR)

        self.interval = interval

    def capture_screenshot(self):
        while True:
            time.sleep(self.interval)
            screenshot = ImageGrab.grab()
            filename = os.path.join(
                self.SCREEN_DIR,
                f"screenshot_{int(time.time())}.png"
            )
            screenshot.save(filename)

    def start(self):
        thread = threading.Thread(target=self.capture_screenshot)
        thread.daemon = True
        thread.start()
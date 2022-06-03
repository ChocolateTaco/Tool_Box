import time
import datetime

class TwentyFive():
    def __init__(self):
        self._total_seconds =  25 * 60

    def startTimer(self):
        while self._total_seconds > 0:
            timer = datetime.timedelta(seconds = self._total_seconds)
            # minutes = self._total_seconds // 60
            # seconds = self._total_seconds % 60
            # print(f"{minutes}:{seconds}", end="\r")
            print(timer, end="\r")
            time.sleep(1)       # waits 1 second
            self._total_seconds -= 1
        
        print("5 MINUTE BREAK TIME!")

def main():
    apple = TwentyFive()
    apple.startTimer()

if __name__ == "__main__":
    main()

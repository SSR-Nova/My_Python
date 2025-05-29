import time
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def start(self):
        for i in range(self.seconds):          
            print(self.seconds - i)
            time.sleep(1)
        print('Время вышло!')


timer = Timer(3)
timer.start()
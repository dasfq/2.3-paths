import time

class Timer():
    def __init__(self):
        pass

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.interval = self.stop - self.start
        print(f'Старт: {self.start}, Остановка: {self.stop}, Порачено времени: {self.interval}')
        return False

with Timer as t:
    for i in range(10):
        i = i*i
        print(i)

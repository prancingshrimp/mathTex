import time

class TIME_COUNTER(object):
    def __init__(self):
        self.start_time = time.time()


    def stop(self):
        self.stop_time = time.time()


    def print_result(self):
        print("Elapsed time:", round(self.stop_time - self.start_time, 4), 'sec')

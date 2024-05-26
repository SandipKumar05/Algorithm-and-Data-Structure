import time
from threading import Lock

class FixedWindow:
    def __init__(self, rate, window_size):
        self.rate = rate
        self.window_size = window_size
        self.requests = 0
        self.window_start = time.time()
        self.lock = Lock()

    def allow_request(self):
        with self.lock:
            current_time = time.time()
            if current_time - self.window_start >= self.window_size:
                self.window_start = current_time
                self.requests = 0

            if self.requests < self.rate:
                self.requests += 1
                return True
            return False

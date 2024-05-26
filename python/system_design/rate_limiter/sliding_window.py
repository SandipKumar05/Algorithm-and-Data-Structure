import time
from collections import deque
from threading import Lock

class SlidingWindow:
    def __init__(self, rate, window_size):
        self.rate = rate
        self.window_size = window_size
        self.requests = deque()
        self.lock = Lock()

    def allow_request(self):
        with self.lock:
            current_time = time.time()
            while self.requests and current_time - self.requests[0] > self.window_size:
                self.requests.popleft()

            if len(self.requests) < self.rate:
                self.requests.append(current_time)
                return True
            return False

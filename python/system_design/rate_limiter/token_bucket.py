import time
from threading import Lock

class TokenBucket:
    def __init__(self, rate, capacity) -> None:
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()
        self.lock = Lock()

    def allow_req(self):
        with self.lock:
            current_time = time.time()
            elapsed_time = current_time - self.last_refill_time
            self.tokens = min(self.capacity, self.tokens+self.rate*elapsed_time)
            self.last_refill_time = current_time

            if self.tokens > 1:
                self.token -=1
                return True
            return False
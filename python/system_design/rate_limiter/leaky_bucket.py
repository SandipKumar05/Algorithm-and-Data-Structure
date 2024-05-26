import time
from collections import deque
from threading import Lock

class LeakyBucket:
    def __init__(self, leaky_rate, capacity):
        self.capacity = capacity
        self.leaky_rate = leaky_rate
        self.queue = deque()
        self.lock = Lock()

    def allow_req(self):
        with self.lock:
            curr_time = time.time()
            while self.queue and curr_time - self.queue[0] > self.leaky_rate:
                self.queue.popleft()
            if len(self.queue) < self.capacity:
                self.queue.append(curr_time)
                return True
            return False
        


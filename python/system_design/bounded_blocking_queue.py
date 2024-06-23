import threading
from collections import deque
import time
import random

class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.queue = deque()
        self.lock = threading.Lock()
        self.capacity = capacity
        self.condition1 = threading.Condition(self.lock)
        self.condition2 = threading.Condition(self.lock)

    def enqueue(self, msg):
        with self.condition1:
            while len(self.queue) == self.capacity:
                # release lock and sleep, reacquires lock when waken up
                # this prevent busy waiting
                self.condition1.wait()
            self.queue.append(msg)
            # waken up waiting threads
            self.condition2.notify()
    
    def dequeue(self):
        with self.condition2:
            while len(self.queue) == 0:
                self.condition2.wait()
            msg = self.queue.popleft()
            self.condition1.notify()
            return msg

def producer(queue, id):
    for i in range(5):
        item = f"item-{id}-{i}"
        queue.enqueue(item)
        print(f"producer {id} produce {item}")
        time.sleep(random.uniform(0.1,0.5))

def consumer(queue, id):
    for i in range(5):
        item = queue.dequeue()
        print(f"consumer {id} consumed {item}")
        time.sleep(random.uniform(0.1,0.5))

def main():
    q = BoundedBlockingQueue(5)
    p = [threading.Thread(target=producer, args=(q, i)) for i in range(2)]
    c = [threading.Thread(target=consumer, args=(q,i)) for i in range(2)]

    t = p + c
    for i in t:
        i.start()
    for i in t:
        i.join()

if __name__ == "__main__":
    main()

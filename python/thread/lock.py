import threading
import time

counter = 0

def incre():
    global counter

    for i in range(100000000):
        counter+=1

t1= threading.Thread(target=incre)
t2= threading.Thread(target=incre)
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)
import threading
import time
import random
def producer():
    while True:
        condition.acquire()
        if len(data) >= 5:
            print('Producer : waiting...')
            condition.wait()
        else:
            data.append(random.randint(1, 100))
            print('Storage', data)
            time.sleep(1)
        condition.notify()
        condition.release()

def consumer():
    while True:
        condition.acquire()
        if not data:
            print('Consumer : waiting...')
            condition.wait()
        else:
            print('Consumer consume :', data.pop(0))
            print('Storage', data)
            time.sleep(1)
        condition.notify()
        condition.release()

condition = threading.Condition()
data = []

p = threading.Thread(name='product', target=producer)
c = threading.Thread(name='consumer', target=consumer)

p.start()
c.start()
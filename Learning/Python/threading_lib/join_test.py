import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

w = threading.Thread(name='worker', target=worker)
w.start()
print('start join')
print(w.is_alive())
w.join(1)
print('end join')
import threading
import time

semaphore = threading.BoundedSemaphore(3)

def func():
    if semaphore.acquire():
        print(threading.current_thread().getName(), 'locked')
        print('Working...')
        time.sleep(2)
        semaphore.release()
        print(threading.current_thread().getName(), 'unlocked')

for i in range(5):
    t = threading.Thread(target=func)
    t.start()
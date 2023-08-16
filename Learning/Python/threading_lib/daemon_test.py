import threading
import time

def daemonFunc():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')

def non_daemon():
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')

d = threading.Thread(name='daemon', target=daemonFunc)
d.setDaemon(True)
nd = threading.Thread(name='Non-daemon', target=non_daemon)

d.start()
nd.start()
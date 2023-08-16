import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global data
        data_lock.acquire()
        # data_lock.acquire() dead lock
        data += 5
        print(f'data={data}')
        data_lock.release()

data = 10
data_lock = threading.Lock()
ts = []
for t in range(10):
    t = MyThread()
    ts.append(t)

for t in ts:
    t.start()

for t in ts:
    t.join()
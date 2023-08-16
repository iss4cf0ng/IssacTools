import threading, time, random, queue

buffer_size = 10
q = queue.Queue(buffer_size)

def producer():
    while True:
        if not q.full():
            item = random.randint(1, 100)
            q.put(item)
            print(f'Producer putting : {str(item):2s} : queue count {str(q.qsize())}')
            time.sleep(2)

def consumer():
    while True:
        if not q.empty():
            item = q.get()
            print(f'Consumer getting {str(item):2s} : queue count {q.qsize()}')
            time.sleep(2)

p = threading.Thread(name='producer', target=producer)
c = threading.Thread(name='consumer', target=consumer)
p.start()
time.sleep(2)
c.start()
time.sleep(2)
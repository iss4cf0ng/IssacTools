import random, time
import threading

def waiter(event, loop):
    for i in range(loop):
        print(f'{i+1}')
        event.wait()
        print(f'Waiting time : {time.ctime()}')
        event.clear()
        print()

def setter(event, loop):
    for i in range(loop):
        time.sleep(random.randint(2, 5))
        event.set()

event = threading.Event()
loop = random.randint(3, 6)

w = threading.Thread(target=waiter, args=[event, loop])
w.start()
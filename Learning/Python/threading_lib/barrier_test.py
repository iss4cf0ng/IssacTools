import random, time
import threading

def player():
    name = threading.current_thread().getName()
    time.sleep(random.randint(2, 5))
    print(f'{name} Approach time : {time.ctime()}')
    b.wait()

b = threading.Barrier(4)
print('Start!')
for i in range(4):
    t = threading.Thread(target=player)
    t.start()

for i in range(4):
    t.join()
print('Finished!')
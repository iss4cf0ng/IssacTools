import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print(threading.Thread.getName(self))
        print('Hello Python')

a = MyThread()
a.run()
a.run()
b = MyThread()
b.start()
import threading
from datetime import datetime

class Thread1(threading.Thread):
    def run(self) -> None:
        for i in range(1000):
            now = datetime.now()
            print(now)

class Thread2(threading.Thread):
    def run(self) -> None:
        for i in range(10000):
            print(i)

t1 = Thread1()
t1.start()
t2 = Thread2()
t2.daemon = True
t2.start()
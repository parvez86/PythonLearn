from threading import Thread
from time import sleep


class MyThread(Thread):
    def run(self):
        i = 0
        while i <= 10:
            print(i)
            sleep(1)
            i += 1


t = MyThread()
t.start()

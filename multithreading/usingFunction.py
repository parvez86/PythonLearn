from threading import *
from time import sleep


def displayNumbers():
    i = 0
    print(current_thread().getName())
    while i <= 10:
        print(i)
        sleep(1)
        i += 1


print(current_thread().getName())
t = Thread(target=displayNumbers)
# print(dir(t))
t.start()
thread_func = ['daemon', 'getName', 'ident', 'isAlive', 'isDaemon',
               'is_alive', 'join', 'name', 'native_id', 'run',
               'setDaemon', 'setName', 'start']

print(len(thread_func))
print('daemon:', t.daemon)
print('getName:', t.getName())
print('ident:', t.ident)
# print(t.isAlive())
print('is_alive: ', t.is_alive())
print('isDaemon: ', t.isDaemon())
print('native_id: ', t.native_id)
print('setName: ', t.setName('DisplayNumbers'))
print('name: ', t.name)

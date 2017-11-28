#coding=utf-8
import threading
from time import ctime,sleep


def music():
    for i in range(2):
        print "I was listening to %s" %(ctime())
        sleep(1)

def move():
    for i in range(4):
        print "I was at the %s" %(ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=())
threads.append(t1)
t2 = threading.Thread(target=move,args=())
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print "all over %s" % ctime()
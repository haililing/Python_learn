import threading
import time

def task():
    print("子线程1开始执行")
    time.sleep(3)
    print("子线程1执行结束")

def task1():
    print("子线程2开始执行")
    time.sleep(3)
    print("子线程2执行结束")


print("主线程开始")

thread = threading.Thread(target=task)
thread1 = threading.Thread(target=task1)

thread.start()
thread1.start()

thread.join()
thread1.join()

print("主线程结束")
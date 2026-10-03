import threading
import time

def func1(name):
    print(f"{name}开始")
    time.sleep(2)
    print(f"{name}完成")

def func2(name):
    print(f"{name}开始")
    time.sleep(3)
    print(f"{name}完成")

def func3(name):
    print(f"{name}开始")
    time.sleep(1)
    print(f"{name}完成")

start_time = time.time()

thread1 = threading.Thread(target=func1, args=("任务1",))
thread2 = threading.Thread(target=func2, args=("任务2",))
thread3 = threading.Thread(target=func3, args=("任务3",))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("全部任务完成")
end_time = time.time()
print(f'总耗时:{end_time - start_time:.0f}')
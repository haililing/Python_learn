import threading
import time


def task(name):
    print(f"{name} 开始")

    time.sleep(2)

    print(f"{name} 完成")


start_time = time.time()

thread1 = threading.Thread(
    target=task,
    args=("任务A",)
)

thread2 = threading.Thread(
    target=task,
    args=("任务B",)
)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"总耗时：{end_time - start_time:.2f} 秒")
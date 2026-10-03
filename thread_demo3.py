import threading
import time

tickets = 3

users = 10

threads = []

barrier = threading.Barrier(users)

lock = threading.Lock()

def buy_tickets():
    global tickets

    barrier.wait()

    with lock:
        if tickets > 0:
            time.sleep(0.1)
            tickets -= 1
            print("成功")
        else:
            print("失败")

for _ in range(users):
    thread = threading.Thread(target=buy_tickets)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(tickets)
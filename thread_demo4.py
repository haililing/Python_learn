import time
from concurrent.futures import (ThreadPoolExecutor,as_completed)
import threading

tickets = 3
user_count = 10
futures = []
success_count = 0
fail_count = 0
lock = threading.Lock()
barrier = threading.Barrier(user_count)

def buy_tickets(user_id):
    global tickets
    thread_name = threading.current_thread().name
    barrier.wait()

    print(
        f"用户{user_id}开始抢票"
        f"当前线程:{thread_name}"
    )

    time.sleep(1)

    with lock:
        if tickets > 0:
            time.sleep(0.1)
            tickets -= 1

            print(
                f"用户{user_id}抢票成功,还剩余{tickets}张票"
                f"线程:{thread_name}"
            )
            return {"user_id":user_id, "succesed":True}

        else:
            print(f"用户{user_id}抢票失败")

            return {"user_id":user_id, "succesed":False}

with ThreadPoolExecutor(max_workers=user_count) as executor:
    for user_id in range(1,user_count+1):
        future = executor.submit(buy_tickets, user_id)
        futures.append(future)

for future in as_completed(futures):
    result = future.result()
    if result["succesed"]:
        success_count += 1
    else:
        fail_count += 1

    print(success_count)
    print(fail_count)
    print(tickets)
import threading

lock = threading.Lock()

count = 0

def add():
    global count
    with lock:
        count += 1

threads = []

for i in range(5):
    thread = threading.Thread(target = add)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(count)
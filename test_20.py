import threading

def task():
    print("task")

thread = threading.Thread(target=task)

thread.start()
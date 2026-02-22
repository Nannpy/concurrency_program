import threading
import time

def task(name, delay):
    print(f"Start {name}")
    time.sleep(delay)
    print(f"End {name}")

t1 = threading.Thread(target=task, args=("A", 2))
t2 = threading.Thread(target=task, args=("B", 1))
t3 = threading.Thread(target=task, args=("C", 3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All done")
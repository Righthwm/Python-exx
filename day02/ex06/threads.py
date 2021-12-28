import _thread
import time

def thread_function(index):
    print("Thread " +str(index)+": started")
    time.sleep(index*60)
    print("Thread " +str(index)+": finished")

if __name__ == "__main__":
    for index in range(1,6):
        _thread.start_new_thread(thread_function, (index,))
    input()

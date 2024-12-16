"""
信号量的基本概念
threading.Semaphore：在 Python 中，信号量是一个计数器，表示资源的可用数量。
    当线程调用 acquire() 时，信号量的计数减 1。
    当线程调用 release() 时，信号量的计数加 1。
    当计数为 0 时，acquire() 会阻塞线程，直到信号量变为正数。
threading.BoundedSemaphore：类似于 Semaphore，但防止计数超过初始值。如果调用了过多的 release()，会抛出异常。

信号量的使用场景
    资源访问限制：比如数据库连接池、线程池、文件访问等。
    流量控制：限制同时执行的线程数量，避免系统资源耗尽。
    并发限制：对共享资源的访问进行限制。

信号量的注意事项
避免过多的 release()：
    如果 release() 的次数超过 acquire()，可能会导致信号量计数不正确，建议使用 BoundedSemaphore。
死锁问题：
    如果一个线程 acquire() 后没有及时调用 release()，其他线程可能会永远等待。
适用场景：
    信号量适用于需要限制并发访问数量的场景，比如 I/O 资源、连接池等。
"""
import random
import threading
import time
# 限制并发下载文件
# 假设有多个线程下载文件，但同时只能进行 3 个下载。
semaphore = threading.Semaphore(3)

def download_file(file_id):
    print(f"File-{file_id}: Waiting to download...")
    with semaphore:
        print(f"File-{file_id}: Downloading...")
        time.sleep(random.randint(1,5))  # 模拟下载耗时
        print(f"File-{file_id}: Download completed.")

file_ids = range(1, 7)

threads = [threading.Thread(target=download_file, args=(file_id,)) for file_id in file_ids]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All files downloaded.")

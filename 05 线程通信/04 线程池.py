"""
线程池的优势
    线程复用：避免频繁创建和销毁线程，提高性能。
    任务管理：线程池可以轻松地调度和管理任务，控制并发数量。
    代码简洁：线程池封装了线程的创建、启动和销毁逻辑，使代码更清晰。

线程池的基本用法:
concurrent.futures.ThreadPoolExecutor 是 Python 中线程池的实现。其常用方法包括：
    submit(fn, *args, **kwargs)：将任务提交到线程池中，返回一个 Future 对象。
    map(func, iterable)：将可迭代对象中的每个元素作为参数调用 func，返回结果的迭代器。
    shutdown(wait=True)：关闭线程池，释放资源。
"""

"""
注意事项
避免任务阻塞
    如果线程池中的任务存在 I/O 阻塞，可以考虑使用 concurrent.futures.ProcessPoolExecutor 或异步编程（asyncio）。
线程数量控制
    线程池的大小 (max_workers) 需要根据任务的性质和计算资源合理设置。
    CPU 密集型任务：max_workers 通常设置为 CPU 核心数。
    I/O 密集型任务：max_workers 可以适当设置得更大。
异常处理
    提交的任务可能会抛出异常，使用 future.exception() 可以捕获。
"""

import time
from concurrent.futures import ThreadPoolExecutor

# 创建一个线程池对象，并且指定线程池中最大的线程数为3
executor = ThreadPoolExecutor(max_workers=3)
def task(n):
    print(f"Task {n} is running")
    time.sleep(1)
    print(f"Task {n} is completed")
    return n * 2
# 提交多个任务
futures = [executor.submit(task, i) for i in range(5)]
# 获取任务的结果
for future in futures:
    # future.done() # 检查任务是否完成
    # future.cancle() # 取消执行任务，任务没有放入线程池才能取消成功
    # future.result() # 获取任务执行结果
    print(f"Result: {future.result()}")
# 关闭线程池
executor.shutdown()


# 使用 map 方法
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))
    for result in results:
        print(f"Result: {result}")

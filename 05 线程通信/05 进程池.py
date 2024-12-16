"""
进程池的主要功能
    任务并发：通过分发任务到多个进程，充分利用多核 CPU 的计算能力。
    资源复用：进程池复用一组进程，避免频繁创建和销毁进程的开销。
    接口简洁：进程池封装了进程的创建、管理和销毁逻辑，简化并发代码。

进程池的两种实现
    multiprocessing.Pool：标准库中的进程池接口，功能强大但语法相对复杂。
    concurrent.futures.ProcessPoolExecutor：更高层次的抽象，语法类似于线程池。

注意事项
进程池大小：
    CPU 密集型任务：进程数量建议设置为 CPU 核心数。
    I/O 密集型任务：进程数量可以设置得更大。
避免共享状态：
    多进程间无法直接共享全局变量，需通过 multiprocessing.Manager 或 Queue 等方式实现进程间通信。
调试困难：
    多进程代码可能难以调试，尽量避免复杂逻辑。
避免 GIL 的限制：
    对于计算密集型任务，进程池优于线程池，因为它可以绕过 GIL。

"""
import math
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
import os

def square(n):
    print(f"Process {os.getpid()} computing square of {n}")
    return n * n

def cube(n):
    print(f"Process {os.getpid()} computing cube of {n}")
    return n ** 3

if __name__ == '__main__':
    """
    使用 multiprocessing.Pool
    常用方法
        map(func, iterable)：将 iterable 中的每个元素作为参数调用 func，返回结果列表。
        apply(func, args)：在池中执行单个函数调用，等待结果返回。
        apply_async(func, args)：异步调用单个函数，返回 AsyncResult 对象。
        starmap(func, iterable)：类似于 map，但参数以元组形式传递。
    """
    with Pool(processes=4) as pool:  # 创建一个包含 4 个进程的进程池
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)  # 将任务分配到进程池
    print(f"Results: {results}")
    """
    使用 concurrent.futures.ProcessPoolExecutor
    """
    with ProcessPoolExecutor(max_workers=4) as executor:
        numbers = [math.pi, 2, 3, 4, 5]
        results = [executor.map(cube, numbers)]

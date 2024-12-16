"""
threading.local() 提供了一种简单的方式来为每个线程维护独立的数据空间，避免线程间的数据竞争问题。
它特别适合在多线程程序中存储线程相关的上下文数据，如用户信息、数据库连接等。
在多线程编程中使用 threading.local 可以有效提高代码的可维护性和可靠性。

线程退出时的数据清理
    每个线程的数据只在该线程的生命周期内有效。
    当线程退出时，与该线程相关的数据会自动清除。
线程安全
    threading.local 是线程安全的，不需要额外的加锁操作。
适用于多线程，不适用于协程
    threading.local 是为线程设计的，不适用于异步编程中的协程。如果需要在协程中实现类似功能，可以使用 contextvars 模块。
"""

import threading
import logging

# 设置日志格式
logging.basicConfig(level=logging.INFO, format='%(message)s')

# 使用 threading.local() 存储每个线程的日志上下文
log_context = threading.local()

def set_log_context(task_id):
    log_context.task_id = task_id

def log_message(message):
    task_id = getattr(log_context, "task_id", "Unknown")
    logging.info(f"[Task-{task_id}] {message}")

def worker(task_id):
    set_log_context(task_id)
    log_message("Starting task")
    log_message("Processing data")
    log_message("Task completed")

if __name__ == '__main__':
    threads = [
        threading.Thread(target=worker, args=(str(i)*3,), name=f"Thread-{i}")
        for i in range(3)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


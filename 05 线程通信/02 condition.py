"""
Condition 的工作原理
Condition 对象提供了如下关键方法：
    wait()：让当前线程等待，直到另一个线程调用 notify() 或 notify_all() 通知它继续。
    notify()：通知等待该条件的一个线程继续执行。
    notify_all()：通知等待该条件的所有线程继续执行。
    acquire() 和 release()：通常与锁一起使用，用来确保对条件的访问是线程安全的。

使用 Condition 实现线程间协调
Condition 允许多个线程等待某些条件，直到条件满足时才开始执行。最常见地使用场景是在生产者-消费者模式中，生产者线程会在生产数据时通知消费者线程，消费者线程在消费数据时通知生产者线程。

Condition 的常用方法
    acquire()：请求锁定条件变量，确保对条件的独占访问。
    release()：释放锁。
    wait(timeout=None)：使当前线程等待，直到收到通知或者超时。
    notify(n=1)：通知一个等待的线程，默认通知一个线程。
    notify_all()：通知所有等待的线程。

Condition 与 Event 的区别
    Condition 需要与锁（Lock 或 RLock）一起使用，确保线程对共享资源的互斥访问。它适用于需要多个线程等待和通知的场景。
    Event 是一个简单的信号机制，通常用于单个线程等待某个事件发生，适用于多个线程等待同一个事件的场景。
"""

import threading
import time
import random

# 创建条件变量
condition = threading.Condition()

# 数据共享队列
queue = []

# 最大队列大小
MAX_SIZE = 10

def producer():
    global queue
    for i in range(3):
        with condition:  # 获取条件锁
            if len(queue) > MAX_SIZE:  # 如果队列超过最大值，等待消费者消费数据
                print("Queue is full, producer is waiting...")
                condition.wait()  # 等待消费者消费数据
            items = [random.randint(1, 100) for i in range(5)] # 生产5个产品
            queue.extend(items)
            print(f"Produced {items}, Queue size: {len(queue)}")
            condition.notify()  # 通知消费者有新数据可消费
        time.sleep(random.randint(1, 3))

def consumer():
    global queue
    while True:
        with condition:  # 获取条件锁
            if len(queue) == 0:  # 如果队列为空，等待生产者生产数据
                print("Queue is empty, consumer is waiting...")
                condition.wait(timeout=10)  # 等待生产者生产数据
                break
            item = queue.pop()  # 消费数据
            print(f"Consumed {item}, Queue size: {len(queue)}")
            if len(queue) <= 5:
                condition.notify()  # 通知生产者有空位
        time.sleep(random.randint(1, 3))

def main():
    # 创建生产者和消费者线程
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # 启动线程
    producer_thread.start()
    consumer_thread.start()

    # 等待线程结束
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()

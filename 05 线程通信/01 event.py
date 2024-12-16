import threading
import time


class MyThread(threading.Thread):
    def __init__(self, event):
        super().__init__()
        self.event = event

    def run(self):
        print(f"线程{self.name}初始化成功。。。")
        # 设置线程等待
        self.event.wait()
        print(f"开始执行线程{self.name}。。。")
if __name__ == "__main__":
    event = threading.Event()
    threads = []
    [threads.append(MyThread(event)) for i in range(1, 10)]

    [t.start() for t in threads]
    time.sleep(2) # 模拟任务耗时
    event.set() # 设置事件，通知其他线程
    [t.join() for t in threads]
    event.clear()
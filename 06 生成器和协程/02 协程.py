"""
注意事项
事件循环的管理：
    Python 3.7+ 提供 asyncio.run() 管理事件循环。
    不同平台（如 Windows 和 Linux）事件循环机制可能略有不同。
协程嵌套：
    使用 await 调用嵌套协程，确保异步任务依赖关系正常执行。
异常处理：
    在 await 或 asyncio.gather() 中处理协程可能的异常，避免中断事件循环。
"""

"""
使用生成器（Generator）模拟协程
生成器是协程的基础，通过 yield 关键字可以暂停函数的执行并返回一个值。
"""
def simple_coroutine():
    print("使用生成器 Coroutine started")
    x = yield
    print(f"Received value: {x}")

# 创建生成器对象
cor = simple_coroutine()
next(cor)  # 启动协程
#cor.send(42)  # 向协程发送值
"""
输出：
Coroutine started
Received value: 42
"""

"""
基于 asyncio 的原生协程
Python 从 3.5 开始引入了 async def 语法支持原生协程，与 await 一起用于异步任务的管理。
"""
import asyncio

import asyncio

async def fetch_data(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(2)  # 模拟网络延迟
    print(f"Fetched data from {url}")

async def main():
    urls = ["https://example.com", "https://google.com", "https://github.com"]
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)  # 并发执行
asyncio.run(main())
print("主线程结束")
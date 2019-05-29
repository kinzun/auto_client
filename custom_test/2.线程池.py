import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    """
    采集资产
    :return:
    """
    time.sleep(2)
    print(i)
    print(hostname)


# 创建一个线程池，线程池最多放 20 线程

pool = ThreadPoolExecutor(20)

for i in range(1, 101):
    hostname = "c%s.com" % (i,)
    # 去线程池申请一个线程执行 task function
    pool.submit(task, hostname)

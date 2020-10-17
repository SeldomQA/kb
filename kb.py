from __future__ import print_function
import time
import gevent
from gevent import monkey
monkey.patch_all()

import requests
from numpy import mean


users = 10  # 用户数
numbers = 100  # 请求次数
req_url = "http://127.0.0.1:5000/user/tom"  # 请求URL

print("请求URL: {url}".format(url=req_url))

print("用户数：{}，循环次数: {}".format(users, numbers))

print("============== Running ===================")

pass_number = 0
fail_number = 0

run_time_list = []


def running(url):
    global fail_number
    global pass_number
    for _ in range(numbers):
        start_time = time.time()
        r = requests.get(url)
        if r.status_code == 200:
            pass_number = pass_number + 1
            print(".", end="")
        else:
            fail_number = fail_number + 1
            print("F", end="")

        end_time = time.time()
        run_time = round(end_time - start_time, 4)
        run_time_list.append(run_time)


jobs = [gevent.spawn(running, req_url) for _url in range(users)]
gevent.wait(jobs)

print("\n============== Results ===================")
print("最大:       {} s".format(str(max(run_time_list))))
print("最小:       {} s".format(str(min(run_time_list))))
print("平均:       {} s".format(str(round(mean(run_time_list), 4))))
print("请求成功", pass_number)
print("请求失败", fail_number)
print("============== end ===================")

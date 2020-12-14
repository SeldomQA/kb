from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import time
import click
import requests
from numpy import mean
from tqdm import tqdm


class statistical:
    pass_number = 0
    fail_number = 0
    run_time_list = []


def running(url, numbers):
    for _ in tqdm(range(numbers)):
        start_time = time.time()
        r = requests.get(url)
        if r.status_code == 200:
            statistical.pass_number = statistical.pass_number + 1
        else:
            statistical.fail_number = statistical.fail_number + 1

        end_time = time.time()
        run_time = round(end_time - start_time, 4)
        statistical.run_time_list.append(run_time)


@click.command()
@click.argument('url')
@click.option('-u', default=1, help='运行用户的数量，默认 1', type=int)
@click.option('-q', default=1, help='单个用户请求数，默认 1', type=int)
def main(url, u, q):
    print("请求URL: {url}".format(url=url))
    print("用户数：{}，循环次数: {}".format(u, q))
    print("============== Running ===================")

    jobs = [gevent.spawn(running, url, q) for _url in range(u)]
    gevent.wait(jobs)

    print("\n============== Results ===================")
    print("最大:       {} s".format(str(max(statistical.run_time_list))))
    print("最小:       {} s".format(str(min(statistical.run_time_list))))
    print("平均:       {} s".format(str(round(mean(statistical.run_time_list), 4))))
    print("请求成功", statistical.pass_number)
    print("请求失败", statistical.fail_number)
    print("================== end ====================")


if __name__ == "__main__":
    main()

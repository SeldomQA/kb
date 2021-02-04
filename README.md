# kb

kb 是一个简单的性能测试脚本，通过`协程`模拟并发请求。

## install

```shell
> git clone https://github.com/SeldomQA/kb
> cd kb
> python3 setup.py install
```

## 使用

查看帮助：

```py
kb --help
usage: kb [-h] [-v] [-r R] [-m M] [-u USERS] [-q REQUESTS] [url]

kb is a simple performance testing tool, Simulate concurrent requests through
a coroutine.

positional arguments:
  url                   URL to hit

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -r R                  run test case
  -m M                  run tests modules, classes or even individual test
                        methods from the command line
  -u USERS, --users USERS
                        Number of concurrent users
  -q REQUESTS, --requests REQUESTS
                        Number of requests
```

## 运行

```shell
> kb http://wwww.baidu.com -u 10 -q 10
请求URL: https://wwww.baidu.com
用户数：10，循环次数: 10
============== Running ===================
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  3.06it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  3.01it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.99it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.87it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.75it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.69it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:03<00:00,  2.56it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:04<00:00,  2.39it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:04<00:00,  2.39it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:04<00:00,  2.21it/s]
100%|██████████████████████████████████████████████████████████████████████████| 10/10 [00:04<00:00,  1.86it/s]
============== Results ===================
最大:       1.5049 s████████████████████████████████████████████████████▌       | 9/10 [00:03<00:00,  2.71it/s]
最小:       0.2811 s
平均:       0.3755 s███████████████████████████████████████████████████████████| 10/10 [00:04<00:00,  2.89it/s]
请求成功 100
请求失败 0
================= end ====================
```

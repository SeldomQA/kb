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
> kb --help
usage: kb [-h] [-v] [-u USERS] [-q REQUESTS] [url]

kb is a simple performance testing tool, Simulate concurrent requests through
a coroutine.

positional arguments:
  url                   URL to hit

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -u USERS, --users USERS
                        Number of concurrent users
  -q REQUESTS, --requests REQUESTS
                        Number of requests
```

## 运行

通过`kb`命令实现URL并发请求

```shell
> kb https://www.baidu.com -u 5 -q 20
URL: https://www.baidu.com
users: 5, requests: 20
============== Running ===================
100%|████████████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<?, ?it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.45it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.41it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.31it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.20it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.14it/s]

============== Results ===================
Max:       0.2601 s
Min:       0.054 s
Average:   0.0968 s
pass:  100
fail:  0
total: 100
================== end ===================
```

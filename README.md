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
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.85it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.49it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.46it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.17it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 10.09it/s]
100%|██████████████████████████████████████████████████████████████████████████████████| 20/20 [00:01<00:00, 11.02it/s]
============== Results ===================
Samples: 100
Average:      0.0958 s
Max:          0.1821 s
Min:          0.063 s
Median:       0.089 s
90% Line:       0.1303000000000001 s
95% Line:       0.15015 s
99% Line:       0.16725000000000007 s
Total time:   9.5755 s
pass:  100, fail:  0
================== end ===================
Assertion HTTP status code 200
```

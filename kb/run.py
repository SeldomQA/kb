from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import sys
import time
import argparse
import requests
from numpy import mean
from tqdm import trange

from kb import __description__, __version__


def main():
    """
    API test: parse command line options and run commands.
    """

    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument(
        '-v', '--version', dest='version', action='store_true',
        help="show version")

    parser.add_argument("url", help="URL to hit", nargs="?")

    parser.add_argument(
        "-u", "--users",
        help="Number of concurrent users", type=int, default=1)

    parser.add_argument(
        "-q", "--requests",
        help="Number of requests", type=int, default=1)

    args = parser.parse_args()

    if args.version:
        print("kb {}".format(__version__))
        sys.exit(0)

    if args.url is None:
        print("You need to provide an URL.")
        parser.print_usage()
        sys.exit(1)

    load(args.url, args)
    return 0


class Statistical:
    pass_number = 0
    fail_number = 0
    run_time_list = []


def running(url, numbers):
    for _ in trange(numbers):
        start_time = time.time()
        r = requests.get(url)
        if r.status_code == 200:
            Statistical.pass_number = Statistical.pass_number + 1
        else:
            Statistical.fail_number = Statistical.fail_number + 1

        end_time = time.time()
        run_time = round(end_time - start_time, 4)
        Statistical.run_time_list.append(run_time)


def load(url, args):
    print("URL: {url}".format(url=url))
    print("users: {}, requests: {}".format(args.users, args.requests))
    print("============== Running ===================")

    jobs = [gevent.spawn(running, url, args.requests) for _url in trange(args.users)]
    gevent.wait(jobs)

    print("\n============== Results ===================")
    print("Max:       {} s".format(str(max(Statistical.run_time_list))))
    print("Min:       {} s".format(str(min(Statistical.run_time_list))))
    print("Average:   {} s".format(str(round(mean(Statistical.run_time_list), 4))))
    print("pass:  {}".format(Statistical.pass_number))
    print("fail:  {}".format(Statistical.fail_number))
    print("total: {}".format(Statistical.pass_number + Statistical.fail_number))
    print("================== end ===================")


def console_main():
    main()
    return 0


if __name__ == "__main__":
    main()

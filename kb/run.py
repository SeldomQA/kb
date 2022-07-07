from __future__ import print_function
import gevent
from gevent import monkey
monkey.patch_all()
import sys
import time
import argparse
import httpx
import numpy
from tqdm import trange

from kb import __description__, __version__
from rich.progress import track
from rich.console import Console
from rich.table import Column, Table

console = Console()


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
    for _ in range(numbers):
        start_time = time.time()
        r = httpx.get(url)
        if r.status_code == 200:
            Statistical.pass_number = Statistical.pass_number + 1
        else:
            Statistical.fail_number = Statistical.fail_number + 1

        end_time = time.time()
        run_time = round(end_time - start_time, 4)
        Statistical.run_time_list.append(run_time)


def load(url, args):
    console.print(f"🌐 URL: {url}", style="magenta")
    console.print("👥", f"Users: {args.users}   📨 requests: {args.requests}", style="magenta")
    console.print("============== Running ===================", style="bold blue")

    jobs = [gevent.spawn(running, url, args.requests) for _url in track(range(args.users))]
    gevent.wait(jobs)

    console.print("\n============== Results ===================", style="bold blue")
    console.print("Samples: {s} 📨      pass:  {p} ✔️    fail:  {f}❌️".format(
        s=str(Statistical.pass_number + Statistical.fail_number),
        p=str(Statistical.pass_number),
        f=str(Statistical.fail_number)
    ))

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Title", style="green", width=12)
    table.add_column("Second")

    table.add_row(
        "Average:", str(round(numpy.mean(Statistical.run_time_list), 4))
    )
    table.add_row(
        "Max:", str(max(Statistical.run_time_list))
    )
    table.add_row(
        "Min:", str(min(Statistical.run_time_list))
    )
    table.add_row(
        "Median:", str(numpy.median(numpy.array(Statistical.run_time_list)))
    )
    table.add_row(
        "90% Line:", str(numpy.percentile(numpy.array(Statistical.run_time_list), 90))
    )
    table.add_row(
        "95% Line:", str(numpy.percentile(numpy.array(Statistical.run_time_list), 95))
    )
    table.add_row(
        "Total time:", str(numpy.percentile(numpy.array(Statistical.run_time_list), 99))
    )
    console.print(table)
    console.print("================== Ending ===================", style="bold blue")
    console.print("Assertion HTTP status code 200")


def console_main():
    main()
    return 0


if __name__ == "__main__":
    main()

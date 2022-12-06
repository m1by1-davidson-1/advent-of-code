#!/usr/bin/env python3
# encoding: utf-8

import json
import logging
import sys
from datetime import datetime, timezone, timedelta
import argparse

logger = logging.getLogger()


def load_file(filename):
    c = []
    with open(filename, 'r') as f:
        for line in f:
            c.append(line.strip('\n'))
    return c


class Solver:
    __tool_value = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    __tool_score = {
        'X': {'A': 3, 'B': 0, 'C': 6},
        'Y': {'A': 6, 'B': 3, 'C': 0},
        'Z': {'A': 0, 'B': 6, 'C': 3}
    }

    def __init__(self, filename=None):
        self.input = load_file(filename)

    def run(self):
        total = 0
        for round in self.input:
            elems = round.split(' ')
            total += self.score(elems[0], elems[1])
        return total

    @classmethod
    def score(cls, elf, me):
        return cls.__tool_value.get(me, 0) + cls.__tool_score.get(me, {}).get(elf, 0)


def main():
    # Define args
    parser = argparse.ArgumentParser(description='Args parser')
    parser.add_argument("-c", "--config", required=True, help="config file in 'config' directory")
    parser.add_argument("-d", "--debug", required=False, default=False, type=bool, help="1 for debug, 0 for info")
    parsed = parser.parse_args()

    # Define logging levels
    logger.setLevel(logging.DEBUG if parsed.debug else logging.INFO)
    logging.getLogger("boto").setLevel(logging.WARNING)
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)-7s] %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)

    # Launch downloader
    solver = Solver(parsed.config)
    res = solver.run()
    print(res)

if __name__ == '__main__':
    main()




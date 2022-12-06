#!/usr/bin/env python3
# encoding: utf-8

import json
import logging
import sys
from datetime import datetime, timezone, timedelta
import argparse
import string

logger = logging.getLogger()


def load_file(filename):
    c = []
    with open(filename, 'r') as f:
        for line in f:
            c.append(line.strip('\n'))
    return c


class Solver:
    __letters = string.ascii_lowercase + string.ascii_uppercase

    def __init__(self, filename=None):
        self.input = load_file(filename)

    def run(self):
        total = 0
        for rucksack in self.input:
            l = len(rucksack)
            comp1 = set(rucksack[0:int(l/2)])
            comp2 = set(rucksack[int(l/2):])
            total += self.__letters.find(list(comp1.intersection(comp2))[0]) + 1
        return total


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




#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys


def get_string(filename):
    with open(filename) as f:
        return f.read()


word_count = {}


def main():
    a_str = get_string(sys.argv[1])
    obj = re.findall("[A-Za-z0-9]+", a_str)
    print len(obj)


if __name__ == '__main__':
    main()

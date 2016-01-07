#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys


LINE_COUNT = {
    "empty": 0,
    "code": 0,
    "comment": 0,
}

dirname = sys.argv[1]


for filename in os.listdir(dirname):
    if not filename.endswith(".py"):
        continue
    file_path = os.path.join(dirname, filename)
    with open(file_path) as fin:
        for line in fin.xreadlines():
            s = line.strip()
            if not s:
                LINE_COUNT['empty'] += 1
            elif s.startswith("#"):
                LINE_COUNT['comment'] += 1
            else:
                LINE_COUNT['code'] += 1


print LINE_COUNT


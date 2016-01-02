#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys

from PIL import Image


# size = 640, 1136
WIDTH = 640
HEIGHT = 1136


IMG_DIR = sys.argv[1]

for infile in os.listdir(IMG_DIR):
    name, ext = os.path.splitext(infile)
    img = Image.open(os.path.join(IMG_DIR, infile))
    width, height = img.size
    print img.size
    if width > WIDTH:
        width = WIDTH
    if height > HEIGHT:
        height = HEIGHT
    print width, height
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(os.path.join(IMG_DIR, name) + "_5s.jpg", "JPEG")

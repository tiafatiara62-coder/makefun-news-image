#!/usr/bin/env python3
"""Copy the pre-rendered front page to /output/entry.png.

The image is drawn deterministically at build time (render.py, PIL) and
committed as entry.png; this program only copies it, so the output is
byte-identical on every run. Standard library only.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"

os.makedirs("/output", exist_ok=True)
# The copy is the whole program: entry.png is already the final image.
shutil.copyfile(SRC, DST)

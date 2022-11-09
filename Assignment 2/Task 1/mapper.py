#!/usr/bin/env python3

import sys

for lines in sys.stdin:
    line = lines.split()
    print(line[0], "\t", line[1])
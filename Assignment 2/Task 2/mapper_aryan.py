#!/usr/bin/env python3
import json
import math
import sys


embed_data = open(sys.argv[2].strip())
data = json.load(embed_data)
pages = dict()
with open(sys.argv[1].strip()) as v:
    lines = v.read().strip().split("\n")
    print(lines)
    for line in lines:
        try:
            page, rank = line.split(",")
        except:
            continue
        pages[float(page.strip())] = float(rank.strip())

for line in sys.stdin:
    line = line.strip()
    try:
        src, dest = line.split("\t")
        src = int(src.strip())
        dest = eval(dest.strip())
    except:
        continue

    # out = len(dest)
    # result = pages[src]
    cont = pages[src] * (1 / len(dest))

    print(f"{src},0")

    for i in dest:
        if i in pages.keys():
            p = data[str(src)]
            q = data[str(i)]
            mag_p = math.sqrt(sum(i ** 2 for i in p))
            mag_q = math.sqrt(sum(i ** 2 for i in q))
            res = sum(x * y for x, y in zip(p, q)) / (mag_p * mag_q)
            print(f"{i},{cont * res}")
        else:
            print(f"{i},0.14")

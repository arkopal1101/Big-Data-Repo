#!/usr/bin/env python3

import sys

current_time = None
time_count = 0
time = None

for line in sys.stdin:
    line = line.strip()
    time, count = line.split(',', 1)
    try:
        count = int(count)
        time = str(int(time))
    except ValueError:
        continue

    if current_time == time:
        time_count += count
    else:
        if current_time:
            print('%s %s' % (current_time, time_count))
        time_count = count
        current_time = time

if current_time == time:
    print('%s %s' % (current_time, time_count))

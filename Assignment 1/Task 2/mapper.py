#!/usr/bin/env python3

import json
import math
import sys
import time

import requests

objects = None
start_lon = []
end_lon = []
start_lat = []
end_lat = []
D = 0

url = 'http://20.185.44.219:5000/'

target_lat = sys.argv[1]
target_lon = sys.argv[2]
D = sys.argv[3]

for line in sys.stdin:
    objects = json.loads(line)
    start_lat.append(objects['Start_Lat'])
    start_lon.append(objects['Start_Lng'])

for i in range(len(start_lat)):
    x = (target_lat, target_lon)
    y = (start_lat[i], start_lon[i])
    distance = math.sqrt(sum([(float(a) - float(b)) ** 2 for a, b in zip(x, y)]))
    if distance <= float(D):
        while True:
            try:
                params = {"latitude": start_lat[i], "longitude": start_lon[i]}
                x = requests.post(url, json=params).json()
                print("%s,%s,%s" % (x['state'], x['city'], 1))
            except:
                time.sleep(1)
                params = {"latitude": start_lat[i], "longitude": start_lon[i]}
                x = requests.post(url, json=params).json()
                print("%s,%s,%s" % (x['state'], x['city'], 1))
                continue

            break


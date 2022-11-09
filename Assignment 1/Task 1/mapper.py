#!/usr/bin/env python3

import json
import sys
from datetime import *
from re import search, IGNORECASE, findall


objects = []
description = []
severity = []
sunrise_sunset = []
visibility = []
precipitation = []
weather_condition = []
start_time = []

for line in sys.stdin:
    objects = json.loads(line)
    description.append(objects['Description'])
    severity.append(objects['Severity'])
    sunrise_sunset.append(objects['Sunrise_Sunset'])
    visibility.append(objects['Visibility(mi)'])
    precipitation.append(objects['Precipitation(in)'])
    weather_condition.append(objects['Weather_Condition'])
    start_time.append(objects['Start_Time'])


for i in range(len(description)):
    if search("lane blocked|shoulder blocked|overturned vehicle", description[i], IGNORECASE) \
            and severity[i] >= 2 \
            and search("Night", str(sunrise_sunset[i]), IGNORECASE) and visibility[i] <= 10 \
            and precipitation[i] >= 0.2 \
            and search(r"\bHeavy Snow\b|\bThunderstorm\b|\bHeavy Rain\b|\bHeavy Rain Showers\b|\bBlowing Dust\b",
                       weather_condition[i], IGNORECASE):

        conditions = findall(r"\bHeavy Snow\b|\bThunderstorm\b|\bHeavy Rain\b|\bHeavy Rain Showers\b|\bBlowing Dust\b",
                             weather_condition[i], IGNORECASE)
        if len(conditions[0]) == len(str(weather_condition[i])):

            try:
                hours = str(datetime.strptime(str(start_time[i]), '%Y-%m-%d %H:%M:%S').hour)
                print("%s,%s" % (hours.zfill(2), 1))
            except ValueError:
                hours = str(datetime.strptime(str(start_time[i])[0:21], '%Y-%m-%d %H:%M:%S.%f').hour)
                print("%s,%s" % (hours.zfill(2), 1))


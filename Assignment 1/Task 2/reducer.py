#!/usr/bin/env python3


import sys

flag = 1
count_city = 0
count_states = 0

for line in sys.stdin:
    line = line.strip()
    state, city, waste = line.split(",")
    if flag == 1:
        count_states = 0
        print(state)
        current_state = state
        current_city = city
        count_city = 0
        flag = 0

    if state == current_state and city == current_city:
        count_city += 1

    elif state == current_state and city != current_city:
        count_states += count_city
        print(current_city, count_city)
        current_city = city
        count_city = 1

    elif state != current_state and city != current_city:
        count_states += count_city
        print(current_city, count_city)
        print(current_state, count_states)
        count_states = 0
        current_state = state
        print(current_state)
        current_city = city
        count_city = 1

if count_city != 0 and count_states != 0:
    count_states += count_city
    print(current_city, count_city)
    print(current_state, count_states)

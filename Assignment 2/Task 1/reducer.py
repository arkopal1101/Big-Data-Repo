#!/usr/bin/env python3

import sys

v = open(sys.argv[1], 'w')
o = open(sys.argv[2], 'w')
dest_lst = []
prev = None
curr = None

for line in sys.stdin:
    src, dest = line.strip().split('\t')

    if prev == src:
        dest_lst.append(int(dest))

    elif prev is None:
        curr = src
        dest_lst.append(int(dest))
        prev = src

    else:
        print(curr, "\t", dest_lst)
        v.write('%s,%s\n' % (curr, int(1)))
        o.write('%s\t%s\n' % (curr, dest_lst))
        curr = src
        dest_lst.clear()
        dest_lst.append(int(dest))
        prev = curr

print(curr, "\t", dest_lst)
o.write('%s\t%s\n' % (curr, dest_lst))
v.write('%s,%s\n' % (curr, int(1)))
v.close()

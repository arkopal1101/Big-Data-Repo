import sys
from ast import literal_eval

for lines in sys.stdin:
    line = lines.strip().split('\t')
    # print((line[1:]))
    x = literal_eval(line[1])
    print(x)
    print(x[2])
    # print(line[1].eval())

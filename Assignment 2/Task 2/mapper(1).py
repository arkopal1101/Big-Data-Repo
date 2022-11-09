import json
import sys
from ast import literal_eval
import math

with open(sys.argv[1], "r") as f:
    with open(sys.argv[2], "r") as f1:
        inp = f.read().splitlines()
        data = json.loads(f1.read())

        M = [[] for i in range(len(data.keys()))]
        S = [[] for j in range(len(data.keys()))]

        # inp = [i.replace(" ,1", "") for i in inp]
        # print(inp)

        for lines in sys.stdin:
            c = 0
            line = (lines.strip().split('\t'))
            pos = literal_eval(line[1])
            initial = 1 / len(pos)

            # print(line[0])
            for i in data.keys():

                if int(i) not in pos:
                    M[c].append(0.0)

                    # if i not in inp:
                    #     M[c].append(0.0)

                else:
                    M[c].append(round(initial, 2))
                c += 1

    print(M)
    # for i in data.keys():
    #     if i not in inp:
    #         j = i

    for i in sorted(data.keys()):
        count = 0
        # print(i)
        for j in sorted(data.keys()):
            result, dot, mod, p, q = 0, 0, 0, 0, 0
            if i != j:
                for num1, num2 in zip(data[i], data[j]):
                    p = math.pow(num1, 2) + p
                    q = math.pow(num2, 2) + q
                    dot = num1 * num2 + dot
                mod = math.sqrt(p) * math.sqrt(q)
                result = dot / mod
                S[count].append(round(result, 2))

            else:
                S[count].append(1)
            count += 1

    count2 = 0
    print(S)

    for i in range(len(M)):
        print(i)
        for j in range(len(S)):
            print(j)
            M[i][j] = M[i][j] * S[i][j]
        print(inp[count2][0], M[i], sep='\t')
        S[i].clear()
        count2 += 1
M.clear()

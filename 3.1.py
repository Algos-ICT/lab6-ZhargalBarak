import time


def hash(string):
    res = 0
    for i in range(len(string)):
        res += ord(string[i]) * 263 ** i
    global m
    res = (res % 1000000007) % m
    return res

with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        m = int(f.readline())
        N = int(f.readline())
        table = [[] for _ in range(m)]
        start = time.perf_counter()
        for i in range(N):
            command, s = list(f.readline().split())
            if command == 'check':
                for i in range(len(table[int(s)])):
                    f1.write(table[int(s)][i] + ' ')
                f1.write('\n')
            else:
                h = hash(s)
                if command == 'add':
                    if s not in table[h]:
                        table[h] = [s] + table[h]
                elif command == 'del':
                    if s in table[h]:
                        table[h].remove(s)
                else:
                    if s in table[h]:
                        f1.write('yes\n')
                    else:
                        f1.write('no\n')
        print(time.perf_counter() - start)
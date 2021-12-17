import time

with open ('input.txt') as f:
    with open('output.txt', 'w') as f1:
        plenty = {}
        N = int(f.readline())
        start = time.perf_counter()
        for i in range(N):
            command, key = f.readline().split()
            if command == 'A':
                plenty[key] = []
            elif command == 'D':
                if key in plenty:
                    del(plenty[key])
            else:
                if key in plenty:
                    f1.write('Y\n')
                else:
                    f1.write('N\n')
        print(time.perf_counter() - start)
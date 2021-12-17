def get(x):
    global table
    if x in table:
        return table[x][1]
    return '<none>'

def prev(x):
    global table
    if x in table:
        return get(table[x][0])
    return '<none>'

def next(x):
    global table
    if x in table:
        return get(table[x][2])
    return '<none>'

def put(x, y):
    global table
    if x in table:
        table[x][1] = y
    else:
        global bef
        table[bef][2] = x
        table[x] = [bef, y, '<none>']
        bef = x

def delete(x):
    global table
    if x in table:
        global bef
        if x == bef:
            if table[x][0] != '<none>':
                bef = table[x][0]
        if table[x][0] != '<none>':
            table[table[x][0]][2] = table[x][2]
        if table[x][2] != '<none>':
            table[table[x][2]][0] = table[x][0]
        del(table[x])

with open('input.txt') as f:
    with open('output.txt', 'w') as f1:
        N = int(f.readline())
        table = {}
        bef = ''
        for i in range(N):
            command = list(f.readline().split())
            if command[0] == 'put':
                if len(table) == 0:
                    table[command[1]] = ['<none>', command[2], '<none>']
                    bef = command[1]
                else:
                    put(command[1], command[2])
            elif command[0] == 'get':
                f1.write(get(command[1]) + '\n')
            elif command[0] == 'prev':
                f1.write(prev(command[1]) + '\n')
            elif command[0] == 'next':
                f1.write(next(command[1]) + '\n')
            else:
                delete(command[1])
def find(r: int, c: int) -> list:
    if parent[r][c] != (r, c):
        nr, nc = parent[r][c]
        parent[r][c] = find(nr, nc)
    return parent[r][c]


def update1(r: int, c: int, v: str) -> None:
    root = find(r, c)

    for i in range(n):
        for j in range(n):
            if find(i, j) == root:
                table[i][j] = v


def update2(v1: str, v2: str) -> None:
    for i in range(n):
        for j in range(n):
            r, c = find(i, j)

            if table[r][c] == v1:
                table[r][c] = v2


def merge(r1: int, c1: int, r2: int, c2: int) -> None:
    r1 ,c1 = find(r1, c1)
    r2 ,c2 = find(r2, c2)

    if [r1 ,c1] == [r2 ,c2]: return

    parent[r2][c2] = (r1, c1)
    v = table[r1][c1] if table[r1][c1] else table[r2][c2]
    update1(r1, c1, v)


def unmerge(r: int, c: int) -> None:
    root = find(r, c)
    v = table[root[0]][root[1]]

    mrg = [(i, j) for i in range(n) for j in range(n) if find(i, j) == root]

    for rt in mrg:
        r1, c1 = rt
        parent[r1][c1] = (r1, c1)

        if (r1, c1) != (r, c):
            table[r1][c1] = 0

    table[r][c] = v


def printer(r: int, c: int) -> None:
    r1, c1 = find(r, c)
    v = table[r1][c1]
    ans.append('EMPTY' if not v else v)


def solution(commands):

    global n
    global ans
    global table
    global parent

    n = 51
    ans = []
    table = [[0] * n for _ in range(n)]
    parent= [[(r, c) for c in range(n)] for r in range(n)]

    for command in commands:
        command = command.split()
        cmd, value = command[0], command[1:]

        if cmd == 'UPDATE':
            if len(value) == 3:
                r, c, v = value
                update1(int(r), int(c), v)

            else:
                v1, v2 = value
                update2(v1, v2)

        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, value)
            merge(r1, c1, r2, c2)

        elif cmd == 'UNMERGE':
            r, c = map(int, value)
            unmerge(r, c)

        else:
            r, c = map(int, value)
            printer(r, c)

    return ans


# Run.
'''
output : ["EMPTY", "group"]
commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", 
            "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", 
            "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", 
            "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
'''
from collections import deque

n = int(input())
stack = deque()

ans = ''
chk = 1
for _ in range(n):
    x = int(input())

    if chk <= x:
        for i in range(chk, x + 1):
            stack.append(i)
            ans += '+'
        chk = x + 1

    if stack[-1] == x:
        stack.pop()
        ans += '-'

    else:
        print('NO')
        exit(0)

print(*ans, sep = '\n')


'''
output :
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

8
4
3
6
8
7
5
2
1
'''
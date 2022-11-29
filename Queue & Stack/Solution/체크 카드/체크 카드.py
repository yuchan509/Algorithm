from collections import deque

n, m = map(int, input().split())

temp = deque()
for _ in range(m):
    op, k = input().split()
    k = int(k)

    if op == "deposit":
        n += k

    elif op == "pay":
        if n >= k:
            n -= k

    else:
        if n < k or temp:
            temp.append(k)
        elif n >= k:
            n -= k

    while temp:
        t = temp.popleft()
        if n >= t:
            n -= t
        else:
            temp.appendleft(t)
            break

print(n)

    
```
output : 5
0 6
deposit 10
reservation 20
pay 5
deposit 10
deposit 10
reservation 6
```
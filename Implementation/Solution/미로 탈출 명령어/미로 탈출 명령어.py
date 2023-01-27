def solution(n, m, x, y, r, c, k):

    mx = abs(x - r)
    my = abs(y - c)
    k -= (mx + my)

    direction = {d: 0 for d in ['d', 'l', 'rl', 'r', 'u']}

    direction['d' if x < r else 'u'] += mx
    direction['l' if y > c else 'r'] += my

    if k % 2 != 0 or k < 0: return 'impossible'

    du = min(n - max(r, x), k // 2)
    k -= du * 2

    direction['d'] += du
    direction['u'] += du

    lr = min(min(y, c) - 1, k // 2)
    k -= lr * 2

    direction['l'] += lr
    direction['r'] += lr

    direction['rl'] = k // 2

    ans = ''.join([k * v for k, v in direction.items()])

    return ans


```
output : "dllrl"
n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5
```
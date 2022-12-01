def solution(k, ranges):

    ans = []
    number = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        number.append(k)

    dp = [0] * (len(number) - 1) 
    for i in range(len(number) - 1):
        dp[i] = (number[i] + number[i + 1]) / 2

    for s, e in ranges:
        if len(dp) + e < s:
            ans.append(-1.0)

        else:
            if e == 0:
                ans.append(sum(dp[s : ]))
            else:
                ans.append(sum(dp[s : e]))

    return ans

```
output : [33.0,31.5,0.0,-1.0]
k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
```
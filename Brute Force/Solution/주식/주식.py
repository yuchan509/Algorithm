for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))

    ans, MAX = 0, 0
    for stock in stocks[::-1]:
        MAX = max(stock, MAX)
        ans += MAX - stock

    print(ans)


# answer 2.
for _ in range(int(input())):
    n = int(input())
    stock = list(map(int, input().split()))

    ans = [0] * n
    MAX = stock[n - 1]

    for idx in range(n - 1, -1, -1):
        MAX = max(MAX, stock[idx])
        ans[idx] = MAX

    res = 0
    for a, b in zip(ans, stock):
        res += a - b

    print(res)


'''
out : 
0
10
5

3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
'''
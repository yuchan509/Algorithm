import sys
input = sys.stdin.readline

k = int(input())

for rank in range(k):
    s1, s2, s3 = input().split()

    ans = "no"

    n, m = len(s1), len(s2)
    dp = [[True] * (m + 1) for _ in range(n + 1)]

    if n + m != len(s3):
        print(f"Data set {rank + 1}: {ans}")
        continue

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, m + 1):
        dp[0][i] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            c2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            dp[i][j] = c1 or c2

    print(f"Data set {rank + 1}: {'yes' if dp[-1][-1] else ans}")

# run.
'''
output :
Data set 1: yes
Data set 2: yes
Data set 3: no

3
cat tree tcraete
cat tree catrtee
cat tree cttaree
'''

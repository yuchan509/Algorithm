import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

belt = [int(input()) for _ in range(n)]

ans = 0
length = len(belt)

for i in range(length):
    window = belt[i:length] + belt[:(k + i) % length] if k + i > length else belt[i:k + i]

    ans = max(ans, len(set(window + [c])))

print(ans)


# Run.
'''
output : 5
8 30 4 30
7
9
7
30
2
7
9
25
'''
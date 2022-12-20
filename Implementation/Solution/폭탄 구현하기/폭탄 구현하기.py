import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[1, 0],[0, 1],[-1, 0],[0, -1]]
arr = [[0] * n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] += 1
    
    for da, db in d:
        na = a + da
        nb = b + db
        
        if 0 <= na < n and 0 <= nb < n:
            arr[na][nb] += 1
            
ans = sum(sum(arr, []))

print(ans)


'''
output : 9
3 3
3 3
3 3
1 1
'''

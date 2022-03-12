import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def division(mid):

    m_cnt = 1
    mx = mn = arr[0]
    for v in arr:
        mx = max(mx, v)
        mn = min(mn, v)

        if mid < (mx - mn):
            m_cnt += 1
            mx = mn = v
            
    
    return m_cnt

ans = 10000000
left, right = 0, max(arr)
while left <= right:
    mid = (left + right) // 2
    
    if division(mid) <= m:
        right = mid - 1
        ans = mid if mid < ans else ans

    else:
        left = mid + 1
        
print(ans)


# Run.
'''
output : 5
8 3
1 5 4 6 2 1 3 7
'''

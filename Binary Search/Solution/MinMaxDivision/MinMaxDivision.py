def division(A, mid):
    cnt, cursum = 1, 0
    for i in A:
        cursum += i;
        
        if cursum > mid:
            cursum = i
            cnt += 1
    return cnt
    
def solution(K, M, A):
    left, right = max(A), sum(A)
    
    while left <= right:
        mid = (left + right) // 2
        if division(A, mid) <= K:
            right = mid - 1
        else:
            left = mid + 1
            
    return left


# Run.
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
solution(K, M, A)

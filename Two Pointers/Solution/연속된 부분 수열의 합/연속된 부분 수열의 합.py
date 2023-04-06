def solution(sequence, k):
    
    min_start = -1
    n = len(sequence)
    cumsum = sequence[0]
    
    start, end, length = 0, 0, float('inf')
    
    while end < n:
        if cumsum < k:
            end += 1
            if end < n:
                cumsum += sequence[end]
        else:
            if cumsum == k and end - start + 1 < length:
                length = end - start + 1
                min_start = start
                
            cumsum -= sequence[start]
            start += 1
            
    return [min_start, min_start + length - 1]


'''
output : [2, 3]
equence	= [1, 2, 3, 4, 5]
k = 7
'''
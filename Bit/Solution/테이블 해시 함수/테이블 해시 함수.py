def solution(data, col, row_begin, row_end):
    
    ans = 0
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin - 1, row_end):
        ans ^= sum(map(lambda x: x % (i + 1), data[i]))
    return ans

    
'''
output : 4
data : [2,2,6],[1,5,10],[4,2,9],[3,8,3]]	
col = 2
row_begin = 2
row_end = 3
'''
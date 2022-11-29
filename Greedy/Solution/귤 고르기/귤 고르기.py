from collections import Counter

def solution(k, tangerine):

    size = sorted(Counter(tangerine).items(), key = lambda x : -x[-1])    

    ans, cumsum = 0, 0
    for s in size:
        ans += 1
        cumsum += s[-1]
        if cumsum >= k:
            break
    return ans


'''
output : 1
k = 2
tangerine =[1, 1, 1, 1, 2, 2, 2, 3]	
'''
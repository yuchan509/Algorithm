import heapq

def solution(scoville, K) :

    heapq.heapify(scoville)
    ans = 0
    while scoville[0] < K:
        
        if len(scoville) > 1:
            ans += 1
            value = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, value)
            
        else: return -1
    
    return ans


# Run.
'''
output : 2
scoville = [1, 2, 3, 9, 10, 12]	
K = 7	
'''
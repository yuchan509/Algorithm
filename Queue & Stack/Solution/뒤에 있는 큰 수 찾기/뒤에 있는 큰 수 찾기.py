from queue import PriorityQueue

def solution(numbers):

    ans = [-1] * len(numbers)

    pq = PriorityQueue()
    for idx, n in enumerate(numbers):

        while not pq.empty() and pq.queue[0][0] < n:
            v, i = pq.get()
            ans[i] =  n

        pq.put((n, idx))

    return ans

    
```
output : [3, 5, 5, -1]
numbers = [9, 1, 5, 3, 6, 2]
```
from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    ans = 0
    q = deque(truck_weights)    
    # 다리 길이 만큼의 배열 생성.
    bridge = deque([0] * bridge_length)
    
    # 현재 다리의 무게.
    cur_weight = 0
    
    while bridge:
        cur_weight -= bridge.popleft()    
        ans += 1
        
        if q:
            # 다리에 트럭을 더 올리는 것이 가능하다면,
            if cur_weight + q[0] <= weight:
                truck = q.popleft()
                cur_weight += truck
                bridge.append(truck)
            else:
                # 그렇지 않다면,
                bridge.append(0)
    return ans


```
output : 8
bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
```
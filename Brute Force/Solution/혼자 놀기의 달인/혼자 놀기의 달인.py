from collections import deque

def solution(cards):
    answer = []

    v = set()
    q = deque(cards[:])

    while q:
        x = q.popleft()

        if x not in v:
            v.add(x)

            next = x
            count = 1

            while x != cards[next - 1]:
                if cards[next - 1] not in v:
                    v.add(cards[next - 1])
                    next = cards[next - 1] 
                    count += 1  

            answer.append(count)
    answer.sort() 

    return answer[-1] * answer[-2] if len(answer) > 1 else 0


'''
output : 12
dungeons = [8,6,3,7,2,5,1,4]s
'''
from collections import deque

def calculator(time: str) -> int:
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def solution(plans):
    ans = []
    assignment = {name: int(playtime) for name, start, playtime in plans}
    plans.sort(key=lambda x: x[1])

    stop = []
    q = deque(plans)

    while len(q) > 1:
        name, start, playtime = q.popleft()
        next_name, next_start, next_playtime = q[0]

        d = calculator(next_start) - calculator(start)

        if d < int(playtime):
            assignment[name] -= d
            stop.append(name)

        else:
            d -= int(playtime)
            ans.append(name)

            while stop and d > 0:
                stop_name = stop.pop()
                v = assignment[stop_name]
                assignment[stop_name] -= d

                if v > d:
                    d = 0
                    stop.append(stop_name)
                else:
                    d -= v
                    ans.append(stop_name)

    ans += [q[0][0]] + stop[::-1]

    return ans

    
```
output : ["korean", "english", "math"]
plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
```
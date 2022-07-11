import math
def solution(progresses, speeds):
    
    ans = []
    idx = 0
    prev_day = math.ceil((100 - progresses[0]) / speeds[0])
    
    for p, s in zip(progresses, speeds):
    
        cur_day = math.ceil((100 - p) / s)
            
        if prev_day >= cur_day:
            idx += 1

        else:
            ans.append(idx)
            idx = 1
            prev_day = cur_day

    ans.append(idx)
    
    return ans


# Run.
'''
output : [2, 1]	
progresses = [93, 30, 55]	
speeds = [1, 30, 5]	
'''

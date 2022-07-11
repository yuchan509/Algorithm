def solution(arr):
    answer = []
    answer.append(arr[0])
    for value in arr:
        if value != answer[-1]:
            answer.append(value)
    return answer


# Run.
'''
output : [1,3,0,1]
arr = [1,1,3,3,0,1,1]	
'''

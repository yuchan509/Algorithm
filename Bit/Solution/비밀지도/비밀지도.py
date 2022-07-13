def solution(n, arr1, arr2):
    ans = []
    
    for a, b in zip(arr1, arr2):
        line = bin(a | b)[2:].zfill(n)
        ans.append(line.replace('0', ' ').replace('1', '#'))
        
    return ans

    
```
output : ["#####","# # #", "### #", "# ##", "#####"]
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
```
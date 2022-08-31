def solution(survey, choices):
    
    ans = ''
    d = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    for t, c in zip(survey, choices):
        if c > 4:
            d[t[-1]] += c - 4    
        else:
            d[t[0]] += 4 - c


    for i in ['RT', 'CF', 'JM', 'AN']:
        a, b = i
        if d[a] >= d[b]:
            ans += a
        else:
            ans += b

    return ans

```
output : "TCMA"
survey = ["AN", "CF", "MJ", "RT", "NA"]	
choices = [5, 3, 2, 7, 5]	
```
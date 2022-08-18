def solution(phone_book):
    
    ans = True
    phone_book.sort()

    for a, b in zip(phone_book , phone_book[1:]):
        if b.startswith(a):
            ans = False
    return ans

    
```
output : false
phone_book = ["119", "97674223", "1195524421"]		
```
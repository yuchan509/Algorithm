# Algorithm
## Python 문법

#### Loop
```python
# ex1
sum = 0 
for i in range(1, 11):
    sum += i
    
# ex2
sum = sum(i for i in range(1, 11))

# ex3
sum = sum(range(1, 11))    
```

#### Generic
=> parameter의 타입이 나중에 지정되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일.
* Python은 동적 타이핑 언어로서 제네릭이 필요 없으나, 코드의 복잡도가 높아질 수록 혼란을 야기하므로 타입은 명시하는 것이 좋다.

```python
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')

def are_equal(a: T, b: U) -> bool:
    return a == b

are_equal(10, 10.0)
```

#### Array
```python
foo = ['A', 'B', 'C']
for f in foo :
    print(f)
```



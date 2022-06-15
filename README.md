# Algorithm 

## Algorithm 문제집
|<center>NO|<center>Workbooks|<center>Tag|<center>Explanation|
|:---:|:---:|:---:|:---:|
 
|01|[<center>바로가기](https://www.acmicpc.net/problem/2606)|String|[<center>Link](https://github.com/yuchan509/Coding-Test-Study/blob/main/Coding%20Test%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)|
|02|[<center>바로가기](https://programmers.co.kr/learn/courses/30/lessons/43162)|Brute Force||
|03|[<center>바로가기](https://www.acmicpc.net/problem/2606)|Binary Search|[<center>Link](https://github.com/yuchan509/Coding-Test-Study/blob/main/Coding%20Test%20-%20%EC%A4%91%EB%9F%89%20%EC%A0%9C%ED%95%9C.py)|
|04|[<center>바로가기](https://www.acmicpc.net/problem/2606)|Graph search||
|05|[<center>바로가기](https://www.acmicpc.net/problem/2606)|Prefix Sum|[<center>Link](https://github.com/yuchan509/Coding-Test-Study/blob/main/Coding%20Test%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)|
|06|[<center>바로가기](https://www.acmicpc.net/problem/2606)|Dynamic Programming|[<center>Link](https://github.com/yuchan509/Coding-Test-Study/blob/main/Coding%20Test%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)|
|07|[<center>바로가기](https://www.acmicpc.net/problem/2606)|Two Pointer|[<center>Link](https://github.com/yuchan509/Coding-Test-Study/blob/main/Coding%20Test%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)|
    

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

# Type hint

# 아래와 같은 형태로 명시적으로 선언함으로써 가독성을 향상시키고 버그 발생 확률을 줄일 수 있다. 단, version 3.5부터 사용이 가능.
a : str = "1"
b : int = 1

def fn(a : int) -> bool:

pip install mypy -> 타입 힌트에 대한 오류 검정.
```

#### Array
```python
foo = ['A', 'B', 'C']
for f in foo :
    print(f)
```


#### List Comprehension
```python
list(map(lambda x: x + 10, [1, 2, 3]))


```




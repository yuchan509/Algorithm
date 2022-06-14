# Algorithm
## Python 문법



## GraphSearch - 그래프탐색
<br>

|<center>문제 이름|<center>문제 링크|<center>풀이|<center>메모|
|---|---|---|---|---|
|<center>DFS와 BFS|[<center>링크](http://boj.kr/1260)|[<center>링크]|
|<center>단지번호붙이기|[<center>링크](http://boj.kr/2667)|[<center>링크]|
|<center>물통|[<center>링크](http://boj.kr/2251)|[<center>링크]|
|<center>연구소|[<center>링크](http://boj.kr/14502)||[<center>링크]|
|<center>유기농 배추|[<center>링크](http://boj.kr/1012)|[<center>링크]|
|<center>연결 요소의 개수|[<center>링크](http://boj.kr/11724)|[<center>링크]|




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




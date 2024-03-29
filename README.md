# Algorithm 

## Algorithm 사이트
[Programmers](https://programmers.co.kr/learn/challenges) <br/>
[Baekjoon](https://www.acmicpc.net/) <br/>
[Codility](https://app.codility.com/programmers/lessons/1-iterations/) <br/>
[HackerRank](https://www.hackerrank.com/) <br/>
[LeetCode](https://leetcode.com/) <br/>
[Softeer](https://softeer.ai/) <br/>

## Algorithm 문제집
|<center>NO|<center>Workbooks|<center>Tag|<center>Explanation|
|:---:|:---:|:---:|:---:|
|01|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/String)|String||
|02|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Greedy)|Greedy||
|03|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Brute%20Force)|Brute Force||
|04|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Binary%20Search)|Binary Search||
|05|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Graph%20Search)|Graph search||
|06|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Shortest%20Path)|Shortest Path||
|07|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Prefix%20Sum)|Prefix Sum||
|08|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Dynamic%20Programming)|Dynamic Programming||
|09|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Disjoint%20Set)|Disjoint Set||
|10|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Minimum%20Spanning%20Tree(MST))|Minimum Spanning Tree(MST)||
|11|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Heap)|Heap||
|12|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Queue%20&%20Stack)|Queue & Stack||
|13|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Bit)|Bit||
|14|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Implementation)|Implementation||
|15|[바로가기](https://github.com/yuchan509/Algorithm/tree/main/Two%20Pointers)|Two Pointers||


### Contributors


<table>
    <tr height="140px">
        <td align="center" width="130px">
            <a href="https://github.com/yuchan509"><img height="100px" width="100px" src="https://avatars.githubusercontent.com/u/75283773?v=4"/></a>
            <br />
            <a href="https://github.com/yuchan509">Yuchan</a>
        </td>
        <td align="center" width="130px">
            <a href="https://github.com/Kimsunghyunny"><img height="100px" width="100px" src="https://avatars.githubusercontent.com/u/22141977?v=4"/></a>
            <br />
            <a href="https://github.com/Kimsunghyunny">Kimsunghyunny</a>
        </td>
        <td align="center" width="130px">
            <a href="https://github.com/henn36"><img height="100px" width="100px" src="https://avatars.githubusercontent.com/u/50240552?v=4"/></a>
            <br />
            <a href="https://github.com/henn36">henn36</a>
        </td>
        <td align="center" width="130px">
            <a href="https://github.com/gihye0395"><img height="100px" width="100px" src="https://avatars.githubusercontent.com/u/38374463?v=4"/></a>
            <br />
            <a href="https://github.com/gihye0395">gihye0395</a>
        </td>
    </tr>
</table>
    
    
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




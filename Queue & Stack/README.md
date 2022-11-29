# Algorithm 
## Queue & Stack
|<center>NO|                                   <center>Workbooks                                    |            <center>Solution             |<center>Memo|
|:---:|:--------------------------------------------------------------------------------------:|:---------------------------------------:|:---:|
|01|      [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)      |    [바로가기](./Solution/같은%20숫자는%20싫어)     |  |
|02|        [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)         |         [바로가기](./Solution/기능개발)         ||
|03|         [프린터](https://school.programmers.co.kr/learn/courses/30/lessons/42587)         |         [바로가기](./Solution/프린터)          | |
|04|     [다리를 지나는 트럭](https://school.programmers.co.kr/learn/courses/30/lessons/42583)      |    [바로가기](./Solution/다리를%20지나는%20트럭)    ||
|05|        [주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)         |         [바로가기](./Solution/주식가격)         ||
|06|   [올바른 괄호](https://school.programmers.co.kr/learn/courses/30/lessons/12909)    |       [바로가기](./Solution/올바른%20괄호)       ||
|07|                  [카드2](https://www.acmicpc.net/problem/2164)                   |         [바로가기](./Solution/카드2)          ||
|08|    [스킬트리](https://school.programmers.co.kr/learn/courses/30/lessons/49993)     |         [바로가기](./Solution/스킬트리)         ||
|09|  [요세푸스 문제 0](https://school.programmers.co.kr/learn/courses/30/lessons/11866)  |    [바로가기](./Solution/요세푸스%20문제%200)     ||
|10|    [괄호의 값](https://school.programmers.co.kr/learn/courses/30/lessons/11866)    |       [바로가기](./Solution/괄호의%20값)        ||
|11|[두 큐 합 같게 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)| [바로가기](./Solution/두%20큐%20합%20같게%20만들기) ||
|12| [크레인 인형뽑기 게임](https://school.programmers.co.kr/learn/courses/30/lessons/64061) |   [바로가기](./Solution/크레인%20인형뽑기%20게임)    ||
|13|                 [스택 수열](https://www.acmicpc.net/problem/1874)                  |       [바로가기](./Solution/스택%20수열)        | |
|14|                 [체크 카드](https://edu.goorm.io/learn/lecture/33428/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%A8%BC%EB%8D%B0%EC%9D%B4-%EC%B1%8C%EB%A6%B0%EC%A7%80-%ED%95%B4%EC%84%A4/lesson/1679178/4%EC%A3%BC%EC%B0%A8-%EB%B3%B5%EC%8A%B5%EB%AC%B8%EC%A0%9C-1-%EC%B2%B4%ED%81%AC-%EC%B9%B4%EB%93%9C)                  |       [바로가기](./Solution/체크%20카드)        | |

## Stack
- stack : LIFO(Last in, First Out) = FILO(First in, Last Out)
- 기능
  - **push()** : 데이터 스택에 쌓기 
  - **pop()** 데이터 스택에 꺼내기 
- 장점
  - 구조가 단순, 구현이 쉬움.
  - 데이터 저장 / 읽기 속도 빠름.

- 단점
  - 데이터 최대 개수 설정 필요. - 파이썬에서는 기본 1000개 까지 공간 사용 가능.
  - 저장 공간의 낭비가 발생할 수 있음.

   ``` python
   # 재귀시 기본적인 공간을 늘리기 위한 방법.
   import sys 
   sys.setrecursionlimit(10 ** 6)
   
  stack = []
   stack.append(1)
   stack.append(2)
  
   stack.pop()
   ```

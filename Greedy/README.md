# Algorithm 

## Greedy
|<center>NO|<center>Workbooks|<center>Solution|<center>Memo|
|:---:|:---:|:---:|:---:|
|01|[<center>ATM](https://www.acmicpc.net/problem/11399)|[<center>바로가기](./Solution/ATM)||

<br/>

## Greedy Algorithm 
- 최적의 해에 가까운 값을 구하기 위해 이용.
- 여러 경우 중 하나를 결정해야할 때마다, 매순간 최적이라고 생각되는 경우를 선택하는 방식으로 최종값을 구하는 방식.


#### 한계
- 반드시 최적의 해를 구할 수 있는 방법이 아니므로 근사치 추정에 이용.
 

#### EX1. 동전 문제
- 지불해야 하는 값이 4720이라고 할 때, 1원, 50원, 100원 500원 동전으로 동전의 수가 가장 적게 지불하시오.
    - 가장 큰 동전부터 최대한 지불해야하는 값을 채우는 방식으로 구현.

        ```python
        cnt = 0
        money = 4720;
        for i in [500, 100, 50, 1]:
            a, b = divmod(money, i)
            cnt += a
            money = b

        print(cnt)
        ```

#### EX2. 부분 배낭 문제(Fractional Knapsack Problem) 
- 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제.
    |<center>물건[i]|<center>물건1|<center>물건2|<center>물건3|<center>물건4|<center>물건5|
    |:---:|:---:|:---:|:---:|:---:|:---:|
    |무게(w)|10|15|20|25|30|
    |가치(v)|10|12|10|8|5|

- 각 물걸은 무게(w)와 가치(v)로 표현될 수 있음.
- 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음.(**단위 무게당 가치가 가장 높은 물건부터** 욕심내어 배낭에 담기)
    - Fractional Knapsack Problem <-> 0/1 Knapsack Problem : 물건을 쪼개서 넣을 수 없는 배낭 문제. 
        
        ```python
        weight, cursum = 30, 0

        data = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
        value = sorted(data, key = lambda x : -(x[-1] / x[0]))

        for w, v in data:
            if weight - w >= 0:
                weight -= w
                cursum += v
            
            else:
                fraction = weight / w
                cursum += v * fraction
                break
                
        print(cursum)
        ```

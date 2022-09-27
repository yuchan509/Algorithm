-- 헤비 유저가 소유한 장소
select * from places
where host_id 
in (select host_id from places
    group by host_id
    having count(*) > 1)
order by id


-- 우유와 요거트가 담긴 장바구니
select cart_id from cart_products
where name in ('Milk', 'Yogurt')
group by cart_id
having (count(distinct(name))) > 1


-- 고양이와 개는 몇 마리 있을까
select animal_type, count(animal_type) as count 
from animal_ins 
group by animal_type 
order by animal_type


-- 동명 동물 수 찾기
select name, count(name) CNT
from animal_ins 
group by name 
having CNT > 1 
order by name


-- 입양 시각 구하기(1)
select 
    hour(datetime) as HOUR, 
    count(hour(datetime)) as COUNT
from animal_outs
group by hour(datetime)
having HOUR between 9 and 19
order by HOUR


-- 입양 시각 구하기(2)
set @a := -1;

select 
    (@a := @a + 1) as HOUR,
    
    (select count(*) 
    from animal_outs
    where hour(datetime) = @a) as COUNT
    
from animal_outs
where @a < 23


-- 보호소에서 중성화한 동물
select a.animal_id, a.animal_type, a.name
from animal_ins a
join animal_outs b
on a.animal_id = b.animal_id
where a.sex_upon_intake regexp 'Intact'
    and b.sex_upon_outcome regexp 'Spayed|Neutered'


-- 루시와 엘라 찾기
select animal_id, name, sex_upon_intake
from animal_ins
where name regexp '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$'
-- where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id


-- 이름에 el이 들어가는 동물 찾기
select animal_id, name
from animal_ins
where name regexp 'el' and animal_type = 'Dog'
-- where name like '%el%' and animal_type = 'Dog'
order by name


-- 중성화 여부 파악하기
select animal_id,
       name,
       if (sex_upon_intake regexp 'Intact', 'X', 'O') as 중성화
       -- if (sex_upon_intake like '%Intact%', 'X', 'O') as 중성화
from animal_ins


-- 오랜 기간 보호한 동물(1)
select a.name, a.datetime
from animal_ins a
left join animal_outs b
on a.animal_id = b.animal_id
where b.animal_id is null
order by a.datetime
limit 3


-- 오랜 기간 보호한 동물(2)
select a.animal_id, a.name
from animal_ins a
join animal_outs b
on a.animal_id = b.animal_id
order by b.datetime - a.datetime desc
limit 2


-- 최댓값 구하기
select max(datetime) from animal_ins

select datetime from animal_ins
order by datetime desc
limit 1


-- 최솟값 구하기
select min(datetime) from animal_ins


-- DATETIME에서 DATE로 형 변환
select animal_id, name, date_format(datetime, '%Y-%m-%d') as 날짜
from animal_ins
order by animal_id


-- Revising the Select Query II
select name from city
where population > 120000 and countrycode = 'USA'


-- Employee Salaries
select name from employee
where salary > 2000 and months < 10
order by employee_id


-- Weather Observation Station 1
select city, state 
from station


-- Weather Observation Station 2
select round(sum(lat_n), 2), round(sum(long_w), 2)
from station


-- Weather Observation Station 3
select distinct(city)
from station
where mod(id, 2) = 0


-- Weather Observation Station 4
select count(city) - count(distinct(city))
from station


-- Weather Observation Station 6
select city 
from station 
where city regexp '^[aeiou]'


-- Weather Observation Station 7
select distinct(city) 
from station 
where city regexp '[aeiou]$'


-- Weather Observation Station 8
select distinct(city) 
from station
where city regexp '^[aeiou]' and city regexp '[aeiou]$'


-- Weather Observation Station 9
select distinct(city) 
from station
where city regexp '^[^aeiou]'


-- Weather Observation Station 10
select distinct(city) 
from station
where city regexp '[^aeiou]$'


-- Weather Observation Station 11
select distinct(city) 
from station
where city regexp '^[^aeiou]' or city regexp '[^aeiou]$'


-- Weather Observation Station 12
select distinct(city)
from station
where city regexp '^[^aeoiu]' and city regexp '[^aeoiu]$'


-- Weather Observation Station 13
select truncate(sum(lat_n), 4)
from station
where lat_n between 38.7880 and 137.2345


-- Weather Observation Station 14
select truncate(max(lat_n), 4)
from station
where lat_n < 137.2345


-- Weather Observation Station 15
select round(long_w, 4)
from station
where lat_n = (select max(lat_n) 
               from station 
               where lat_n < 137.2345)


select round(long_w, 4)
from station
where lat_n < 137.2345
order by lat_n desc
limit 1

-- Weather Observation Station 16
select round(min(lat_n), 4)
from station
where lat_n > 38.7880


-- Weather Observation Station 17
select round(long_w, 4)
from station
where lat_n > 38.7780
order by lat_n
limit 1

select round(long_w, 4)
from station
where lat_n = 
    (select min(lat_n) 
     from station
     where lat_n > 38.7780)


-- Weather Observation Station 18
select
    round(abs(min(lat_n) - max(lat_n)) + abs(min(long_w) - max(long_w)), 4)
from station


-- Revising Aggregations - The Count Function
select count(*)
from city
where population > 100000


-- Revising Aggregations - The Sum Function
select sum(population)
from city
where district = 'California'

-- Revising Aggregations - Averages
select avg(population)
from city
where district = 'California'


-- Population Census
select sum(a.population) from city a
join country b
on a.countrycode = b.code
where b.continent = 'Asi'


-- African Cities (join)
select a.name
from city a
join country b
on a.countrycode = b.code
where b.continent = 'Africa'


-- Average Population of Each Continent (join, floor)
select b.continent, floor(avg(a.population)) 
from city a
join country b
on a.countrycode = b.code
group by b.continent


-- Population Density Difference
select max(population) - min(population)
from city


-- Top Earners (group by)
select months * salary as earnings, count(*)
from employee
group by earnings
order by earnings desc
limit 1


-- Higher Than 75 Marks (다중 정렬)
select name
from students
where marks > 75
order by right(name, 3), id


-- Select All
select *
from city


-- Select By ID
select * 
from city
where id = 1661


-- Average Population
select floor(avg(population))
from city


-- Japan Population
select sum(population) 
from city
where countrycode = 'JPN'


-- Japanese Cities' Attributes
select * 
from city
where countrycode = 'JPN'


-- Japanese Cities' Names
select name
from city
where countrycode = 'JPN'


-- Employee Names
select name
from employee
order by name


-- The Blunder (replace, ceil)
select ceil(avg(salary) - avg(replace(salary, '0', '')))
from employees


-- The PADS
select concat(name, '(', left(occupation, 1), ')')
from occupations
order by name;

select concat('There are a total of ', 
              count(occupation), 
              ' ',
              lower(occupation), 
              's.')
from occupations
group by occupation
order by count(occupation), occupation



-- 알고리즘 문제
# 1. 조합 + 집합 문제
- 문자열 s = 'BDAA' 이런식으로 주어짐 -> 'B', 'D', 'A', "A" 로 만들 수 있는 모든 문자 사전을 만들고(겹칠 수 있으므로 set 처리 - 집합 개념), 
  알파벳 기준으로 정렬처리하고, 주어진 문자열 s 다음의 값을 return 하는 문제.
  ```python
    from itertools import permutations # 조합 함수
    def solution(s):
        
        # 단어 사전(집합) 만들기.
        case = [''.join(i) for i in permutations(list(s), len(s))]
        case = list(set(res))
        
        # 정렬 및 주어진 문자열 s 인덱스 위치 찾기.
        case.sort()  
        idx = case.index(s)

        # 단어 사전이 한개나, 주어진 문자가 마지막 문자가 아니라면,
        if idx != len(s) - 1:
            ans = case[idx + 1]
        else:
            ans = case[idx]

        return ans
  ```

# 2. queue, stack
- 전광판 글자가 오른쪽에서 왼쪽 순으로 보인다. 크기가 6개인 전광판에서 6초가 지나면 hi piz 이렇게 보이며, hi_piz 으로 리턴해야함
  7초가 지났다고 가정하면 i piz  이렇게 보이며 i_piz_ 이렇게 리턴해야 한다. 
- n : 전광판 크기(6이면 6개의 글자를 담을 수 있음.)
- second : 전광판이 움직이고 지나간 시간 
- text : "hi piz"

- 코드 기억 잘 안남.
    ```python
    
    def solution(n, second, text)
    
        q = []
        text = text.replace(' ', '_')

        for i in range(second):
            
            idx = i % n
            if text[idx] in q:
                q.remove(text[idx])
            
            else:
                q.append(text[idx])
                
        chk = (second - 1) // n

        for _ in range(n - len(q)):
            if chk % 2 == 0:
                q.insert(0, '_')
            else:
                q.append('_')
                
        ans = ''.join(q)
        return ans
    ```


# 3. bfs/dfs, flood fill 응용 문제
- 0이 바다고, 1이 육지며, 각 사각형 크기의 둘레의 길이이 합을 구하는 문제.
- maps : array 배열

    ```python
        from collections import deque

        def solution(maps):
            
            ans = 0
            n, m = len(maps), len(maps[0])
            visited = [[0] * m for _ in range(n)]

            d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            def bfs(x, y):

                res = 0
                q = deque()
                q.append([x, y])
                visited[x][y] = 1

                while q:
                    x, y = q.popleft()

                    chk = 0 # nx, ny가 몇번 들어오는 지 확인.
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < m:
                            if maps[nx][ny] != 0 # 육지(1)면, 
                                chk += 1 
                                if not visited[nx][ny]:
                                    visited[nx][ny] = 1
                                    q.append([nx, ny])

                # 특정 위치 주변으로 육지 분포(chk)를 확인 후 4 - chk를 빼주면 그 만큼이 그 공간이 차지하는 둘레의 길이.
                res += (4 - chk) 

                return res
            
            # 1(육지)이면서 방문하지 않은 곳에서 bfs 탐색.
            for i in range(n):
                for j in range(m):
                    if maps[i][j] != 0 and not visited[i][j]:
                        ans += bfs(i, j)

            return ans
        ```

-- sql 복기 - ktds 역량테스트 평가(9.14)
-- if문 이용, group by, sum
select 

    cart_id,
    if (sum(price) < 50000, sum(price) + 3000, sum(price))

from cart_products
group by cart_id
order by cart_id


-- group by, having, desc 사용.
select

    chnnel_title,
    sum(views)

from youtubes
group by chnnel_title
having count(chnnel_title) > 1
order by sum(views) desc


-- case문 이용, group by, count
select 
    empolyee_id, 
    case
        when count(employee_id) > 3
        then '최우수 사원'

        when count(employee_id) > 1 and count(employee_id) <= 3
        then '우수 사원'

        else '일반 사원'
    end '컬러명 이름',

    count(employee_id) COUNT

from table_name
group by employee_id
order by employee_id


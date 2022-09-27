-- ��� ������ ������ ���
select * from places
where host_id 
in (select host_id from places
    group by host_id
    having count(*) > 1)
order by id


-- ������ ���Ʈ�� ��� ��ٱ���
select cart_id from cart_products
where name in ('Milk', 'Yogurt')
group by cart_id
having (count(distinct(name))) > 1


-- ����̿� ���� �� ���� ������
select animal_type, count(animal_type) as count 
from animal_ins 
group by animal_type 
order by animal_type


-- ���� ���� �� ã��
select name, count(name) CNT
from animal_ins 
group by name 
having CNT > 1 
order by name


-- �Ծ� �ð� ���ϱ�(1)
select 
    hour(datetime) as HOUR, 
    count(hour(datetime)) as COUNT
from animal_outs
group by hour(datetime)
having HOUR between 9 and 19
order by HOUR


-- �Ծ� �ð� ���ϱ�(2)
set @a := -1;

select 
    (@a := @a + 1) as HOUR,
    
    (select count(*) 
    from animal_outs
    where hour(datetime) = @a) as COUNT
    
from animal_outs
where @a < 23


-- ��ȣ�ҿ��� �߼�ȭ�� ����
select a.animal_id, a.animal_type, a.name
from animal_ins a
join animal_outs b
on a.animal_id = b.animal_id
where a.sex_upon_intake regexp 'Intact'
    and b.sex_upon_outcome regexp 'Spayed|Neutered'


-- ��ÿ� ���� ã��
select animal_id, name, sex_upon_intake
from animal_ins
where name regexp '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$'
-- where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by animal_id


-- �̸��� el�� ���� ���� ã��
select animal_id, name
from animal_ins
where name regexp 'el' and animal_type = 'Dog'
-- where name like '%el%' and animal_type = 'Dog'
order by name


-- �߼�ȭ ���� �ľ��ϱ�
select animal_id,
       name,
       if (sex_upon_intake regexp 'Intact', 'X', 'O') as �߼�ȭ
       -- if (sex_upon_intake like '%Intact%', 'X', 'O') as �߼�ȭ
from animal_ins


-- ���� �Ⱓ ��ȣ�� ����(1)
select a.name, a.datetime
from animal_ins a
left join animal_outs b
on a.animal_id = b.animal_id
where b.animal_id is null
order by a.datetime
limit 3


-- ���� �Ⱓ ��ȣ�� ����(2)
select a.animal_id, a.name
from animal_ins a
join animal_outs b
on a.animal_id = b.animal_id
order by b.datetime - a.datetime desc
limit 2


-- �ִ� ���ϱ�
select max(datetime) from animal_ins

select datetime from animal_ins
order by datetime desc
limit 1


-- �ּڰ� ���ϱ�
select min(datetime) from animal_ins


-- DATETIME���� DATE�� �� ��ȯ
select animal_id, name, date_format(datetime, '%Y-%m-%d') as ��¥
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


-- Higher Than 75 Marks (���� ����)
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



-- �˰��� ����
# 1. ���� + ���� ����
- ���ڿ� s = 'BDAA' �̷������� �־��� -> 'B', 'D', 'A', "A" �� ���� �� �ִ� ��� ���� ������ �����(��ĥ �� �����Ƿ� set ó�� - ���� ����), 
  ���ĺ� �������� ����ó���ϰ�, �־��� ���ڿ� s ������ ���� return �ϴ� ����.
  ```python
    from itertools import permutations # ���� �Լ�
    def solution(s):
        
        # �ܾ� ����(����) �����.
        case = [''.join(i) for i in permutations(list(s), len(s))]
        case = list(set(res))
        
        # ���� �� �־��� ���ڿ� s �ε��� ��ġ ã��.
        case.sort()  
        idx = case.index(s)

        # �ܾ� ������ �Ѱ���, �־��� ���ڰ� ������ ���ڰ� �ƴ϶��,
        if idx != len(s) - 1:
            ans = case[idx + 1]
        else:
            ans = case[idx]

        return ans
  ```

# 2. queue, stack
- ������ ���ڰ� �����ʿ��� ���� ������ ���δ�. ũ�Ⱑ 6���� �����ǿ��� 6�ʰ� ������ hi piz �̷��� ���̸�, hi_piz ���� �����ؾ���
  7�ʰ� �����ٰ� �����ϸ� i piz  �̷��� ���̸� i_piz_ �̷��� �����ؾ� �Ѵ�. 
- n : ������ ũ��(6�̸� 6���� ���ڸ� ���� �� ����.)
- second : �������� �����̰� ������ �ð� 
- text : "hi piz"

- �ڵ� ��� �� �ȳ�.
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


# 3. bfs/dfs, flood fill ���� ����
- 0�� �ٴٰ�, 1�� ������, �� �簢�� ũ���� �ѷ��� ������ ���� ���ϴ� ����.
- maps : array �迭

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

                    chk = 0 # nx, ny�� ��� ������ �� Ȯ��.
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < m:
                            if maps[nx][ny] != 0 # ����(1)��, 
                                chk += 1 
                                if not visited[nx][ny]:
                                    visited[nx][ny] = 1
                                    q.append([nx, ny])

                # Ư�� ��ġ �ֺ����� ���� ����(chk)�� Ȯ�� �� 4 - chk�� ���ָ� �� ��ŭ�� �� ������ �����ϴ� �ѷ��� ����.
                res += (4 - chk) 

                return res
            
            # 1(����)�̸鼭 �湮���� ���� ������ bfs Ž��.
            for i in range(n):
                for j in range(m):
                    if maps[i][j] != 0 and not visited[i][j]:
                        ans += bfs(i, j)

            return ans
        ```

-- sql ���� - ktds �����׽�Ʈ ��(9.14)
-- if�� �̿�, group by, sum
select 

    cart_id,
    if (sum(price) < 50000, sum(price) + 3000, sum(price))

from cart_products
group by cart_id
order by cart_id


-- group by, having, desc ���.
select

    chnnel_title,
    sum(views)

from youtubes
group by chnnel_title
having count(chnnel_title) > 1
order by sum(views) desc


-- case�� �̿�, group by, count
select 
    empolyee_id, 
    case
        when count(employee_id) > 3
        then '�ֿ�� ���'

        when count(employee_id) > 1 and count(employee_id) <= 3
        then '��� ���'

        else '�Ϲ� ���'
    end '�÷��� �̸�',

    count(employee_id) COUNT

from table_name
group by employee_id
order by employee_id


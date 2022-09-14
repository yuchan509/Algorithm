# 알고리즘 문제
# 1. 조합 + 집합 문제
# 문자열 s = 'BDAA' 이런식으로 주어짐 -> 'B', 'D', 'A', "A" 로 만들 수 있는 모든 문자 사전을 만들고(겹칠 수 있으므로 set 처리 - 집합 개념), 
# 알파벳 기준으로 정렬처리하고, 주어진 문자열 s 다음의 값을 return 하는 문제.

from itertools import permutations 

def solution(s):
    
    case = [''.join(i) for i in permutations(list(s), len(s))]
    case = list(set(case))
    
    case.sort()  
    idx = case.index(s)

    if idx != len(s) - 1:
        ans = case[idx + 1]
    else:
        ans = case[idx]

    return ans

# 2. queue, stack
# 전광판 글자가 오른쪽에서 왼쪽 순으로 보인다. 크기가 6개인 전광판에서 6초가 지나면 hi piz 이렇게 보이며, hi_piz 으로 리턴해야함
# 7초가 지났다고 가정하면 i piz  이렇게 보이며 i_piz_ 이렇게 리턴해야 한다. 
    # n : 전광판 크기(6이면 6개의 글자를 담을 수 있음.)
    # second : 전광판이 움직이고 지나간 시간 
    # text : "hi piz"

def solution(n, second, text):

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

# 보완한 효율적인 코드.
def solution(n, second, text):
    
    ans = ''
    s = '_' * n + text.replace(' ', '_')
    idx = second % (n * 2)
   
    for _ in range(n):

        idx = idx % (n * 2)
        ans += s[idx]
        idx += 1
    
    return ''.join(ans)

# 3. bfs/dfs, flood fill 응용 문제
# 0이 바다고, 1이 육지며, 각 사각형 크기의 둘레의 길이이 합을 구하는 문제.
# maps : array 배열

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
                    if maps[nx][ny] != 0: # 육지(1)면,
                        chk += 1 
                        if not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])

            # 특정 위치 주변으로 육지 분포(chk)를 확인 후 4 - chk를 빼주면,
            # 그 만큼이 그 공간이 차지하는 둘레의 길이.
            res += (4 - chk) 

        return res
    
    # 1(육지)이면서 방문하지 않은 곳에서 bfs 탐색.
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and not visited[i][j]:
                ans += bfs(i, j)

    return ans
   
'''
-- 01. if문 이용, group by, sum
select 

    cart_id,
    if (sum(price) < 50000, sum(price) + 3000, sum(price))

from cart_products
group by cart_id
order by cart_id


-- 02. group by, having, desc 사용.
select

    chnnel_title,
    sum(views)

from youtubes
group by chnnel_title
having count(chnnel_title) > 1
order by sum(views) desc


-- 03. case문 이용, group by, count
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
'''
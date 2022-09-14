# �˰��� ����
# 1. ���� + ���� ����
# ���ڿ� s = 'BDAA' �̷������� �־��� -> 'B', 'D', 'A', "A" �� ���� �� �ִ� ��� ���� ������ �����(��ĥ �� �����Ƿ� set ó�� - ���� ����), 
# ���ĺ� �������� ����ó���ϰ�, �־��� ���ڿ� s ������ ���� return �ϴ� ����.

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
# ������ ���ڰ� �����ʿ��� ���� ������ ���δ�. ũ�Ⱑ 6���� �����ǿ��� 6�ʰ� ������ hi piz �̷��� ���̸�, hi_piz ���� �����ؾ���
# 7�ʰ� �����ٰ� �����ϸ� i piz  �̷��� ���̸� i_piz_ �̷��� �����ؾ� �Ѵ�. 
    # n : ������ ũ��(6�̸� 6���� ���ڸ� ���� �� ����.)
    # second : �������� �����̰� ������ �ð� 
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

# ������ ȿ������ �ڵ�.
def solution(n, second, text):
    
    ans = ''
    s = '_' * n + text.replace(' ', '_')
    idx = second % (n * 2)
   
    for _ in range(n):

        idx = idx % (n * 2)
        ans += s[idx]
        idx += 1
    
    return ''.join(ans)

# 3. bfs/dfs, flood fill ���� ����
# 0�� �ٴٰ�, 1�� ������, �� �簢�� ũ���� �ѷ��� ������ ���� ���ϴ� ����.
# maps : array �迭

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
                    if maps[nx][ny] != 0: # ����(1)��,
                        chk += 1 
                        if not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append([nx, ny])

            # Ư�� ��ġ �ֺ����� ���� ����(chk)�� Ȯ�� �� 4 - chk�� ���ָ�,
            # �� ��ŭ�� �� ������ �����ϴ� �ѷ��� ����.
            res += (4 - chk) 

        return res
    
    # 1(����)�̸鼭 �湮���� ���� ������ bfs Ž��.
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and not visited[i][j]:
                ans += bfs(i, j)

    return ans
   
'''
-- 01. if�� �̿�, group by, sum
select 

    cart_id,
    if (sum(price) < 50000, sum(price) + 3000, sum(price))

from cart_products
group by cart_id
order by cart_id


-- 02. group by, having, desc ���.
select

    chnnel_title,
    sum(views)

from youtubes
group by chnnel_title
having count(chnnel_title) > 1
order by sum(views) desc


-- 03. case�� �̿�, group by, count
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
'''
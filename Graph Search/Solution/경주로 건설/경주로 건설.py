from collections import deque

def solution(board):
    
    n = len(board)
    # 좌(0), 상(1), 하(2), 우(3)
    # 좌(0) + 우(3) (수평) <-> 상(1) + 하(2) (수직)
    d = [(0, 0, -1), (1, -1, 0), (2, 1, 0), (3, 0, 1)]

    visited = [[[float("inf")] * 4 for _ in range(n)] for _ in range(n)]
    visited[0][0] = [0, 0, 0, 0]

    q = deque()
     # 시작 지점 : index -> (0, 0), 방향 없음 상태 : -1
    q.append([0, 0, -1])

    while q:
        x, y, direct = q.popleft()

        for curdir, dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:

                '''코너(Coner) 발생 조건.
                01. 무방향 상태가 아니면서(시작 지점에서는 코너 발생 불가)
                02. 수평 <-> 수직 변환이 이루어져야 함.
                03. 이전 방향(direct)와 현재 방향(curdir)이 달라야함.
                
                위 세가지 조건을 만족한다면, (100 + 500) = 600 비용 추가.
                ''' 

                if direct != -1 and (direct + curdir) != 3 and direct != curdir:
                    cost = 600
                else:
                    cost = 100
                
                # 같은 index (x, y) 지점을 재방문 할 수 있으므로, 3d 배열 구성.
                if board[nx][ny] != 1 and visited[nx][ny][curdir] > visited[x][y][direct] + cost:                    
                    visited[nx][ny][curdir] = visited[x][y][direct] + cost
                    q.append([nx, ny, curdir])

    return min(visited[-1][-1])


# Run.
# output : 3200
board = [[0,0,0,0,0,0],
        [0,1,1,1,1,0]
        [0,0,1,0,0,0],
        [1,0,0,1,0,1],
        [0,1,0,0,0,1],
        [0,0,0,0,0,0]]
        
solution(board)
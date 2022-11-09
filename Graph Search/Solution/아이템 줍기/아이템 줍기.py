from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):

    MAX = 102
    space = [['#'] * MAX for i in range(MAX)]
    
    # 시계 방향 180도 회전 space 배열 생성. -> (3, 1) -> (8, 7) 좌표 반대. (x, y) -> (y, x)로 탐색.
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x : x * 2 , r)
        
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if x1 < j < x2 and y1 < i < y2:
                    space[i][j] = 0
                    
                elif space[i][j] != 0:
                    space[i][j] = 1
    

    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    characterX, characterY, itemX, itemY = map(lambda x : x * 2, [characterX, characterY, itemX, itemY])
    
    q = deque()
    q.append([characterY, characterX, 0])
    
    v = [[0] * MAX for i in range(MAX)]
    v[characterY][characterX ] = 1
    
    while q:
        y, x, length = q.popleft()
        
        if y == itemY and x == itemX:
            break
            
        for dx, dy in d:
            ny = y + dy
            nx = x + dx
            
            if not v[ny][nx] and space[ny][nx] == 1:
                v[ny][nx] = 1
                q.append([ny, nx, length + 1])
    
    ans = length // 2
    
    return ans

    
    '''
    output : 17
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    '''
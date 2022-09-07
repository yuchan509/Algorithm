from collections import deque

def solution(board, moves):

    ans, res = 0, [-1]
    n = len(board)
    q = deque(moves)

    while q:
        p = q.popleft()

        for x in range(n):
            v = board[x][p - 1]
            board[x][p - 1] = 0

            if v != 0:
                if res[-1] != v:
                    res.append(v)
                else:
                    res.pop()
                    ans += 1 * 2
                break
    return ans
    
```
output : 4
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]		
```
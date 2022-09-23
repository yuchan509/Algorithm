from collections import deque, defaultdict

def solution(info, edges):

    graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)

    def bfs():

        ans = 0
        q = deque()
        q.append([[0], 1, 0])

        while q:

            nodes, sheep, wolf = q.popleft()
            v = {node for node in nodes}
            ans = max(ans, sheep)

            for node in nodes:
                for x in graph[node]:
                    ns = sheep
                    nw = wolf

                    if x not in v and info[x] == 0:
                        ns += 1
                    else:
                        nw += 1

                    if ns > nw:
                        q.append([nodes + [x], ns, nw])
        return ans

    return bfs()


'''
output : 5
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
'''
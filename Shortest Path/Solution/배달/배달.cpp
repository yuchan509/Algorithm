/* ¹è´Þ */
#include <iostream>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

vector<pair<int, int>> graph[51]; // { dest, cost }
int DP[51];
bool visited[51];

int dijkstra(int N, int K)
{
    int ret = 0;
    int cur, next, cost, ncost;
    priority_queue<
        pair<int, int>, // { cost, vtx }
        vector<pair<int, int>>,
        greater<pair<int, int>>
    > PQ;

    visited[1] = 1;
    PQ.push({ 0, 1 });

    while (!PQ.empty())
    {
        cost = PQ.top().first;
        cur = PQ.top().second;
        PQ.pop();

        for (size_t i = 0; i < graph[cur].size(); i++)
        {
            next = graph[cur][i].first;
            ncost = graph[cur][i].second;
            if (!visited[next])
            {
                visited[next] = 1;
                DP[next] = DP[cur] + ncost;
                PQ.push({ DP[next], next });
            }
            else
            {
                if (DP[next] > DP[cur] + ncost)
                {
                    DP[next] = DP[cur] + ncost;
                    PQ.push({ DP[next], next });
                }
            }
        }
    }

    for (int i = 1; i <= N; i++)
    {
        if (DP[i] <= K) ret++;
    }
    return ret;
}

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;

    int a, b, c;
    for (size_t i = 0; i < road.size(); i++)
    {
        a = road[i][0];
        b = road[i][1];
        c = road[i][2];

        graph[a].push_back({ b, c });
        graph[b].push_back({ a, c });
    }

    answer = dijkstra(N, K);
    return answer;
}
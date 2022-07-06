/* ÆÄÆ¼ */
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <functional>
using namespace std;

int N, M, X, res;
vector<pair<int, int>> graph[1001];	// first : dest, second : dist
bool visited[1001];
int DP[1001][1001];

void dijkstra(int start)
{
	priority_queue<
		pair<int, int>,
		vector<pair<int, int>>,
		greater<pair<int, int>>
	> PQ;

	visited[start] = 1;
	PQ.push({ start, 0 });

	int next, weight;
	pair<int, int> cur;
	while (!PQ.empty())
	{
		cur = PQ.top();
		PQ.pop();

		for (size_t i = 0; i < graph[cur.first].size(); i++)
		{
			next = graph[cur.first][i].first;
			weight = graph[cur.first][i].second;
			if (!visited[next])
			{
				visited[next] = 1;
				DP[start][next] = DP[start][cur.first] + weight;
				PQ.push({ next, DP[start][next] });
			}
			else
			{
				if (DP[start][next] > DP[start][cur.first] + weight)
				{
					DP[start][next] = DP[start][cur.first] + weight;
					PQ.push({ next, DP[start][next] });
				}
			}
		}
	}
}

int main()
{
	cin >> N >> M >> X;
	int src, dest, dist;
	while (M--)
	{
		cin >> src >> dest >> dist;
		graph[src].push_back({ dest, dist });
	}

	for (int i = 1; i <= N; i++)
	{
		dijkstra(i);
		memset(visited, 0, sizeof(visited));
	}

	for (int i = 1; i <= N; i++)
	{
		res = max(res, DP[i][X] + DP[X][i]);
	}
	cout << res << '\n';
	return 0;
}
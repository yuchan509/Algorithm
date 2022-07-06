/* Find the nearest clone */
#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;

int color[1000001];
bool visited[1000001];
vector<int> graph[1000001];

int bfs(int start, int color_id)
{
	queue<pair<int, int>> Q;
	int cur, next, cost;
	int ret = 987654321;

	Q.push({ start, 0 });
	visited[start] = 1;

	while (!Q.empty())
	{
		cur = Q.front().first;
		cost = Q.front().second;
		Q.pop();

		for (size_t i = 0; i < graph[cur].size(); i++)
		{
			next = graph[cur][i];
			if (!visited[next])
			{
				visited[next] = 1;
				if (color[next] == color_id)
				{
					ret = min(ret, cost + 1);
					Q.push({ next, 0 });
				}
				else
				{
					Q.push({ next, cost + 1 });
				}
			}
		}
	}
	return ret;
}

int main()
{
	int n, m, src, dest, color_id;
	vector<int> vec;

	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> src >> dest;
		graph[src].push_back(dest);
		graph[dest].push_back(src);
	}
	for (int i = 1; i <= n; i++)
	{
		cin >> color[i];
	}
	cin >> color_id;

	int start = 0;
	for (int i = 1; i <= n; i++)
	{
		if (color[i] == color_id)
		{
			start = i;
			break;
		}
	}

	int res = bfs(start, color_id);

	if (res == 987654321)	cout << -1 << '\n';
	else					cout << res << '\n';
	return 0;
}
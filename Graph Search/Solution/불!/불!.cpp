/* ��! */
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int drow[4] = { 0, -1, 0, 1 };
int dcol[4] = { -1, 0, 1, 0 };

pair<int, int> J;
vector<pair<int, int>> F;
char maze[1001][1001];
int visited[1001][1001];
int DP[1001][1001];

int solution(int R, int C)
{
	queue<pair<pair<int, int>, bool>> Q; // { { r, c }, flag }
	int ret = -1;
	int r, c, nr, nc, res = 0;
	bool flag = 0; // if flag == 0 then J, else F

	Q.push({ J, 0 });
	visited[J.first][J.second] = 1;

	for (size_t i = 0; i < F.size(); i++)
	{
		Q.push({ {F[i].first, F[i].second}, 1 });
		visited[F[i].first][F[i].second] = 2;
	}

	while (!Q.empty())
	{
		r = Q.front().first.first;
		c = Q.front().first.second;
		flag = Q.front().second;
		Q.pop();

		if (!flag && visited[r][c] == 2)	continue; // �ҿ� ���� ���

		for (int i = 0; i < 4; i++)
		{
			nr = r + drow[i];
			nc = c + dcol[i];
			if (nr < 0 || nr >= R || nc < 0 || nc >= C) // �̷� �ܰ�
			{
				if (!flag)	return DP[r][c] + 1;
				else continue;
			}
			if (maze[nr][nc] == '#')	continue;
			if (!flag) // J
			{
				if (maze[nr][nc] != 'F' && !visited[nr][nc])
				{
					visited[nr][nc] = 1;
					DP[nr][nc] = DP[r][c] + 1;
					Q.push({ {nr, nc}, flag });
				}
			}
			else // F
			{
				if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
				if (visited[nr][nc] != 2)
				{
					visited[nr][nc] = 2;
					Q.push({ {nr, nc}, flag });
				}
			}
		}
	}
	return ret;
}

int main()
{
	int R, C;
	cin >> R >> C;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cin >> maze[i][j];
			if (maze[i][j] == 'J')
			{
				J = { i, j };
			}
			else if (maze[i][j] == 'F')
			{
				F.push_back({ i, j });
			}
		}
	}

	int res = solution(R, C);
	if (res == -1)
	{
		cout << "IMPOSSIBLE";
	}
	else
	{
		cout << res;
	}
	return 0;
}
/* BOJ 2151 (거울 설치) */
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

enum { LEFT = 0, NORTH, RIGHT, SOUTH };
int drow[4] = { 0, -1, 0, 1 };
int dcol[4] = { -1, 0, 1, 0 };

int N;
char matrix[50][50];
bool visited[4][50][50];
char input[50];
vector<pair<int, int>> door;
queue<tuple<pair<int, int>, int, int>> Q;	// {r, c}, dir, cnt

void move(int r, int c, int dir, int cnt)
{
	int nr = r + drow[dir], nc = c + dcol[dir];
	while (true)
	{
		if (nr < 0 || nr >= N || nc < 0 || nc >= N)	break;
		if (matrix[nr][nc] == '*')	break;
		if (matrix[nr][nc] != '.' && visited[dir][nr][nc] == 0)
		{
			visited[dir][nr][nc] = 1;
			if (matrix[nr][nc] == '#')
			{
				Q.push({ {nr, nc}, dir, cnt });
			}
			else
			{
				Q.push({ {nr, nc}, dir, cnt + 1 });
			}
		}
		nr += drow[dir], nc += dcol[dir];
	}
}

int bfs(int r, int c)
{
	int nr, nc, dir, cnt = 0;
	pair<int, int> cur;

	for (int i = 0; i < 4; i++)
	{
		nr = r + drow[i];
		nc = c + dcol[i];
		if (nr < 0 || nr >= N || nc < 0 || nc >= N)	continue;
		move(r, c, i, 0);
	}

	while (!Q.empty())
	{
		cur = get<0>(Q.front());
		dir = get<1>(Q.front());
		cnt = get<2>(Q.front());
		Q.pop();
		if (cur.first == door[1].first && cur.second == door[1].second)	break;	// 반대쪽 문에 도달했을 경우

		if (dir == NORTH || dir == SOUTH)
		{
			/* LEFT */
			move(cur.first, cur.second, 0, cnt);

			/* RIGHT */
			move(cur.first, cur.second, 2, cnt);
		}
		if (dir == LEFT || dir == RIGHT)
		{
			/* NORTH */
			move(cur.first, cur.second, 1, cnt);

			/* SOUTH */
			move(cur.first, cur.second, 3, cnt);
		}
	}
	return cnt;
}

int main()
{
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> input;
		for (int j = 0; j < N; j++)
		{
			matrix[i][j] = input[j];
			if (matrix[i][j] == '#')
			{
				door.push_back({ i, j });
			}
		}
	}

	cout << bfs(door[0].first, door[0].second) << '\n';
	return 0;
}
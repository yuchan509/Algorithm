/* BOJ 14503 (로봇 청소기) */
#include <iostream>
#include <queue>
using namespace std;

int drow[4] = { -1, 0, 1, 0 };
int dcol[4] = { 0, 1, 0, -1 };
int matrix[50][50];
bool visited[50][50];
int main()
{
	int N, M, r, c, d;
	cin >> N >> M >> r >> c >> d;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> matrix[i][j];
		}
	}

	visited[r][c] = 1;
	int nr, nc, nd, cnt = 1, flag = 0;
	while (true)
	{
		if (flag == 4)
		{
			nd = (d + 2) % 4;
			nr = r + drow[nd];
			nc = c + dcol[nd];
			if (!matrix[nr][nc])
			{
				r = nr, c = nc;
				flag = 0;
			}
			else
			{
				break;
			}
		}

		d--;
		if (d < 0)	d = 3;

		nr = r + drow[d];
		nc = c + dcol[d];

		if (!matrix[nr][nc])
		{
			if (!visited[nr][nc])
			{
				r = nr, c = nc;
				visited[r][c] = 1;
				cnt++;
				flag = 0;
			}
			else
			{
				flag++;
			}
		}
		else
		{
			flag++;
		}
	}

	cout << cnt;
	return 0;
}
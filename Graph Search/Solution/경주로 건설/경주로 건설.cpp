/* ���ַ� �Ǽ� */
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int drow[4] = { 0, -1, 0, 1 };
int dcol[4] = { -1, 0, 1, 0 };

int DP[25][25][4];
// bool visited[25][25][4]; DP�迭�� �ּҰ����� ��� ���ŵǸ� ���̻� ť�� ���� �����Ƿ� �湮üũ�� ���� �����൵ ��

struct car
{
	int r, c, dir, cost;
};

int solution(vector<vector<int>> board) {
	int answer = 0;
	int N = (int)board.size();
	int r, c, nr, nc, dir, cost, ncost;
	queue<car> Q;

	/* DP�迭 �ʱ�ȭ */
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				DP[i][j][k] = 987654321;
			}
		}
	}

	/* ����� �ʱ�ȭ */
	for (int i = 0; i < 4; i++)
	{
		DP[0][0][i] = 0;
	}
	Q.push({ 0, 0, -1, 0 });

	while (!Q.empty())
	{
		r = Q.front().r;
		c = Q.front().c;
		dir = Q.front().dir;
		cost = Q.front().cost;
		Q.pop();

		for (int i = 0; i < 4; i++)
		{
			nr = r + drow[i];
			nc = c + dcol[i];
			if (nr < 0 || nr >= N || nc < 0 || nc >= N || board[nr][nc]) continue;

			ncost = cost + 100;
			if (dir >= 0 && (dir % 2) != (i % 2)) // �ٸ� ����
			{
				ncost += 500;
			}

			if (DP[nr][nc][i] > ncost)
			{
				DP[nr][nc][i] = ncost;
				Q.push({ nr, nc, i, ncost });
			}
		}
	}

	answer = *min_element(DP[N - 1][N - 1], DP[N - 1][N - 1] + 4);
	return answer;
}
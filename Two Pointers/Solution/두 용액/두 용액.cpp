/* BOJ 2470 (두 용액) */
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

int arr[100001];
int main()
{
	int N;
	int Min = 2147483647;
	vector<int> res;
	map<int, pair<int, int>> M;

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	sort(arr, arr + N);
	if (arr[0] >= 0) // 양수만 주어질 경우
	{
		res.push_back(arr[0]), res.push_back(arr[1]);
	}
	else if (arr[N - 1] < 0) // 음수만 주어질 경우
	{
		res.push_back(arr[N - 1]), res.push_back(arr[N - 2]);
	}
	else
	{
		int left = 0, right = N - 1;
		int sum = 0;
		while (left < right)
		{
			sum = arr[left] + arr[right];
			Min = min(Min, abs(arr[left] + arr[right]));
			M.insert({ abs(sum), { arr[left], arr[right] } });
			if (sum > 0)
			{
				right--;
			}
			else if (sum < 0)
			{
				left++;
			}
			else // sum == 0
			{
				cout << arr[left] << " " << arr[right] << '\n';
				return 0;
			}
		}
		res.push_back(M.find(Min)->second.first);
		res.push_back(M.find(Min)->second.second);
	}

	sort(res.begin(), res.end());
	for (size_t i = 0; i < 2; i++)
	{
		cout << res[i] << " ";
	}
	return 0;
}

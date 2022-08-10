/* BOJ 2473 (세 용액) */
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <tuple>
using namespace std;

long long arr[5001];
int main()
{
	tuple<long long, long long, long long> res;
	long long Min = 3000000001;
	int N;

	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}

	sort(arr, arr + N);
	long long sum;
	int left, right;
	for (int pivot = 0; pivot < N; pivot++)
	{
		left = pivot + 1;
		right = N - 1;

		while (left < right)
		{
			sum = arr[pivot] + arr[left] + arr[right];
			if (Min > llabs(sum))
			{
				Min = llabs(sum);
				res = { arr[pivot], arr[left], arr[right] };
			}

			if (sum < 0)	left++;
			else	right--;
		}
	}

	cout << get<0>(res) << " " << get<1>(res) << " " << get<2>(res);
	return 0;
}

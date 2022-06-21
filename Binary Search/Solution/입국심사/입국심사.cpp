/* 입국심사 */
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long start, end, mid, num;

    sort(times.begin(), times.end());

    start = 1; // 심사 시간이 1초인 1명의 심사관이 1명의 입국자를 심사하는 경우
    end = (long long)times.back() * n; // 모든 입국자가 심사시간이 가장 큰 심사관에 몰리는 경우

    while (start <= end)
    {
        mid = (start + end) / 2;
        num = 0;

        for (size_t i = 0; i < times.size(); i++)
        {
            num += mid / (long long)times[i]; // 해당 심사시간 케이스에 대해 각각의 심사위원이 입국처리시키는 입국자의 수의 합
        }

        if (num >= n) // 심사 시간을 더 줄일 수 있는 경우
        {
            end = mid - 1;
            answer = mid;
        }
        else
        {
            start = mid + 1;
        }
    }
    return answer;
}
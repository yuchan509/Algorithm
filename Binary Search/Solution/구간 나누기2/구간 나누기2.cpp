/* 구간 나누기2 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> vec;
bool check(int mid, int M) // 조건에 맞게 M개 이하의 구간으로 나눌 수 있을 경우
{
    int cnt = 1; // 1개의 구간으로 시작
    int minVal = vec[0], maxVal = vec[0];
    for (size_t i = 1; i < vec.size(); i++)
    {
        minVal = min(minVal, vec[i]); // 최소값을 구해나감
        maxVal = max(maxVal, vec[i]); // 최대값을 구해나감
        if ((maxVal - minVal) > mid)  // 조건에 맞는 구간을 찾았을 경우
        {
            /* 새로운 구간 시작 */
            cnt++;
            minVal = vec[i];
            maxVal = vec[i];
        }
    }
    return (M >= cnt);
}

int solution(int N, int M)
{
    int ret = 987654321;
    int left = 0; // 구간의 크기가 1일 경우
    int right = *max_element(vec.begin(), vec.end()); // 배열의 최대값
    int mid;

    /* 이분탐색 시작 */
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (check(mid, M))
        {
            ret = min(ret, mid); // 최대값의 최소값 갱신
            right = mid - 1; // 최대를 줄여보기
        }
        else
        {
            left = mid + 1; // 최소를 늘려보기
        }
    }
    return ret;
}

int main()
{
    int N, M, val;
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        cin >> val;
        vec.push_back(val);
    }
    cout << solution(N, M);
    return 0;
}
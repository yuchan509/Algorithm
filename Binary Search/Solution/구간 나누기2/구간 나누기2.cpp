/* ���� ������2 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> vec;
bool check(int mid, int M) // ���ǿ� �°� M�� ������ �������� ���� �� ���� ���
{
    int cnt = 1; // 1���� �������� ����
    int minVal = vec[0], maxVal = vec[0];
    for (size_t i = 1; i < vec.size(); i++)
    {
        minVal = min(minVal, vec[i]); // �ּҰ��� ���س���
        maxVal = max(maxVal, vec[i]); // �ִ밪�� ���س���
        if ((maxVal - minVal) > mid)  // ���ǿ� �´� ������ ã���� ���
        {
            /* ���ο� ���� ���� */
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
    int left = 0; // ������ ũ�Ⱑ 1�� ���
    int right = *max_element(vec.begin(), vec.end()); // �迭�� �ִ밪
    int mid;

    /* �̺�Ž�� ���� */
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (check(mid, M))
        {
            ret = min(ret, mid); // �ִ밪�� �ּҰ� ����
            right = mid - 1; // �ִ븦 �ٿ�����
        }
        else
        {
            left = mid + 1; // �ּҸ� �÷�����
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
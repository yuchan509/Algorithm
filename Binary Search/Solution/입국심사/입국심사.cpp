/* �Ա��ɻ� */
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long start, end, mid, num;

    sort(times.begin(), times.end());

    start = 1; // �ɻ� �ð��� 1���� 1���� �ɻ���� 1���� �Ա��ڸ� �ɻ��ϴ� ���
    end = (long long)times.back() * n; // ��� �Ա��ڰ� �ɻ�ð��� ���� ū �ɻ���� ������ ���

    while (start <= end)
    {
        mid = (start + end) / 2;
        num = 0;

        for (size_t i = 0; i < times.size(); i++)
        {
            num += mid / (long long)times[i]; // �ش� �ɻ�ð� ���̽��� ���� ������ �ɻ������� �Ա�ó����Ű�� �Ա����� ���� ��
        }

        if (num >= n) // �ɻ� �ð��� �� ���� �� �ִ� ���
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
/* BOJ 1541 (잃어버린 괄호) */
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int main()
{
	string input, str;
	vector<int> vec;

	cin >> input;

	/* 문자열 파싱 */
	int sign = 1;
	for (size_t i = 0; i < input.size(); i++)
	{
		if (input[i] == '-')
		{
			vec.push_back(atoi(&str[0]) * sign);
			str.clear();
			sign = -1;
		}
		else if (input[i] == '+')
		{
			vec.push_back(atoi(&str[0]) * sign);
			str.clear();
			sign = 1;
		}
		else
		{
			str.push_back(input[i]);
		}
	}
	vec.push_back(atoi(&str[0]) * sign);

	/* -를 만나면 그 뒤의 값은 모두 음수로 취급함 */
	int answer = 0;
	bool flag = false;
	for (size_t i = 0; i < vec.size(); i++)
	{
		if (vec[i] < 0)	flag = true;
		if (flag)
		{
			if (vec[i] >= 0) vec[i] *= -1;
		}
		answer += vec[i];
	}
	cout << answer << '\n';
	return 0;
}



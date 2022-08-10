/* BOJ 2504 (°ýÈ£ÀÇ °ª) */
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int solution(string str)
{
	int answer = 0;
	bool flag = true;
	stack<char> stk;
	int tmp = 1;

	for (size_t i = 0; i < str.size(); i++)
	{
		if (str[i] == '(')
		{
			stk.push('(');
			tmp *= 2;
		}
		else if (str[i] == ')')
		{
			if (stk.empty() || stk.top() != '(')
			{
				flag = false;
				break;
			}
			if (str[i - 1] == '(')
			{
				answer += tmp;
			}
			tmp /= 2;
			stk.pop();
		}
		else if (str[i] == '[')
		{
			stk.push('[');
			tmp *= 3;
		}
		else // str[i] == ']'
		{
			if (stk.empty() || stk.top() != '[')
			{
				flag = false;
				break;
			}
			if (str[i - 1] == '[')
			{
				answer += tmp;
			}
			tmp /= 3;
			stk.pop();
		}
	}

	if (!flag || !stk.empty())	answer = 0;
	return answer;
}

int main()
{
	string str;
	cin >> str;
	cout << solution(str);
	return 0;
}

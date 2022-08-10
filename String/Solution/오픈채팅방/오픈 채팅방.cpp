/* 오픈 채팅방 */
#include <string>
#include <vector>
#include <map>
using namespace std;

string input[3]; // command, id, name
vector<string> solution(vector<string> record) {
	vector<string> answer;
	vector<pair<string, string>> vec;
	map<string, string> M;

	string command, id, name;

	int idx;
	for (size_t i = 0; i < record.size(); i++)
	{
		/* 문자열 파싱 */
		idx = 0;
		for (size_t j = 0; j < record[i].size(); j++)
		{
			if (record[i][j] == ' ')
			{
				idx++;
				continue;
			}
			input[idx].push_back(record[i][j]);
		}

		command = input[0], input[0].clear();
		id = input[1], input[1].clear();
		name = input[2], input[2].clear();

		/* id에 대한 name 갱신 */
		if (command == "Enter" || command == "Change")
		{
			if (M.count(id) == 0)
			{
				M.insert({ id, name });
			}
			else
			{
				M[id] = name;
			}
		}

		/* 로그인-로그아웃 기록 시간 순서대로 삽입 */
		if (command != "Change")
		{
			vec.push_back({ id, command });
		}
	}

	/* id에 대한 가장 최근 name 기준으로 결과 삽입 */
	string str;
	for (size_t i = 0; i < vec.size(); i++)
	{
		str += M[vec[i].first];
		if (vec[i].second == "Enter")
		{
			str += "님이 들어왔습니다.";
		}
		else
		{
			str += "님이 나갔습니다.";
		}
		answer.push_back(str);
		str.clear();
	}

	return answer;
}
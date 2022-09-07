#include <string>
#include <vector>
#include <set>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    set<string> S;

    for (size_t i = 0; i < phone_book.size(); i++)
    {
        S.insert(phone_book[i]);
    }

    for (size_t i = 0; i < phone_book.size(); i++)
    {
        string cur;
     
        for (size_t j = 0; j < phone_book[i].size(); j++)
        {
            cur += phone_book[i][j];
            if (S.count(cur) && phone_book[i] != cur)
            {
                answer = false;
                break;
            }
        }
        if (answer == false) break;
    }
    return answer;
}


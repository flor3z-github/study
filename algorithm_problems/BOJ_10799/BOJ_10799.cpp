#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(string arrangement) {
    int answer = 0;
    stack<int> stack;
    vector<int> lazer;

    for (int i = 0; i < arrangement.size(); i++) {
        if (arrangement[i] == '(') {
            stack.push(i);
            if (arrangement[i + 1] == ')') {
                lazer.push_back(stack.top());
                stack.pop();
                i++;
            }
        } else {
            for (int j = 0; j < lazer.size(); j++) {
                if (lazer.at(j) > stack.top() && lazer.at(j) < i) {
                    answer++;
                }
            }
            stack.pop();
            answer++;
        }
    }
    return answer;
}

int main() {
    string arr;

    cin >> arr;
    cout << solution(arr) << endl;

    return 0;
}
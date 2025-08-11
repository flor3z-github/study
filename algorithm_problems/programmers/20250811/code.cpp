#include <bits/stdc++.h>

using namespace std;

vector<int> numbers = {2,1,3,4,1};

vector<int> solution(vector<int> numbers) {
    vector<int> answer;

    for (long unsigned int i = 0; i < numbers.size(); i++) {
        for (auto j = i + 1; j < numbers.size(); j++) {
            int sum = numbers.at(i)+numbers.at(j);
            if (find(answer.begin(), answer.end(), sum) == answer.end()) {
                answer.push_back(sum);
            }
        }
    }

    sort(answer.begin(), answer.end());

    return answer;
}

int main() {
    for (int i : solution(numbers)) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
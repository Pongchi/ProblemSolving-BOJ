// URL : https://www.acmicpc.net/problem/19941

#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, K;
    cin >> N >> K;
    
    string chair;
    cin >> chair;

    queue<int> hamberger;
    queue<int> person;
    for (int i=0; i < N; i++) {
        if (chair[i] == 'H') hamberger.push(i);
        else person.push(i);
    }

    int result = 0;
    while (!hamberger.empty() && !person.empty()) {
        if (abs(person.front() - hamberger.front()) <= K) {
            result++;
            person.pop(); hamberger.pop();
        }
        else {
            if (person.front() < hamberger.front()) person.pop();
            else hamberger.pop();
        }
    }

    cout << result << '\n';
    
    return 0;
}
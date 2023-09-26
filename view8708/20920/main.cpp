// URL : https://www.acmicpc.net/problem/20920

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool compare(string, string);

vector<string> memo;
map<string, int> counter;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    for (int i=0; i < N; i++) {
        string word; cin >> word;

        if (word.length() >= M) {
            if (counter.find(word) == counter.end()) {
                counter[word] = 0;
                memo.push_back(word);
            }
            else counter[word]++;
        }
    }

    sort(memo.begin(), memo.end(), compare);
    for (int i=0; i < memo.size(); i++) {
        cout << memo[i] << '\n';
    }
    
    return 0;
}

bool compare(string a, string b) {
    if (counter[a] != counter[b]) return counter[a] > counter[b];
    else {
        if (a.length() != b.length()) return a.length() > b.length();
        else {
            return b.compare(a) > 0;
        }
    }
}
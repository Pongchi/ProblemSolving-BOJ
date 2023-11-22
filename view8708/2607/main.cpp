// URL : https://www.acmicpc.net/problem/2607

#include <cstring>
#include <string>
#include <iostream>

using namespace std;

int counter[26];

bool isSimilar(string other);
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    int N;
    cin >> N;

    string word;
    cin >> word;

    for (int i=0; i < word.length(); i++) {
        counter[word[i] - 'A']++;
    }

    int result = 0;
    for (int i=0; i < N-1; i++) {
        string other;
        cin >> other;

        int diff = word.length() - other.length();
        if (abs(diff) <= 1 && isSimilar(other)) result++;
    }

    cout << result << '\n';

    return 0;
}

bool isSimilar(string other) {
    int other_counter[26];
    memset(other_counter, 0, sizeof(other_counter));
    for (int j=0; j < other.length(); j++) {
        other_counter[other[j] - 'A']++;
    }

    int diff_word = 0;
    for (int j=0; j < 26; j++) {
        if (counter[j] != other_counter[j]) {
            diff_word += abs(counter[j] - other_counter[j]);
            if (diff_word > 2) return false;
        }
    }
    return true;
}
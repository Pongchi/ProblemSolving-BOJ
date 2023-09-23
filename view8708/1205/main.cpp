// URL : https://www.acmicpc.net/problem/1205

#include <iostream>

using namespace std;

const int MAX_SIZE = 55;
int scores[MAX_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, new_score, P;
    cin >> N >> new_score >> P;

    int result = 1;
    int duplication = 0;
    for (int i=0;  i < N; i++) {
        cin >> scores[i];

        if (scores[i] > new_score) result++;
        if (scores[i] == new_score) duplication++;
    }

    cout << ((result+duplication) <= P ? result : -1) << '\n';
    
    return 0;
}
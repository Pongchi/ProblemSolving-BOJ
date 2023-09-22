// URL : https://www.acmicpc.net/problem/25757

#include <iostream>
#include <set>

using namespace std;

const int MAX_SIZE = 100'005;
string players[MAX_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, needPlayer;
    char T;
    cin >> N >> T;

    switch (T) {
        case 'Y': needPlayer = 1; break;
        case 'F': needPlayer = 2; break;
        case 'O': needPlayer = 3; break;
    }

    set<string> players;
    for (int i=0; i < N; i++) {
        string player;
        cin >> player;
        players.insert(player);
    }

    cout << players.size() / needPlayer << '\n';
    
    return 0;
}
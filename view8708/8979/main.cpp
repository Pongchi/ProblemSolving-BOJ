// URL : https://www.acmicpc.net/problem/8979

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, vector<int>> pii;

vector<pii> COUNTRY;

bool compare(pii a, pii b) {
    for (int i=0; i < 3; i++) {
        if (a.second.at(i) != b.second.at(i)) {
            return a.second.at(i) > b.second.at(i);
        }
    }
    return false;
}

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    int N, K;
    cin >> N >> K;

    pii k;
    for (int i=0; i < N; i++) {
        int n; cin >> n;
        int gold, silver, bronze;
        cin >> gold >> silver >> bronze;

        vector<int> prize;
        prize.push_back(gold); prize.push_back(silver); prize.push_back(bronze);
        if (n == K) {
            k = make_pair(n, prize);
        } else {
            COUNTRY.push_back(make_pair(n, prize));
        }
    }

    int result = 1;
    for (int i=0; i < COUNTRY.size(); i++) {
        if (compare(COUNTRY[i], k)) {
            result++;
        }
    }

    cout << result << '\n';

    return 0;
}
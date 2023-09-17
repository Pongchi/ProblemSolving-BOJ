// URL : https://www.acmicpc.net/problem/8979

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, vector<int>> pii;

const int MAX_SIZE = 100'5;
vector<pii> COUNTRY;

bool compare(pii a, pii b) {
    for (int i=0; i < 3; i++) {
        if (a.second[i] != b.second[i]) {
            return a.second[i] > b.second[i];
        }
    }
    return true;
}

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    int N, K;
    cin >> N >> K;

    for (int i=0; i < N; i++) {
        int n; cin >> n;
        int gold, silver, bronze;
        cin >> gold >> silver >> bronze;

        vector<int> prize;
        prize.push_back(gold); prize.push_back(silver); prize.push_back(bronze);
        COUNTRY.push_back(make_pair(n, prize));
    }

    sort(COUNTRY.begin(), COUNTRY.end(), compare);
    
    int result = 1;
    if (!(COUNTRY[0].first == K)) {
        for (int i=1; i < N; i++) {
            result++;
            if (COUNTRY[i-1].second[0] == COUNTRY[i].second[0] && 
                COUNTRY[i-1].second[1] == COUNTRY[i].second[1] && 
                COUNTRY[i-1].second[2] == COUNTRY[i].second[2]) {
                result--;
            }
            else {
                result = i+1;
            }
            if (COUNTRY[i].first == K) break;
        }   
    }

    cout << result << '\n';

    return 0;
}
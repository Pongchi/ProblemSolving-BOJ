// URL : https://www.acmicpc.net/problem/11501

#include <iostream>
#include <climits>

using namespace std;

int chart[1'000'001];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int T; cin >> T;
    for (int t=0; t < T; t++) {
        int N; cin >> N;

        int MAX = 0;
        long result = 0;
        for (int i=0; i < N; i++) {
            cin >> chart[i];
        }

        for (int i=N-1; i >= 0; i--) {
            if (MAX < chart[i]) {
                MAX = chart[i];
            } else {
                result += MAX - chart[i];
            }
        }

        cout << result << '\n';
    }
    
    return 0;
}
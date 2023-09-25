// URL : 

#include <iostream>

using namespace std;

const int MAX_SIZE = 100'005;
int loc[MAX_SIZE];
bool road[MAX_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    for (int i=0; i < M; i++) cin >> loc[i];
    
    int start = 0;
    int end = N;
    while (start <= end) {
        bool d = true;
        int mid = (start + end) / 2;
        fill_n(road, N, false);

        for (int i=0; i < M; i++) {
            int location = loc[i];
            if (location - mid > 0) fill_n(road + location - mid, mid*2, true);
            else {
                fill_n(road, location, true);
                fill_n(road+location, mid, true);
            }
        }

        for (int i=0; i < N; i++) {
            if (!road[i]) {
                d = false;
                break;
            }
        }

        if (d) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    cout << start << '\n';
    
    return 0;
}
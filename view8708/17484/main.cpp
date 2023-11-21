// URL : https://www.acmicpc.net/problem/17484

#include <iostream>
#include <climits>

using namespace std;

int N, M = 6;
int MAP[6][6];
int directions[3] = {-1, 0, 1};

int recur(int row, int column, int before_direction);

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    cin >> N >> M;

    for (int i=0; i < N; i++) {
        for (int j=0; j < M; j++) {
            cin >> MAP[i][j];
        }
    }

    int result = INT_MAX;
    for (int i=0; i < N; i++) {
        int sum = recur(N-1, i, -1);
        result = min(result, sum);
    }

    cout << result << '\n';
    
    return 0;
}

int recur(int row, int column, int before_direction) {
    if (row == 0) return MAP[row][column];
    
    int result = INT_MAX;
    for (int i=0; i < 3; i++) {
        if (i == before_direction) continue;
        if (0 <= column+directions[i] && column+directions[i] < M) {
            int tmp = recur(row-1, column+directions[i], i);
            result = min(result, tmp);
        }
    }

    return result + MAP[row][column];
}
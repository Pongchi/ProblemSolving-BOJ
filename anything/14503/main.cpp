// URL : https://www.acmicpc.net/problem/14503

#include <iostream>
#include <stack>

const int MAX_SIZE = 55;
int MAP[MAX_SIZE][MAX_SIZE];

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    int r, c, d;
    cin >> r >> c >> d;

    for (int i=0; i < N; i++) {
        for (int j=0; j < M; j++) {
            cin >> MAP[i][j];
        }
    }

    int result = 0;
    int direction = 0;
    while (true) {
        if (MAP[r][c] == 0) {
            MAP[r][c] = 2;
            result++;
        }
        if ((r+dx[0] >= 0 && MAP[r+dx[0]][c] == 0) || // 북
            (c+dy[1] < M && MAP[r][c+dy[1]] == 0) ||  // 동
            (r+dx[2] < N && MAP[r+dx[2]][c] == 0) ||  // 남
            (c+dy[3] >= 0 && MAP[r][c+dy[3]] == 0)) { // 서

            d = (d+3) % 4;
            if (0 <= r+dx[d] && r+dx[d] < N &&
                0 <= c+dy[d] && c+dy[d] < M &&
                MAP[r+dx[d]][c+dy[d]] == 0) {

                r += dx[d];
                c += dy[d];
            }
        }
        else {
            if (0 <= r+dx[(d+2)%4] && r+dx[(d+2)%4] < N &&
                0 <= c+dy[(d+2)%4] && c+dy[(d+2)%4] < M &&
                MAP[r+dx[(d+2)%4]][c+dy[(d+2)%4]] != 1) {

                r += dx[(d+2)%4];
                c += dy[(d+2)%4];
            } else break;
        }
    }

    cout << result << '\n';
    
    return 0;
}
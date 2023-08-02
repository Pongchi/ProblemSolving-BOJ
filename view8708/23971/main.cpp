// URL : https://www.acmicpc.net/problem/23971

#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    
    int H, W, N, M, column, row;
    cin >> H >> W >> N >> M;

    column = H / (N+1);
    if (H % (N+1) != 0) column++;

    row = W / (M+1);
    if (W % (M+1) != 0) row++;

    cout << row * column << '\n';

    return 0;
}
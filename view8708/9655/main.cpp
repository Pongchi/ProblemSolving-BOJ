// URL : https://www.acmicpc.net/problem/9655

#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N;
    cin >> N;

    if (N % 2 == 1) {
        cout << "SK" << '\n';
    } else {
        cout << "CY" << '\n';
    }
    
    return 0;
}
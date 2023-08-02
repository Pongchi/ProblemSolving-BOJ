// URL : https://www.acmicpc.net/problem/5073

#include <iostream>
#include <algorithm>

int arr[3];

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    while (true) {
        cin >> arr[0] >> arr[1] >> arr[2];
        if (arr[0] == 0 && arr[1] == 0 && arr[1] == 0) break;

        sort(arr, arr+3);

        if (!(arr[2] < arr[0] + arr[1])) cout << "Invalid" << '\n';
        else if (arr[0] == arr[1] && arr[1] == arr[2]) cout << "Equilateral" << '\n';
        else if (arr[0] == arr[1] || arr[1] == arr[2]) cout << "Isosceles" << '\n';
        else cout << "Scalene" << '\n';
    }
    
    return 0;
}
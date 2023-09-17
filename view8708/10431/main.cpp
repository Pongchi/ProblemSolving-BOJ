// URL : https://www.acmicpc.net/problem/10431

#include <algorithm>
#include <any>
#include <iostream>

int arr[20];

using namespace std;

void popAndInsert(int first_index, int second_index);

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int P;
    cin >> P;

    for (int p=0; p < P; p++) {
        int T;
        cin >> T;
        for (int t=0; t < 20; t++) cin >> arr[t];

        int result = 0;
        for (int i=1; i < 20; i++) {
            if (arr[i-1] > arr[i]) {
                for (int j=0; j <= i; j++) {
                    if (arr[j] > arr[i]) {
                        result += i-j;
                        popAndInsert(j, i);
                        break;
                    }
                }
            }
        }
        cout << T << ' ' << result << '\n';
    }
    
    return 0;
}

void popAndInsert(int first_index, int second_index) {
    int tmp = arr[first_index];
    arr[first_index] = arr[second_index];
    arr[second_index] = tmp;

    if (first_index+1 == second_index) return;

    for (int i=second_index; i > first_index+1; i--) {
        tmp = arr[i];
        arr[i] = arr[i-1];
        arr[i-1] = tmp;
    }
}
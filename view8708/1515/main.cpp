// URL : https://www.acmicpc.net/problem/1515

#include <iostream>
#include <string>

using namespace std;

int count_number(int n, int target);
int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    string num;
    cin >> num;

    int lastest = 0;
    for (int i = 0; i < num.length(); i++) {
        lastest++;
        while (true) {
            int count = count_number(lastest, num[i]-'0');
            if (count != 0) {
                lastest += count - 1;
                break;
            }
            else lastest++;
        }
    }

    cout << lastest << '\n';
    
    return 0;
}

int count_number(int n, int target) {
    if (n == target) return 1;

    int result = 0;
    do {
        if (n%10 == target) result++;
        n /= 10;
    } while (n != 0) ;
    return result;
}
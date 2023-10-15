// URL : https://www.acmicpc.net/problem/1515

#include <iostream>
#include <string>

using namespace std;

int includeCount(int, int);
int number_length(int);

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    string num;
    cin >> num;

    int lastest = 1;
    for (int i = 0; i < num.length(); i++) {
        bool flag = false;
        while (!flag) {
            int length = (i+number_length(lastest) < num.length() ? number_length(lastest) : 1);
            int current_number = stoi(num.substr(i, length));
            if (current_number == lastest) {
                flag = true;
                i += length-1;
            }
            else {
                int count = includeCount(lastest, num[i]-'0');
                if (count != 0) {
                    i += count-1;
                    flag = true;
                }
            }
            lastest++;
        }
    }

    cout << lastest-1 << '\n';
    
    return 0;
}

int includeCount(int n, int target) {
    if (n == target) return 1;

    int result = 0;
    do {
        if (n%10 == target) result++;
        n /= 10;
    } while (n != 0);
    return result;
}

int number_length(int n) {
    int result = 0;
    while (n) {
        n /= 10;
        result++;
    }
    return result;
}
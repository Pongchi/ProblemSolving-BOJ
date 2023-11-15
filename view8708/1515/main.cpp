// URL : https://www.acmicpc.net/problem/1515

#include <algorithm>
#include <iostream>
#include <string>
#include <deque>

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
            int length = (number_length(i)+number_length(lastest)+1 <= num.length() ? number_length(lastest) : 1);
            int current_number = stoi(num.substr(i, length));
            int count = includeCount(lastest, current_number);

            if (count != 0) {
                i += count-1;
                flag = true;
            }
            lastest++;
        }
    }

    cout << lastest-1 << '\n';
    
    return 0;
}

int includeCount(int n, int target) {
    deque<int> deque1;
    deque<int> deque2;
    for (int i=0; n != 0 || target != 0; i++) {
        deque1.push_front(n%10);
        deque2.push_front(target%10);
        n /= 10;
        target /= 10;
    }

    int result = 0;
    int i=0;
    int j=0;
    while (i < deque1.size() && j < deque2.size()) {
        if (deque1[i] == deque2[j]) {
            result++; i++; j++;
        }
        else {
            i++;
        }
    }

    return result;
}

int number_length(int n) {
    return to_string(n).size();
}
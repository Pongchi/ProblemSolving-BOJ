// URL : https://www.acmicpc.net/problem/1244

#include <iostream>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

const int MAX_SIZE = 105;
bool SWITCH[MAX_SIZE];
pii students[MAX_SIZE];


int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N; cin >> N;
    for (int i=1; i <= N; i++) {
		int n; cin >> n;
		SWITCH[i] = (n == 1 ? true : false);
	}
	
	int S; cin >> S;
	for (int i=0; i < S; i++) {
		int gender, switchN;
		cin >> gender >> switchN;
		students[i] = make_pair(gender, switchN);
	}
	
	for (int i=0; i < S; i++) {
		pii student = students[i];
		if (student.first == 1) {
			for (int n=student.second; n <= N; n += n) SWITCH[n] = !SWITCH[n];
		}
		else {
			SWITCH[student.second] = !SWITCH[student.second];
			for (int n=1; !(student.second-n == 0 || student.second+n == N+1); n++) {
				if (SWITCH[student.second-n] == SWITCH[student.second+n]) {
					SWITCH[student.second-n] = !SWITCH[student.second-n];
					SWITCH[student.second+n] = !SWITCH[student.second+n];
				}	
				else break;
			}
		}
	}
	
	for (int i=0; i < N/8; i++) {
		for (int j=0; j < 8; j++) {
			cout << SWITCH[8*i + j+1] << ' ';
		}
		cout << '\n';
	}
    
    return 0;
}
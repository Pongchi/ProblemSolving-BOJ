// URL : https://www.acmicpc.net/problem/20125

#include <iostream>
#include <string>

using namespace std;

const int MAX_SIZE = 100'5;
string cookie[MAX_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N;
    cin >> N;

    for (int i=0; i < N; i++) {
        cin >> cookie[i];
    }

    int heartX = -1, heartY = -1, leftArm = -1, rightArm =-1, body = -1, leftLeg = -1, rightLeg = -1;
    // 머리를 기반으로 심장 찾기
    for (int i=0; i < N; i++) {
        if (heartX == -1 && heartY == -1) {
            for (int j=0; j < N; j++) {
                if (cookie[i][j] == '*') {
                    heartX = i+1;
                    heartY = j;
                    break;
                }
            }
        }
        else break;
    }

    // 왼팔
    for (int i=heartY; 0 <= i; i--) {
        if (cookie[heartX][i] == '_') {
            leftArm = heartY - i - 1;
            break;
        }
    }
    if (leftArm == -1) leftArm = heartY;

    // 오른팔
    for (int i=heartY; i < N; i++) {
        if (cookie[heartX][i] == '_') {
            rightArm = i - heartY - 1;
            break;
        }
    }
    if (rightArm == -1) rightArm = N - heartY - 1;

    // 몸통
    for (int i=heartX; i < N; i++) {
        if (cookie[i][heartY] == '_') {
            body = i - heartX - 1;
            break;
        }
    }

    // 왼다리
    for (int i=heartX+body+1; i < N; i++) {
        if (cookie[i][heartY-1] == '_') {
            leftLeg = i - heartX - body - 1;
            break;
        }
    }
    if (leftLeg == -1) leftLeg = N - heartX - body - 1;

    // 오른다리
    for (int i=heartX+body+1; i < N; i++) {
        if (cookie[i][heartY+1] == '_') {
            rightLeg = i - heartX - body - 1;
            break;
        }
    }
    if (rightLeg == -1) rightLeg = N - heartX - body - 1;

    cout << heartX+1 << ' ' << heartY+1 << '\n';
    cout << leftArm << ' ' << rightArm << ' ' << body << ' ' << leftLeg << ' ' << rightLeg << '\n';
    
    return 0;
}
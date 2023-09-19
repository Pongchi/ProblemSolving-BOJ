// URL : https://www.acmicpc.net/problem/4659

#include <iostream>
#include <string>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    string vowel = "aeiou";
    string acceptableContinous = "eo";
    
    while (true) {
        string password; cin >> password;
        if (password == "end") break;

        bool isContainVowel = (vowel.find(password[0]) != string::npos);
        int sequence = 1;
        int isPrevVowel = isContainVowel;
        bool result = isContainVowel;

        for (int i=1; i < password.size(); i++) {
            if (vowel.find(password[i]) != string::npos) {
                result = true;
                isContainVowel = true;
                if (isPrevVowel) sequence++;
                else sequence = 1;
            }
            else {
                if (!isPrevVowel) sequence++;
                else sequence = 1;
            }

            isPrevVowel = vowel.find(password[i]) != string::npos;
            if (sequence >= 3 || (password[i] == password[i-1] && acceptableContinous.find(password[i]) == string::npos)) {
                result = false;
                break;
            }
        }

        cout << '<' << password << "> is " << ((result ? "" : "not ")) << "acceptable.\n";
    }
    return 0;
}
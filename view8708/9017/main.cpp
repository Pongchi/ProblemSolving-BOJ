// URL : https://www.acmicpc.net/problem/9017

#include <iostream>
#include<vector>
#include <map>

using namespace std;

const int MAX_PLAYER_SIZE = 1'005;
int record[MAX_PLAYER_SIZE];

const int MAX_TEAM_SIZE = 205;
int player_count[MAX_TEAM_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int T; cin >> T;
	for (int t=0; t < T; t++) {
		int N; cin >> N;

		map<int, vector<int>> team;
		map<int, int> scores;

		fill_n(record, N, 0);
		fill_n(player_count, MAX_TEAM_SIZE, 0);

		for (int i=0; i < N; i++) {
			cin >> record[i];
			player_count[record[i]]++;
		}
		
		int rank = 1;
		for (int i=0; i < N; i++) {
			if (player_count[ record[i] ] == 6) {
				team[ record[i] ].push_back(rank++);
				if (team[record[i]].size() <= 4) {
					if (scores.find(record[i]) == scores.end()) scores[record[i]] = 0;
					scores[record[i]] += rank-1;
				}
			}
		}

		int result = record[0];
		for (auto score : scores) {
			if ((scores[result] > score.second) || (scores[result] == score.second && team[result][4] > team[score.first][4]))
				result = score.first;
		}

		cout << result << '\n';
	}
    
    return 0;
}
// URL : https://www.acmicpc.net/problem/9017

#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

const int MAX_PLAYER_SIZE = 1'005;
int record[MAX_PLAYER_SIZE];

const int MAX_TEAM_SIZE = 205;
int scores[MAX_TEAM_SIZE];
vector<int> teams[MAX_TEAM_SIZE];
int teams_count[MAX_TEAM_SIZE];
int cutline[MAX_TEAM_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int T; cin >> T;
	for (int t=0; t < T; t++) {
		int N; cin >> N;
		int max_team = 0;

		fill_n(record, N, 0);
		fill_n(teams, MAX_TEAM_SIZE, vector<int>());
		fill_n(teams_count, MAX_TEAM_SIZE, 0);
		fill_n(scores, MAX_TEAM_SIZE, 0);
		fill_n(cutline, MAX_TEAM_SIZE, 0);

		for (int i=0; i < N; i++) {
			cin >> record[i];
			teams_count[record[i]]++;

			if (max_team < record[i]) max_team = record[i];
		}
		
		int rank = 1;
		for (int i=0; i < N; i++) {
			if (teams_count[ record[i] ] == 6) {
				teams[ record[i] ].push_back(rank);

				if (cutline[record[i]] < 4) {
					scores[record[i]] += rank;
					cutline[record[i]]++;
				}
				rank++;
			}
		}
		
		int result = 1;
		for (int i=1; i <= max_team; i++) {
			if (scores[i] == 0) continue;
			if ((scores[result] > scores[i]) || (scores[result] == scores[i] && teams[result][4] > teams[i][4]))
				result = i;
		}

		cout << result << '\n';
	}
    
    return 0;
}
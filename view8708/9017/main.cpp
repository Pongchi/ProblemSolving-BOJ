// URL : https://www.acmicpc.net/problem/9017

#include <iostream>

using namespace std;

const int MAX_SIZE = 100'5;
int record[MAX_SIZE];

const int TEAM_MAX_SIZE = 205;
int teams[TEAM_MAX_SIZE];
int scores[TEAM_MAX_SIZE];
int cutline[TEAM_MAX_SIZE];

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	int T; cin >> T;
	for (int t=0; t < T; t++) {
		int N; cin >> N;
		int max_team = 0;
		
		fill_n(teams, (N+1) * sizeof(int), 0);
		fill_n(scores, (N+1) * sizeof(int), 0);
		fill_n(cutline, (N+1) * sizeof(int), 0);
		for (int i=0; i < N; i++) {
			cin >> record[i];
			teams[ record[i] ]++;
			
			if (max_team < record[i]) max_team = record[i];
		}
		
		int rank = 1;
		for (int i=0; i < N; i++) {
			if (teams[ record[i] ] == 6 && cutline[ record[i] ] < 4) {
				scores[ record[i] ] += rank;
				cutline[ record[i] ]++;
				rank++;
			}
		}
		
		int result = 1;
		for (int i=1; i <= max_team; i++) {
			if (scores[result] > scores[i]) result = i;
			else if (scores[result] == scores[i]) {
				if (record[result])
			}
		}
	}
    
    return 0;
}
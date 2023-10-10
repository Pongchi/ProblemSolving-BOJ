// URL : https://www.acmicpc.net/problem/21921

#include <algorithm>
#include <iostream>
#include <numeric>

const int MAX_SIZE = 250'005;
int graph[MAX_SIZE];
int prefix[MAX_SIZE];

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int N, X;
    cin >> N >> X;

    for (int i=0; i < N; i++) cin >> graph[i];
    prefix[X-1] = accumulate(graph, graph+X-1, graph[X-1]);

    for (int i=X; i < N; i++) {
        prefix[i] = graph[i] + prefix[i-1] - graph[i-X];
    }

    int result = *max_element(prefix, prefix + N);
    if (result != 0) {
        cout << result << '\n';
        cout << count(prefix, prefix + N, result) << '\n';
    }
    else cout << "SAD" << '\n';
    
    return 0;
}
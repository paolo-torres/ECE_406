#include <iostream>
#include <vector>

using namespace std;

const int d(const int k, const int n) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));
    int moves = 0;
    while (dp[moves][k] < n) {
        moves++;
        for (int egg = 1; egg <= k; egg++)
            dp[moves][egg] = dp[moves - 1][egg - 1] + dp[moves - 1][egg] + 1;
    }
    return moves;
}

int main() {
    const int eggs = 100;
    const int floors = 10000000;
	const int result = d(eggs, floors);

    cout << result << endl;

    return 0;
}

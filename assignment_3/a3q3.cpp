#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int editDistance(const string x, const string y) {
    if (x.empty() && y.empty()) {
        return 0;
    }
    if (x.empty() || y.empty()) {
        return 1;
    }
    int n = x.size();
    int m = y.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; i++) {
        dp[i][0] = i;
    }
    for (int j = 1; j <= m; j++) {
        dp[0][j] = j;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (x[i-1] == y[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;
            }
        }
    }
    return dp[n][m];
}

int main() {
    const string x = "SNOWY";
    const string y = "SUNNY";
    cout << editDistance(x, y) << endl;

    return 0;
}

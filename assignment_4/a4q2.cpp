#include <iostream>
#include <vector>

using namespace std;

void dfs(int v, vector<bool> visited, vector<vector<int>> adj) {
    visited[v] = true;
    for (auto it = adj[v].begin(); it != adj[v].end(); ++it) {
        if (!visited[*it]) {
            dfs(*it, visited, adj);
        }
    }
}

int countConnectedComponents(vector<bool> visited, vector<vector<int>> adj) {
    const int n = visited.size();
    int connectedComponents = 0;

    for (int i = 0; i < n; i++) {
        visited[i] = false;
    }
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, visited, adj);
            connectedComponents++;
        }
    }

    return connectedComponents;
}

bool hasKConnectedComponents(const int connectedComponents, const int k) {
    if (connectedComponents == k) {
        return true;
    }
    return false;
}

int main() {
    const int n = 10;
    const int m = 10;

    vector<bool> visited(n, 0);
    vector<vector<int>> adj(n, vector<int>(m, 0));

    const int connectedComponents = countConnectedComponents(visited, adj);

    const int k = 3;
    const bool result = hasKConnectedComponents(connectedComponents, k);

    return 0;
}

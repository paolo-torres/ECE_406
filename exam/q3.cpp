#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> performKruskal(vector<vector<int>>& G) {
    vector<int> T(10, 0);
    // Finds a minimum spanning tree for graph G
    return T;
}

void augmentMST(vector<vector<int>>& H, vector<int>& U, int& weightT) {
    for (int i = 0; i < H.size(); i++) {
        for (int j = 0; j < H[i].size(); j++) {
            for (int k = 0; k < U.size(); k++) {
                if (H[i][j] == U[k]) {
                    H[i][j]++;
                    weightT += U[k];
                    U[k] = 0;
                }
            }
        }
    }
}

bool hasUniqueMST(vector<vector<int>>& G, vector<int>& T) {
    vector<vector<int>> H = G;
    vector<int> U = T;
    int weightT = 0;

    augmentGraphMST(H, U, weightT);

    vector<int> primeT = performKruskal(H);
    if (T == primeT) {
        return true;
    }

    int weightPrimeT = 0;
    for (int i = 0; i < primeT.size(); i++) {
        weightPrimeT += primeT[i] - 1;
    }
    if (weightT == weightPrimeT) {
        return false;
    }

    return true;
}

int main() {
    vector<vector<int>> G(10, vector<int>(10, 0));
    vector<int> T(10, 0);

    bool result = hasUniqueMST(G, T);
    
    cout << result << endl;

    return 0;
}

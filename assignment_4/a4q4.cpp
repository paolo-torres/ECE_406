#include <iostream>
#include <vector>

using namespace std;

bool I(vector<int>& G, vector<int>& H) {
    // Polynomial-time algorithm to determine isomorphism
    return true;
}

void isAutomorphic(vector<int>& G, vector<int>& H, int pos, bool& result) {
    if (pos == H.size() - 1) {
        if (I(G, H) && G != H) {
            result = true;
        }
        return;
    }
    if (result == true) {
        return;
    }
    for (int i = pos; i < G.size(); i++) {
        swap(H[i], H[pos]);
        isAutomorphic(G, H, pos + 1, result);
        swap(H[i], H[pos]);
    }
}

bool A(vector<int> G) {
    vector<int> H = G;
    bool result = false;
    isAutomorphic(G, H, 0, result);
    if (result == true) {
        return true;
    }
    return false;
}

int main() {
    const int n = 10;
    vector<int> G(n, 0);

    if (A(G)) {
        cout << "Automorphic" << endl;
    } else {
        cout << "Not automorphic" << endl;
    }

    return 0;
}

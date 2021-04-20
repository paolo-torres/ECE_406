#include <iostream>

using namespace std;

int sqSum(int p, int q) {
    if (p == q) {
        return p * p;
    } else {
        int m = (p + q) / 2;
        int l = sqSum(p, m);
        int r = sqSum(m + 1, q);
        return l + r;
    }
}

int getSqSum(int n) {
    return sqSum(1, n);
}

int main() {
    for (int n = 1; n < 50; n++) {
        cout << "n: " << n << '\t' << "Value: " << getSqSum(n) << endl;
    }

    return 0;
}

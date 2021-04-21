#include <iostream>
#include <vector>

using namespace std;

const int fairCoinToss() {
    int coinToss = rand() % 2;
    return coinToss;
}

const int getRandInt(const int& a, const int& b) {
    vector<int> v;

    for (int i = a; i <= b; i++) {
        v.push_back(i);
    }

    auto it = v.begin();
    while (v.size() > 1) {
        if (fairCoinToss()) {
            it++;
        } else {
            v.erase(it);
        }
        if (it == v.end()) {
            it = v.begin();
        }
    }

    const int i = v[0];
    return i;
}

int main() {
    srand(time(NULL));

    const int a = 1;
    const int b = 5;

    for (int i = 0; i < 50; i++) {
        cout << getRandInt(a, b) << endl;
    }

    return 0;
}

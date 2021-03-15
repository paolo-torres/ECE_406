#include <iostream>
#include <limits>
#include <vector>

using namespace std;

const int numMinStops(const vector<int> stops) {
    const int numStops = stops.size();
    vector<int> m(numStops + 1, 0);
    for (int j = 0; j < numStops; j++) {
        for (int i = j; i >= 0; i--) {
            // if (stops[i] --> stops[j]) {
            //     m[j + 1] = m[j];
            // } else if (stops[i] -/> stops[j]) {
            //     m[j + 1] = 1 + m[j];
            // }
        }
    }
    if (m.back() != 0) {
        return m.back();
    }
    return numeric_limits<int>::max();
}

int main() {
    const vector<int> stops = {10, 20, 30, 40, 50};
    cout << numMinStops(stops) << endl;

    return 0;
}

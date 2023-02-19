#include <bits/stdc++.h>
using namespace std;

int n, m;
int v[200001];
vector<int>w[200001];

void addElement(int x) {
    int st = 0, dr = m, mid, last = -1;
    while (st <= dr) {
        mid = (st + dr) / 2;
        if (w[mid].back() < x) {
            last = mid;
            dr = mid - 1;
        } else st = mid + 1;
    }
    if (last == -1) {
        ++m;
        w[m].push_back(x);
    } else {
        w[last].push_back(x);
    }
}

int main() {

    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> v[i];
    w[0].push_back(v[1]);
    for (int i = 2; i <= n; i++) {
        addElement(v[i]);
    }
    for (int i = 0; i <= m; i++) {
        for (auto element: w[i]) {
            cout << element << ' ';
        }
        cout << '\n';
    }
    return 0;
}
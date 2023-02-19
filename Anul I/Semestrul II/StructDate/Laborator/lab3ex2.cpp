#include <bits/stdc++.h>
using namespace std;

int n, m;
int v[200001];

bool check(int x) {
    int currentValue = 0;
    for (int i = 1; i <= n; i++) {
        if (v[i] <= currentValue) {
            currentValue++;
        } else if (x > 0) {
            currentValue++;
            x--;
        }
    }
    if (currentValue >= m)
        return true;
    else return false;
}
int solve() {
    int st = 0, dr = n, mid, last = n;
    while (st <= dr) {
        mid = (st + dr) / 2;
        if (check(mid)) {
            last = mid;
            dr = mid - 1;
        } else st = mid + 1;
    }
    return last;
}
int main() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        cin >> v[i];
    int s = solve();
    cout << s;
    return 0;
}
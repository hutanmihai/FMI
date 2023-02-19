#include <bits/stdc++.h>

using namespace std;
ifstream in("progr.in");
ofstream out("progr.out");
int v[2005];
int dp[2005];
int test, n;

int main() {
    in >> test;
    while (test--) {
        in >> n;
        int sol = 0;
        for (int i = 1; i <= n; ++i) {
            in >> v[i];
            dp[i] = 0;
        }
        sort(v + 1, v + n + 1);
        for (int i = 1; i < n; ++i) {
            int ind = i;
            for (int j = i + 1; j <= n; ++j)
                if ((v[i] + v[j]) % 2 == 0) {
                    int med = (v[i] + v[j]) / 2;
                    while (v[ind] < med and ind < j)
                        ++ind;
                    if (v[ind] == med)
                        dp[ind]++;
                }
            sol += n - i - dp[i];
        }
        out << sol << '\n';
    }
    return 0;
}
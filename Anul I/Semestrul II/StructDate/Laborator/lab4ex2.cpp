#include <bits/stdc++.h>
using namespace std;

ifstream in("secv5.in");
ofstream out("secv5.out");

long long a[1050005];
int n, l, u;
unordered_map<long long, int> M;

long long Secv(int x)
{
    int i, nrdist = 0, p = 1;
    long long cnt = 0;
    for (i = 1; i <= n; i++)
    {
        M[a[i]]++;
        if (M[a[i]] == 1) nrdist++;
        while (nrdist > x)
        {
            M[a[p]]--;
            if (M[a[p]] == 0) nrdist--;
            p++;
        }
        cnt += (i - p + 1);
    }
    return cnt;
}
int main()
{
    int i;
    long long x, y;
    in >> n >> l >> u;
    for (i = 1; i <= n; i++)
        in >> a[i];
    x = Secv(u);
    M.clear();
    y = Secv(l - 1);
    out << x - y << "\n";
    in.close();
    out.close();
    return 0;
}
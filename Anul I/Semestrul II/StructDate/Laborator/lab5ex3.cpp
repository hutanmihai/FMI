#include <bits/stdc++.h>

using namespace std;

ifstream f("concurs.in");
ofstream g("concurs.out");

vector<int> v[100100];
vector<int> euler, ad;
int n, nr, m, p[100100];

void parcurgere_euler(int rad, int adancime) {
    int i;
    nr++;
    if (p[rad] == 0)p[rad] = nr;
    ad.push_back(adancime);
    euler.push_back(rad);
    for (i = 0; i < v[rad].size(); i++) {
        parcurgere_euler(v[rad][i], adancime + 1);
        nr++;
        if (p[rad] == 0)p[rad] = nr;
        ad.push_back(adancime);
        euler.push_back(rad);
    }
}

int i, j, x, A, B, N, ad1, rad, y, ad2, poz1, poz2, maxim, val, cp1, cp2, fv1[100100], fv[100100], D[500100][22];

int main() {
    f >> n >> m;
    for (i = 1; i <= n; i++)f >> fv[i];
    for (i = 2; i <= n; i++) {
        f >> x >> y;
        fv1[y] = 1;
        v[x].push_back(y);
    }
    for (i = 1; i <= n; i++)
        if (fv1[i] == 0) {
            rad = i;
            break;
        }
    parcurgere_euler(rad, 0);
    N = euler.size();
    for (i = 1; i <= N; i++)
        D[i][0] = euler[i - 1];

    for (j = 1; (1 << j) <= N; j++) {
        for (i = 1; i + (1 << j) - 1 <= N; i++) {

            ad1 = ad[p[D[i][j - 1]] - 1];
            ad2 = ad[p[D[i + (1 << (j - 1))][j - 1]] - 1];

            if (ad1 < ad2)D[i][j] = D[i][j - 1];
            else D[i][j] = D[i + (1 << (j - 1))][j - 1];
        }
    }

    for (i = 1; i <= m; i++) {
        f >> A >> B;
        cp1 = A;
        cp2 = B;
        A = p[A];
        B = p[B];
        if (A > B)swap(A, B);
        x = log2(B - A + 1);
        ad1 = ad[p[D[A][x]] - 1];
        ad2 = ad[p[D[B - (1 << x) + 1][x]] - 1];
        if (ad1 < ad2)val = fv[D[A][x]];
        else val = fv[D[B - (1 << x) + 1][x]];
        if (val > maxim) {
            maxim = val;
            poz1 = cp1;
            poz2 = cp2;
        } else if (val == maxim) {
            if (cp1 < poz1) {
                poz1 = cp1;
                poz2 = cp2;
            } else if (cp1 == poz1) {
                if (cp2 < poz2)poz2 = cp2;
            }
        }

    }
    g << maxim << " " << poz1 << " " << poz2;
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

ifstream in("algsort.in");
ofstream out("algsort.out");

void QuickSortcresc(vector<int> &v, int st, int dr) {
    if (st < dr) {
        int mij = (st + dr) / 2;
        int aux = v[st];
        v[st] = v[mij];
        v[mij] = aux;
        int i = st, j = dr, d = 0;
        while (i < j) {
            if (v[i] > v[j]) {
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
                d = 1 - d;
            }
            i += d;
            j -= 1 - d;
        }
        QuickSortcresc(v, st, i);
        QuickSortcresc(v, i + 1, dr);
    }
}

vector<int> v;

int main() {
    int n, x;
    in >> n;
    for (int i = 0; i < n; ++i) {
        in >> x;
        v.push_back(x);
    }
    QuickSortcresc(v, 0, int(v.size()) - 1);

    for (int i = 0; i < int(v.size()); ++i) {
        out << v[i] << " ";
    }
    in.close();
    out.close();
    return 0;
}

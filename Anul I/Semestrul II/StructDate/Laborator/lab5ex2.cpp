#include <bits/stdc++.h>

using namespace std;

ifstream in("rmq.in");
ofstream out("rmq.out");

int n, m, x, y;
int matrix[100001][20];
vector<int> v;

int main() {
    in >> n >> m;
    v.resize(n);
    for (auto &element: v) {
        in >> element;
    }
    for (int i = 0; i < n; ++i) {
        matrix[i][0] = i;
    }
    for (int j = 1; (1 << j) <= n; ++j) {
        for (int i = 0; (i + (1 << j) - 1) < n; ++i) {
            if (v[matrix[i][j - 1]] < v[matrix[i + (1 << (j - 1))][j - 1]]) {
                matrix[i][j] = matrix[i][j - 1];
            } else {
                matrix[i][j] = matrix[i + (1 << (j - 1))][j - 1];
            }
        }
    }
    for (int i = 0; i < m; ++i) {
        in >> x >> y;
        if (x > y) swap(x, y);
        --x;
        --y;
        int j = (int) log2(y - x + 1);
        if (v[matrix[x][j]] <= v[matrix[y - (1 << j) + 1][j]]) {
            out << v[matrix[x][j]] << '\n';
        } else {
            out << v[matrix[y - (1 << j) + 1][j]] << '\n';
        }
    }
    return 0;
}
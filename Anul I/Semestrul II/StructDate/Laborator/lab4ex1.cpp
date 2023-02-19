#include <bits/stdc++.h>
using namespace std;

ifstream in("pariuri.in");
ofstream out("pariuri.out");

int main(){

    unordered_map<int, int> D;
    int N, M, timp, bani;
    in >> N;
    for (int i = 0; i < N; ++i) {
        in >> M;
        for (int j = 0; j < M; ++j) {
            in >> timp >> bani;
            D[timp] += bani;
        }
    }
    out << D.size() << '\n';
    for (auto pair : D) {
        out << pair.first << ' ' << pair.second  << ' ';
    }
    return 0;
}
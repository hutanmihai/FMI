#include <bits/stdc++.h>

using namespace std;

ifstream in("radixsort.in");
ofstream out("radixsort.out");

int n, a, b, c, v[10000002], aux[10000002];

int freq[261], poz[261];

int main() {
    in >> n >> a >> b >> c;

    v[1] = b;
    for(int i = 2; i <= n; i++) {
        v[i] = 1LL * (1LL * v[i - 1] * a + b) % c;
    }
    for(int i = 0, mask = 255; i < 32; i += 8, mask <<= 8) {
        for(int j = 1; j <= n; j++) {
            int cifra = (v[j] & mask) >> i;
            freq[cifra]++;
        }
        for(int j = 1; j < 256; j++)
            freq[j] += freq[j - 1];
        for(int j = 1; j <= n; j++) {
            int cifra = (v[j] & mask) >> i;
            poz[cifra]++;
            int newpoz = poz[cifra];
            if(cifra > 0) newpoz += freq[cifra - 1];
            aux[newpoz] = v[j];
        }
        for(int j = 1; j <= n; j++)
            v[j] = aux[j];
        for(int j = 0; j < 256; j++) {
            freq[j] = 0;
            poz[j] = 0;
        }
    }
    for(int i = 1; i <= n; i += 10)
        out << v[i] << " ";
}
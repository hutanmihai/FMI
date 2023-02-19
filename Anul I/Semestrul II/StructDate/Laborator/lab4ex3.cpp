#include <bits/stdc++.h>
using namespace std;

ifstream in("muzica.in");
ofstream out("muzica.out");

unordered_set <long long> melodii(100000);

int main()
{
    long long nrVasile;
    in >> nrVasile;
    long long nrDJ;
    in >> nrDJ;
    long long A, B, C, D, E;
    in >> A >> B >> C >> D >> E;
    melodii.clear();

    for (int i = 1; i <= nrVasile; i++)
    {
        long long melodieVasile;
        in >> melodieVasile;
        melodii.insert(melodieVasile);
    }

    long long comune = 0;
    if (melodii.find(A) != melodii.end())
    {
        comune++;
        melodii.erase(A);
    }

    if (melodii.find(B) != melodii.end())
    {
        comune++;
        melodii.erase(B);
    }

    long long curent, ultima = B, penultima = A;
    for (int i = 3; i <= nrDJ; i++)
    {
        curent =  (C * ultima + D * penultima) % E;
        if (melodii.find(curent) != melodii.end())
        {
            comune++;
            melodii.erase(curent);
        }

        penultima = ultima;
        ultima = curent;
    }
    out << comune;
}
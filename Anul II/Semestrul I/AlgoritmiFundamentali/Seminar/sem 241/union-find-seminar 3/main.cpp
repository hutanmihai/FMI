#include <iostream>
#include <bits/stdc++.h>


using namespace std;

ifstream in(".in");
ifstream in2("interogari.in");

const int NMAX = 1000;
int n, k;
int Heights[NMAX], Fathers[NMAX], UnionSize[NMAX];

void Init(int x)
{
    Fathers[x] = 0;
    Heights[x] = 0;
    UnionSize[x] = 1;
}

//Find fara compresie de cale
int Find(int x)
{
    while(Fathers[x] != 0)
        x = Fathers[x];
    return x;
}
/*
//cu compresie de cale
int Find(int x)
{
    if (Fathers[x]==0)
        return x;
    Fathers[x]=Find(Fathers[x]); //fathers[x] devine radacina arborelui, returnata de apelul recursiv Fathers[x]
    return Fathers[x];
}

//reuniune ponderata dupa inaltime - by rank
int Union(int x, int y)
{
    int RootX = Find(x), RootY = Find(y);
    if(Heights[RootX] < Heights[RootY])
    {
        Fathers[RootX] = RootY;
        UnionSize[RootY] += UnionSize[RootX];
        return UnionSize[RootY];
    }
    else
    {
        if(Heights[RootX] > Heights[RootY])
            Fathers[RootY] = RootX;
        else
            Fathers[RootY] = RootX, Heights[RootX]++;
        UnionSize[RootX] += UnionSize[RootY];
        return UnionSize[RootX];
    }
}*/
//reuniune ponderata dupa dimensiune(nr de varfuri) - by size
//putem renunta la height si sa facem reuniunea in functie de unionsize
int Union(int x, int y)
{
    int RootX = Find(x), RootY = Find(y);
  
    if(UnionSize[RootX] < UnionSize[RootY])
    {
        Fathers[RootX] = RootY;
        UnionSize[RootY] += UnionSize[RootX];
        return UnionSize[RootY];
    }
    else
    {
        if(UnionSize[RootX] > UnionSize[RootY])
            Fathers[RootY] = RootX;
        else
            Fathers[RootY] = RootX;
        UnionSize[RootX] += UnionSize[RootY];
        return UnionSize[RootX];
    }
}




int main()
{
    int length, x, y, dimMax = 1;
    in >> n >> k;
    for(int i = 1; i <= n; i++)
        Init(i);
    for(int i = 1; i <= k; i++)
    {
        in >> length;
        in >> x;
        for(int j = 2; j <= length; j++)
         {

            in >> y, dimMax = max(Union(x, y), dimMax);
             
         }
    }
    for(int i = 1; i <= n; i++)
        cout << Fathers[i] << ' ';
    cout << '\n';
    for(int i = 1; i <= n; i++)
        cout << UnionSize[i] << ' ';
    cout << '\n';
    while(in2 >> x >> y)
    {
        if(Find(x) != Find(y))
            dimMax = max(Union(x, y), dimMax), k--;
        printf("Dupa muchia %d %d, nr componente este %d\n", x, y, k);
        for(int i = 1; i <= n; i++)
            cout << Fathers[i] << ' ';
        cout << '\n';
        for(int i = 1; i <= n; i++)
            cout << UnionSize[i] << ' ';
        cout << '\n';
        printf("Componenta maxima are %d elemente\n", dimMax);
    }
    return 0;
}

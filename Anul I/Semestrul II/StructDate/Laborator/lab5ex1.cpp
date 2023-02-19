#include <bits/stdc++.h>
using namespace std;

ifstream in("heapuri.in");
ofstream out("heapuri.out");

int pozitie[200001];

struct per {
    int val;
    int poz;
};

per heap[200001];
int n;
int nrinserari;

void up(int nod)
{
    if(nod == 1)
        return;
    int tata = nod / 2;
    if(heap[nod].val < heap[tata].val)
    {
        pozitie[heap[nod].poz] = tata;
        pozitie[heap[tata].poz] = nod;
        swap(heap[nod], heap[tata]);
        up(tata);
    }
}

void down(int nod){
    if(nod * 2 > n)
        return;
    int fiumin = nod * 2;
    if(nod * 2 + 1 <= n && heap[fiumin].val > heap[nod * 2 + 1].val)
        fiumin = nod * 2 + 1;
    if(heap[nod].val > heap[fiumin].val){
        pozitie[heap[nod].poz] = fiumin;
        pozitie[heap[fiumin].poz] = nod;
        swap(heap[nod], heap[fiumin]);
        down(fiumin);
    }
}

void inserare(int val){
    n++;
    heap[n] = {val, nrinserari};
    pozitie[nrinserari] = n;
    up(n);
}


void stergere(int x){
    int nod = pozitie[x];
    swap(pozitie[heap[nod].poz], pozitie[heap[n].poz]);
    swap(heap[nod], heap[n]);
    n--;
    up(nod);
    down(nod);
}

int main(){
    int m;
    in >> m;
    for(int i = 1; i <= m; i++){
        int op, x;
        in >> op;
        if(op == 1 || op == 2)
            in >> x;
        if(op == 1)
        {
            nrinserari++;
            inserare(x);
        }
        else if(op == 2)
            stergere(x);
        else
            out << heap[1].val << "\n";
    }
    return 0;
}
#include <iostream>

using namespace std;
int k;
int n = 13;

int cautareBinara(int v[], int st, int dr) {
    if (st > dr)
        return -1;
    if (st==dr)
        return st;
    else {
        int mij = (st + dr) / 2;
        if (v[mij]<v[n])
            return cautareBinara(v, st, mij - 1);
        else
            return cautareBinara(v, mij + 1, dr);
    }
}

int searchNumber(int v[], int num) {
    int x = cautareBinara(v,num,0,k);
    if(x==-1){
        return cautareBinara(v,num,k,n+1);
    }
}

int main() {
    int v[] = {9, 12, 45, 123, 346, 850, 900, 1000, 1240, 3, 6, 7, 8};
    k = cautareBinara(v,0,n)

    cout << searchNumber(v, 6)<<endl;
    cout << searchNumber(v, 1240)<<endl;
    cout << searchNumber(v, 12)<<endl;
    cout << searchNumber(v, 3)<<endl;
    cout << searchNumber(v, 8)<<endl;
    cout << searchNumber(v, 45)<<endl;
    return 0;
}

#include <iostream>
using namespace std;

void QuickSortcresc(long long v[], int st, long long dr)
{
    if(st < dr)
    {
        int m = (st + dr) / 2;
        int aux = v[st];
        v[st] = v[m];
        v[m] = aux;
        int i = st , j = dr, d = 0;
        while(i < j)
        {
            if(v[i] > v[j])
            {
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
                d = 1 - d;
            }
            i += d;
            j -= 1 - d;
        }
        QuickSortcresc(v, st , i - 1);
        QuickSortcresc(v, i + 1 , dr);
    }
}

void QuickSortdescr(long long v[], int st, long long dr)
{
    if(st < dr)
    {
        int m = (st + dr) / 2;
        int aux = v[st];
        v[st] = v[m];
        v[m] = aux;
        int i = st , j = dr, d = 0;
        while(i < j)
        {
            if(v[i] < v[j])
            {
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
                d = 1 - d;
            }
            i += d;
            j -= 1 - d;
        }
        QuickSortdescr(v, st , i - 1);
        QuickSortdescr(v, i + 1 , dr);
    }
}

long long v[1000001];

int main(){
    long long n,mij,aux,mod;
    cin>>n>>mod;
    if(n%2==0){
        mij=n/2;
    }
    else{
        mij=(n+1)/2;
    }
    for (int i = 1; i <= n; ++i) {
        v[i]=i*i%mod;
    }
    cout<<endl;
    QuickSortcresc(v,1,mij);

    for (int i = 1; i <= mij ; ++i) {
        cout<<v[i]<<" ";
    }

    QuickSortdescr(v,mij,n);

    for (int i = mij+1; i <= n ; ++i) {
        cout<<v[i]<<" ";
    }
    return 0;

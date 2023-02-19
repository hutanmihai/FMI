#include <iostream>
using namespace std;

int main(){

    int n,mij,aux;
    cin>>n;
    int v[10001];
    if(n%2==0){
        mij=n/2;
    }
    else{
        mij=(n+1)/2;
    }
    for (int i = 1; i <= n; ++i) {
        v[i]=i*i%30;
    }

    for (int i = 1; i <= n ; ++i) {
        cout<<v[i]<<" ";
    }

    cout<<endl;

    for (int i = 1; i <mij ; ++i) {
        for (int j = i+1; j <= mij ; ++j) {
            if(v[i]>v[j]){
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }

    for (int i = mij+1; i <n ; ++i) {
        for (int j = i+1; j <= n ; ++j) {
            if(v[i]<v[j]){
                aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }

    for (int i = 1; i <=n ; ++i) {
        cout<<v[i]<<" ";
    }

    return 0;
}

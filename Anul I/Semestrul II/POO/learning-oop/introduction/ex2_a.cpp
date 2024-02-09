////2)
////a)
//
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int vfrecv[100001];
//int main(){
//    int n,v[101],w[100001],k=0;
//    cin>>n;
//    for (int i = 0; i < n; ++i) {
//        cin>>v[i];
//    }
//    sort(v, v+n);
//    reverse(v,v+n);
//    for (int i = 0; i < n-1; ++i) {
//        if (v[i]==v[i+1]){
//            for (int j = i+1; j < n; ++j) {
//                v[j]=v[j+1];
//                n--;
//            }
//        }
//    }
//
//    for (int i = 0; i < n-1; ++i) {
//        for (int j = i+1; j < n; ++j) {
//            if(v[i]%v[j]==0){
//                if (vfrecv[v[i]/v[j]]!=1) {
//                    vfrecv[v[i] / v[j]] = 1;
//                    cout << v[i] << "/" << v[j] << " ";
//                }
//            }
//            else{
//                cout<<v[i]<<"/"<<v[j]<<" ";
//            }
//        }
//    }
//}
//

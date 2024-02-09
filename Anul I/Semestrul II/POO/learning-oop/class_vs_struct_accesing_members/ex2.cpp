//#include <iostream>
//#include <string>
//#include <algorithm>
//using namespace std;
//
//class Filme{
//    string titlu;
//    int like;
//
//public:
//    void citeste(){
//        cout<<"Titlu:";
//        getline(cin, titlu);
//        cout<<endl;
//        cout<<"Numar likeuri:";
//        cin>>like;
//        cin.get();
//    }
//
//    int getLike(){
//        return like;
//    }
//
//    string getTitlu(){
//        return titlu;
//    }
//};
//
//bool compare(Filme i, Filme j) {
//    return(i.getLike() < j.getLike());
//}
//
//void afisarePopulare(int n, Filme filme[], int k){
//    sort(filme,filme+n, compare);
//    for (int i = n-1; i >= 0 ; --i) {
//        if(k!=0){
//            cout<<filme[i].getTitlu()<<endl;
//            k--;
//        }
//        else{
//            return;
//        }
//    }
//}
//
//int main(){
//    int n,k;
//    cout<<"n=";
//    cin>>n;
//    cout<<endl;
//    cout<<"k=";
//    cin >> k;
//    cin.get();
//    Filme filme[n];
//
//    for (int i = 0; i < n; ++i) {
//        filme[i].citeste();
//    }
//
//    afisarePopulare(n,filme,k);
//
//}
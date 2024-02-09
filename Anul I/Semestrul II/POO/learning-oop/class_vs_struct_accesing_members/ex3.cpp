//#include <iostream>
//#include <string>
//
//using namespace std;
//
//class Tablou{
//    int h, l, pret;
//    string msj;
//public:
//    void citeste(){
//        cout<<"Mesaj motivational:";
//        getline(cin,msj);
//        cout<<"Inaltimea:";
//        cin>>h;
//        cout<<"Latimea:";
//        cin>>l;
//        cout<<"Pret:";
//        cin>>pret;
//        cin.get();
//    }
//
//    void showAll(){
//        cout<<h<<" "<<l<<" "<<pret;
//    }
//
//    int nrcuv(){
//        int nr=0;
//        for (int i = 0; msj[i]!='\0'; ++i) {
//            if (msj[i]==' ')
//                nr++;
//        }
//        return nr;
//    }
//};
//
//int main(){
//    int n;
//    cout<<"n=";
//    cin>>n;
//    cin.get();
//    Tablou tablouri[n];
//    for (int i = 0; i < n; ++i) {
//        tablouri[i].citeste();
//    }
//
//    int max=0;
//    int poz;
//    for (int i = 0; i < n; ++i) {
//        if (max<tablouri[i].nrcuv()){
//            max=tablouri[i].nrcuv();
//            poz = i;
//        }
//    }
//    tablouri[poz].showAll();
//    cout<<endl<<max;
//}
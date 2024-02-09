//#include <iostream>
//using namespace std;
//
//class Carte{
//    string titlu;
//    int nrpag,pagcur;
//
//public:
//
//    Carte(){
//        cout<<"Constructor gol!"<<endl;
//        titlu = "";
//        nrpag = -1;
//        pagcur = -1;
//    }
//    Carte(string _titlu, int _nrpag, int _pagcur){
//        titlu = _titlu;
//        nrpag = _nrpag;
//        pagcur = _pagcur;
//    }
//    void citeste(){
//        cout<<"Titlul:";
//        getline(cin, titlu);
//        cout<<"Numar pagini:";
//        cin>>nrpag;
//        cout<<"Pagina curenta:";
//        cin>>pagcur;
//        cin.get();
//    }
//    void afiseaza(){
//        cout<<"Cartea cu titlul \""<<titlu<<"\" sta deschisa la pagina "<<pagcur<<" din "<<nrpag<<endl;
//    }
//
//    void setPaginaCurenta(int _pagcur){
//        if (_pagcur < getPaginaMaxima()){
//            pagcur = _pagcur;
//        } else {
//            cout<<"Nu poti sari la pagina "<<_pagcur<<" din "<<nrpag<<", deoarece nu exista!";
//        }
//    }
//
//    int getPaginaMaxima(){
//        return nrpag;
//    }
//};
//
//
//int main(){
//    Carte c;
//    c.citeste();
//    c.afiseaza();
//
//    c.setPaginaCurenta(30);
//    c.afiseaza();
//
//    c.setPaginaCurenta(c.getPaginaMaxima() + 1);
//    return 0;
//}

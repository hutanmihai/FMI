#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

class IntervalOrar{
    int orainc, mininc, orasf, minsf;

public:
    IntervalOrar(){
        cout<<"Constructor gol!"<<endl;
        orainc = -1;
        mininc = -1;
        orasf = -1;
        minsf = -1;
    }
    IntervalOrar(int _orainc, int _mininc, int _orasf, int _minsf){
        orainc = _orainc;
        mininc = _mininc;
        orasf = _orasf;
        minsf = _minsf;
    }

    void citeste(){
        cout<<"Ora inceput:";cin>>orainc;
        cout<<"Minut inceput:";cin>>mininc;
        cout<<"Ora sfarsit:";cin>>orasf;
        cout<<"Minut sfarsit:";cin>>minsf;
    }
    int getOraInceput(){
        return orainc;
    }
    int getMinutInceput(){
        return mininc;
    }
    int getOraSfarsit(){
        return orasf;
    }
    int getMinutSfarsit(){
        return minsf;
    }
};

class Camin{
    string denumire;
    int nrcamere;
    int nroreliniste;
    IntervalOrar oreliniste[10];

public:
    Camin(){
        cout<<"Constructor gol!"<<endl;
        nrcamere = -1;
        denumire = "";
        nroreliniste = 0;

    }
    Camin(string _denumire, int _nrcamere, IntervalOrar _oreliniste[], int _nroreliniste){
        denumire = _denumire;
        nrcamere = _nrcamere;
        nroreliniste = _nroreliniste;
        for (int i = 0; i < _nroreliniste; ++i) {
            oreliniste[i]=_oreliniste[i];
        }
    }
    void citeste(){
        cout<<"Denumire:";cin.ignore();getline(cin,denumire);
        cout<<"Numar Camere:";cin>>nrcamere;
        cout<<"Numar intervale de liniste:";cin>>nroreliniste;
        cout<<"Intervale orare de liniste:"<<endl;
        for (int i = 0; i < nroreliniste; ++i) {
            oreliniste[i].citeste();
        }
    }

    int getOraInc(int j){
         return oreliniste[j].getOraInceput();
    }
    int getMinutInc(int j){
        return oreliniste[j].getMinutInceput();
    }
    int getOraSf(int j){
        return oreliniste[j].getOraSfarsit();
    }
    int getMinutSf(int j){
        return oreliniste[j].getMinutSfarsit();
    }
    int getNrOreLiniste(){
        return nroreliniste;
    }



};

int main(){
    int nrcamine,orainc,orasf,mininc,minsf;
    cout<<"NrCamine=";cin>>nrcamine;
    Camin camine[nrcamine];
    int vore[24];
    int vmin[60];
    for (int i = 0; i < 24; ++i) {
        vore[i]=1;
    }
    for (int i = 0; i < 60; ++i) {
        vmin[i]=1;
    }
    for (int i = 0; i < nrcamine; ++i) {
        camine[i].citeste();
    }

    return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#define inf -999999
using namespace std;
ifstream f("statie.in");
ifstream fi("noi.in");
ofstream o("statie.out");
vector<int>tata,inaltime,dimensiune;
int numarNoduri,numarComponente,dimensiuneMaxima=inf;

void initializare()
{
    tata.resize(numarNoduri+1,0);
    inaltime.resize(numarNoduri+1,0);
    dimensiune.resize(numarNoduri+1,1);
}
int Find(int u) //TO DO - compresie de cale
{
    while(tata[u]!=0)
        u=tata[u];
    //compresie (urmeaza)
    return u;
}
int Union(int u,int v) //link by rank - TO DO link by size (dupa dimensiune - se poate renunta la inaltime)
{
    int reprezentantU=Find(u);
    int reprezentantV=Find(v);
    if(reprezentantU==reprezentantV)
        return 0;
    if(inaltime[reprezentantU]==inaltime[reprezentantV]) //if(dimensiune[reprezentantU]==dimensiune[reprezentantV])
    {
        tata[reprezentantV]=reprezentantU;
        inaltime[reprezentantU]++;
        dimensiune[reprezentantU]+=dimensiune[reprezentantV];
        return dimensiune[reprezentantU];
    }
    else if(inaltime[reprezentantU]>inaltime[reprezentantV])//if(dimensiune[reprezentantU]>dimensiune[reprezentantV])
    {
        tata[reprezentantV]=reprezentantU;
        dimensiune[reprezentantU]+=dimensiune[reprezentantV];
        return dimensiune[reprezentantU];
    }
    else
    {
        tata[reprezentantU]=reprezentantV;
        dimensiune[reprezentantV]+=dimensiune[reprezentantU];
        return dimensiune[reprezentantV];
        }
}
void afisareTata()
{
    for(int i=1; i<=numarNoduri; i++)
        cout<<tata[i]<<" ";
    cout<<"\n";
}
void afisareInaltime()
{
    for(int i=1; i<=numarNoduri; i++)
        cout<<inaltime[i]<<" ";
    cout<<"\n";
}
int main()
{

    f>>numarNoduri>>numarComponente;
    initializare();
    for(int i=1; i<=numarComponente; i++)
    {
        int dimensiuneComponenta;
        f>>dimensiuneComponenta;
        int primulElement;
        f>>primulElement;
        for(int j=2; j<=dimensiuneComponenta; j++)
        {
            int elementCurent,dimensiuneNoua;
            f>>elementCurent;
            dimensiuneNoua=Union(primulElement,elementCurent);
            dimensiuneMaxima=max(dimensiuneMaxima,dimensiuneNoua);
        }
    }
    afisareTata();
    afisareInaltime();
    int muchieNoua1,muchieNoua2;
    while(fi>>muchieNoua1>>muchieNoua2)
    {

        if(Find(muchieNoua1)!=Find(muchieNoua2))
        {
            int dimensiuneNoua;
            dimensiuneNoua=Union(muchieNoua1,muchieNoua2);
            dimensiuneMaxima=max(dimensiuneMaxima,dimensiuneNoua);
            numarComponente--;
        }
        cout<<"Adaugam muchia ( "<<muchieNoua1<<" , "<<muchieNoua2<<" )\n";
        cout<<"Numar componente : "<<numarComponente<<" "<<"\n";
        cout<<"Dimensiunea maxima : "<<dimensiuneMaxima<<"\n";
        afisareTata();
        afisareInaltime();
    }
    return 0;
}

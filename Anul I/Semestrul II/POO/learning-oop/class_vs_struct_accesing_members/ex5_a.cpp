//#include <iostream>
//using namespace std;
//
//class Client{
//    int id, suma;
//
//public:
//    Client(){
//        cout<<"Constructorul este gol!"<<endl;
//        id = 0;
//        suma = 0;
//    }
//    Client(int _id,int _suma){
//        id = _id;
//        suma = _suma;
//    }
//
//    int getSuma(){
//        return suma;
//    }
//
//    void citeste(){
//        cout<<"id =";
//        cin>>id;
//        cout<<"suma =";
//        cin>>suma;
//    }
//};
//
//class Banca{
//    int nrclienti;
//    Client clienti[];
//
//public:
//    Banca(){
//        cout<<"Constructorul este gol!"<<endl;
//        nrclienti = 0;
//
//    }
//    Banca(int _nrclienti,Client _clienti[]){
//        nrclienti = _nrclienti;
//        for (int i = 0; i < nrclienti; ++i) {
//            clienti[i] = _clienti[i];
//        }
//    }
//    void getTotal(){
//        int total = 0;
//        for (int i = 0; i < nrclienti; ++i) {
//            total += clienti[i].getSuma();
//        }
//        cout<<"Suma totala de bani aflati in banca este "<<total<<endl;
//    }
//
//    void getStats(){
//        int peste1000 = 0;
//        float peste100 = 0;
//        for (int i = 0; i < nrclienti; ++i) {
//            if (clienti[i].getSuma() > 100)
//                peste100++;
//            if (clienti[i].getSuma() > 1000)
//                peste1000++;
//        }
//        cout<<"Numarul de clienti cu cel putin 1000 RON in cont este de "<<peste1000<<",iar procentul celor care au peste 100 RON este de "<<(peste100*100)/nrclienti<<"%."<<endl;
//    }
//    void citeste(){
//        cout<<"nrclienti =";
//        cin>>nrclienti;
//        for (int i = 0; i < nrclienti; ++i) {
//            clienti[i].citeste();
//        }
//    }
//};
//
//int main(){
//    Banca BT;
//    BT.citeste();
//    BT.getTotal();
//    BT.getStats();
//
//    return 0;
//}
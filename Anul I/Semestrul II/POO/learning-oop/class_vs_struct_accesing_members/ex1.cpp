//#include <iostream>
//#include <string>
//
//using namespace std;
//
//class Bilet {
//
//private:
//    string nume;
//    bool clasa1;
//
//public:
//    Bilet() {
//        // cout << "Constructor gol!" << endl;
//        nume = "";
//        clasa1 = false;
//    }
//
//    Bilet(string _nume, bool _clasa1) {
//        nume = _nume;
//        clasa1 = _clasa1;
//    }
//
//    string getNume() {
//        return nume;
//    }
//
//    bool getClasa1() {
//        return clasa1;
//    }
//
//    void setNume(string _nume) {
//        nume = _nume;
//    }
//
//    void citeste() {
//        cout << "Nume:";
//        getline(cin, nume);
//        cout << endl;
//        cout << "Clasa1:";
//        cin >> clasa1;
//        cin.get();
//    }
//};
//
//void statisticaZboruri(int n, Bilet bilete[]) {
//    int da = 0, nu = 0;
//    for (int i = 0; i < n; ++i) {
//        if (bilete[i].getClasa1() == true) {
//            da++;
//        } else {
//            nu++;
//        }
//    }
//    cout << "Avem " << da << " bilete la clasa I, dar si " << nu <<" bilete la alte clase";
//}
//
//
//int main() {
//
//    int n;
//    cout << "n =";
//    cin >> n;
//    cin.get();
//    Bilet bilete[n];
//
//    for (int i = 0; i < n; ++i) {
//        bilete[i].citeste();
//    }
//    statisticaZboruri(n, bilete);
//    return 0;
//}

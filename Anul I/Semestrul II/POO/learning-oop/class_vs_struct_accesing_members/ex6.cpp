//#include <iostream>
//#include <string>
//#include <tuple>
//#include <algorithm>
//
//using namespace std;
//
//class Data {
//    int ziinc, lunainc, aninc, zisf, lunasf, ansf;
//
//public:
//    Data() {
//        cout << "Constructor gol!" << endl;
//        ziinc = -1;lunainc = -1;aninc = -1;zisf = -1;lunasf = -1;ansf = -1;
//    }
//
//    Data(int _ziinc, int _lunainc, int _aninc, int _zisf, int _lunasf, int _ansf) {
//        ziinc = _ziinc;lunainc = _lunainc;aninc = _aninc;zisf = _zisf;lunasf = _lunasf;ansf = _ansf;
//    }
//
//    void citeste() {
//        cout << "Ziua inceput:";cin >> ziinc;
//        cout << "Luna inceput:";cin >> lunainc;
//        cout << "An inceput:";cin >> aninc;
//        cout << "Ziua sfarsit:";cin >> zisf;
//        cout << "Luna sfarsit:";cin >> lunasf;
//        cout << "An sfarsit:";cin >> ansf;
//        cout << endl;
//
//    }
//
//    tuple<int, int, int> getDataInc() {
//        return {ziinc, lunainc, aninc};
//    }
//
//    tuple<int, int, int> getDataSf() {
//        return {zisf, lunasf, ansf};
//    }
//};
//
//class Eveniment {
//    string nume;
//    Data data;
//
//public:
//    Eveniment() {
//        cout << "Constructor gol!" << endl;
//    }
//
//    Eveniment(string _nume, Data _data) {
//        nume = _nume;data = _data;
//    }
//
//    void citeste() {
//        cin.ignore();
//        cout << "Nume eveniment:";getline(cin, nume);
//        data.citeste();
//    }
//
//    string getNume() {
//        return nume;
//    }
//
//    tuple<int, int, int> getDataInc() {
//        return data.getDataInc();
//    }
//
//    tuple<int, int, int> getDataSf() {
//        return data.getDataSf();
//    }
//};
//
//bool comparare(Eveniment eveniment1, Eveniment eveniment2) {
//    auto[zisf1, lunasf1, ansf1] = eveniment1.getDataSf();
//    auto[ziinc2, lunainc2, aninc2] = eveniment2.getDataInc();
//    if (ansf1 > aninc2) {
//        return false;
//    } else if (ansf1 < aninc2) {
//        return true;
//    } else if (lunasf1 > lunainc2) {
//        return false;
//    } else if (lunasf1 < lunainc2) {
//        return true;
//    } else if (zisf1 > ziinc2) {
//        return false;
//    } else if (zisf1 < ziinc2) {
//        return true;
//    } else {
//        return true;
//    }
//}
//
//bool compare(Eveniment eveniment1, Eveniment eveniment2) {
//    auto[zisf1, lunasf1, ansf1] = eveniment1.getDataSf();
//    auto[zisf2, lunasf2, ansf2] = eveniment2.getDataSf();
//    if (ansf1 > ansf2) {
//        return false;
//    } else if (ansf1 < ansf2) {
//        return true;
//    } else if (lunasf1 > lunasf2) {
//        return false;
//    } else if (lunasf1 < lunasf2) {
//        return true;
//    } else if (zisf1 > zisf2) {
//        return false;
//    } else if (zisf1 < zisf2) {
//        return true;
//    } else {
//        auto[ziinc1, lunainc1, aninc1] = eveniment1.getDataInc();
//        auto[ziinc2, lunainc2, aninc2] = eveniment2.getDataInc();
//        if (aninc1 > aninc2) {
//            return false;
//        } else if (aninc1 < aninc2) {
//            return true;
//        } else if (lunainc1 > lunainc2) {
//            return false;
//        } else if (lunainc1 < lunainc2) {
//            return true;
//        } else if (ziinc1 > ziinc2) {
//            return false;
//        } else if (ziinc1 < ziinc2) {
//            return true;
//        } else return true;
//    }
//}
//
//int main() {
//    int nrevenimente, nrev = 0;
//    cout << "Numarul evenimentelor:";
//    cin >> nrevenimente;
//    Eveniment evenimente[nrevenimente],uev;
//    string ev[nrevenimente];
//    for (int i = 0; i < nrevenimente; ++i) {
//        evenimente[i].citeste();
//    }
//    for (int i = 0; i < nrevenimente; ++i) {
//        sort(evenimente, evenimente + nrevenimente, compare);
//    }
//    ev[nrev++] = evenimente[0].getNume();
//    uev = evenimente[0];
//    for (int i = 1; i < nrevenimente; ++i) {
//        if (comparare(uev, evenimente[i]) == 1) {
//            ev[nrev++] = evenimente[i].getNume();
//            uev = evenimente[i];
//        }
//    }
//    for (int i = 0; i < nrev; ++i) {
//        cout << ev[i] << " ";
//    }
//    return 0;
//}
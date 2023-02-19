//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//// Acest exercitiu este bun pentru a simplifica un principiu util:
////   Sa programam ceva complex ca o banda de asamblare:
////
////   Vrem fractiile unice? Putem sa facem pas cu pas:
////   1. Obtinem un sir cu toate fractiile supraunitare
////   2. Sortam fractiile
////   3. Afisam doar fractiile unice (prima + cele diferite de precedenta)
//
///* Date:
//
//4
//2 8 10 4
//
//*/
//
//struct Fractie { // vom denumi cu litera mare orice structura creata :)
//    int a, b; // denumiri cat mai simple
//};
//bool cmpFractie(Fractie f1, Fractie f2) {
//    // in functiile de comparare pt sort,
//    //  vom return true doar cand vrem ca f1 sa apara inainte de f2!
//    if (f1.a * f2.b < f2.a * f1.b) { // practic  a/b < c/d   rescris ca    a*d < c*a
//        return true;
//    } else {
//        return false;
//    }
//}
//
//int main() {
//    int v[100], n, cnt;
//    Fractie vf[10000];
//
//    // citim vectorul:
//    cin >> n;
//    for (int i = 0; i < n; ++i) {
//        cin >> v[i];
//    }
//
//    // retinem toate fractiile supraunitare
//    cnt = 0;
//    for (int i = 0; i < n; ++i) {
//        for (int j = 0; j < n; ++j) {
//            if (v[i] > v[j]) {
//                // putem initializa o variabila de tip struct direct cu {valoare1, valoare2, ..., altaValoare}
//                vf[cnt] = {v[i], v[j]};
//                cnt++;
//            }
//        }
//    }
//
//    // sortam fractiile
//    // putem aplica o sortare cu doua for-uri.. sau invatam alte trucuri:
//    //
//    // avem si o metoda destul de simpla cu sort() din <algorithm>  :)
//    sort(vf, vf + cnt, cmpFractie);
//
//    // afisam doar fractiile distincte
//    cout << vf[0].a << '/' << vf[1].b << ' ';
//    for (int i = 1; i < cnt; ++i) {
//        if (vf[i].a * vf[i-1].b != vf[i].b * vf[i-1].a) {
//            cout << vf[i].a << '/' << vf[i].b << ' ';
//        }
//    }
//
//    return 0;
//}
//
//
//// TODO varianta 2: putem sa mai cream functii si pentru egalare de fractii, afisare, citire :)
////  Am implementat  in ex2_functii, dar puteti sa incercati de la zero, tinand cont ca deja ati mai exersat :D
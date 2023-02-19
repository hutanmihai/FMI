//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//// Varianta 2
//
///* Date:
//
//4
//2 8 10 4
//
//*/
//
//// vom denumi cu litera mare orice struct   creata :)
//struct Fractie {
//    int a, b; // denumiri cat mai simple
//};
//
//// 4 functii mici
//bool esteMaiMica(Fractie f1, Fractie f2) {
//    //  vom return true doar cand vrem ca f1 sa apara inainte de f2!
//    return (f1.a * f2.b < f2.a * f1.b); // practic  a/b < c/d   rescris ca    a*d < c*a
//}
//bool esteEgala(Fractie f1, Fractie f2) {
//    return f1.a * f2.b == f2.a * f1.b;
//}
//
//// nu o folosim in exercitiu, dar pare ca eram foarte entuziasmat sa va amintesc despre referinte:
////   https://www.learncpp.com/cpp-tutorial/pass-by-lvalue-reference/
////
////void citesteFractie(Fractie& f) { // este nevoie sa punem & pentru orice variabila "de output"
////    // adica valoarea lui f este modificata si in main(), ca sa putem efectua citirea
////    cin >> f.a >> f.b;
////
////}
//
//void afiseeazaFractie(Fractie& f) {
//    cout << f.a << '/' << f.b << ' ';
//}
//
//// si un main() simplu
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
//    sort(vf, vf + cnt, esteMaiMica);
//
//    // afisam doar fractiile distincte
//    afiseeazaFractie(vf[0]);
//    for (int i = 1; i < cnt; ++i) {
//        if (!esteEgala(vf[i], vf[i-1])) {
//            afiseeazaFractie(vf[i]);
//        }
//    }
//
//    return 0;
//}
//
//
//// varianta 2: putem sa mai cream functii si pentru egalare de fractii, afisare, citire :)
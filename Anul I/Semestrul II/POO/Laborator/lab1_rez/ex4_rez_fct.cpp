//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//struct Fractie {
//    int a, b;
//};
//
//int cmmdc(int a, int b) {
//    if (a == 0 || b == 0) {
//        // nu vom putea imparti la 0:
//        return 0; // un divizor imposibil
//    }
//    int r = a % b;
//    while (r != 0) {
//        a = b;
//        b = r;
//        r = a % b;
//    }
//    return b; // ultimul rest diferit de 0, este retinut in b   deoarece se executa b=r;    inainte de a se incheia while-ul
//}
//
//void simplifica(Fractie &f) {
//    int gcd = cmmdc(f.a, f.b);
//    if (gcd != 0) {
//        f.a /= gcd;
//        f.b /= gcd;
//    }
//}
//
//bool maiMic(Fractie f1, Fractie f2) {
//    return f1.a * f2.b < f2.a * f1.b;
//}
//
//Fractie scade(Fractie f1, Fractie f2) {
//    Fractie scaderea = {f1.a * f2.b - f2.a * f1.b, f1.b * f2.b};
//    simplifica(scaderea);
//
//    return scaderea;
//}
//
//void citeste(Fractie &f) {
//    cin >> f.a >> f.b;
//}
//void afiseaza(Fractie &f) {
//    cout << f.a << '/' << f.b << ' ';
//}
//
//int main() {
//    Fractie f, f2;
//
//    citeste(f);
//
//    while (f.a > 0) { // cat timp fractia este mai mare decat zero
//        int x = 2;
//        f2 = {1,x};
//        while (maiMic(f, f2)) { // citim   f<f2
//            x++;
//            f2 = {1,x};
//        }
//        afiseaza(f2);
//        f = scade(f, f2);
//    }
//
//}
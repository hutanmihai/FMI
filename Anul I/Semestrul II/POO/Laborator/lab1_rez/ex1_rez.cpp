//#include <iostream>
//
//using namespace std;
//
//// 1
///*
//    Se citesc de la tastatură 6 variabile, denumite an1, luna1, ziua1, an2, luna2, ziua2, care vor reprezenta două date calendaristice.
//    Se cere să afișați:
//
//    Care dintre cele două date calendaristice este mai mare?
//
//    Care dintre cele două date calendaristice este mai apropiată de ziua de astăzi?
//
// */
//
//// varianta cu struct:
//struct Data {
//    int an, luna, zi;
//};
//
//bool suntEgale(Data d1, Data d2) {
//    return d1.an == d2.an && d1.luna == d2.luna && d1.zi == d2.zi;
//}
//
//Data gasesteMaiMare(Data d1, Data d2) {
//    if (d1.an < d2.an) {
//        // comparam anii
//        return d2;
//    }
//    // deoarece lucram intr-o functie, nu mai este nevoie sa scriem else,
//    // deoarece ajunge la aceasta linia doar daca if-ul precedent nu era adevarat
//    // => cod mai concis
//    if (d1.an > d2.an) {
//        return d1;
//    }
//    // am trecut de cele doau if-uri? Rezulta ca avem d1.an == d2.an :D
//
//    // comparam lunile
//    if (d1.luna < d2.luna) {
//        return d2;
//    }
//    if (d1.luna > d2.luna) {
//        return d1;
//    }
//
//    // comparam zilele
//    if (d1.zi < d2.zi) {
//        return d2;
//    }
//    if (d1.zi > d2.zi) {
//        return d1;
//    }
//
//    return d1; // sau    return d2    deoarece sunt egale
//}
//
//int main() {
//    Data d1, d2;
//
//    // citim datele
//    cin >> d1.zi >> d1.luna >> d1.an;
//    cin >> d2.zi >> d2.luna >> d2.an;
//
//    // a) Putem rezolva prin a compara anii, apoi luna, apoi anul
//    // TODO sa urmarim cum implementam direct in main, si cum implementam daca folosim o functie
//    // si putem scrie intr-un comentariu datele de input ca sa le citim copiem direct in consola:
//    /*
//2 10 2021
//3 9 2021
//
//7 2 2022
//25 2 2022
//
//25 2 2022
//25 2 2022
//
//     */
//
//    // TODO 1. direct in main
//    // ne intereseaza mai mult codul usor de inteles si verificat decat super eficient, deci putem folosi inca o Data in care retinem data mai mare
//    Data maiMare;
//
//    // caz marginal: sunt egale
//    // TODO desi nu este specificat, este best practice sa tratam toate cazurile
//    if (d1.an == d2.an && d1.luna == d2.luna && d1.zi == d2.zi) {
//        cout << "a) Datele sunt egale." << '\n';
//    } else {
//        if (d1.an < d2.an) {
//            // comparam anii
//            maiMare = d2;
//        } else if (d1.an > d2.an) {
//            maiMare = d1;
//        } else {
//            // comparam lunile
//            if (d1.luna < d2.luna) {
//                maiMare = d2;
//            } else if (d1.luna > d2.luna) {
//                maiMare = d1;
//            } else {
//                // comparam zilele
//                if (d1.zi < d2.zi) {
//                    maiMare = d2;
//                } else if (d1.zi > d2.zi) {
//                    maiMare = d1;
//                }
//            }
//        }
//        cout << "a) " << maiMare.zi << '.' << maiMare.luna << '.' << maiMare.an << '\n';
//    }
//
//    // TODO 2. folosind functie pentru egalitate si pentru gasit maxim
//    if (suntEgale(d1, d2)) {
//        cout << "a) Datele sunt egale." << '\n';
//    } else {
//        maiMare = gasesteMaiMare(d1, d2);
//        cout << "a) " << maiMare.zi << '.' << maiMare.luna << '.' << maiMare.an << '\n';
//    }
//
//    // TODO Concluzie?
//    //  1. Este mai bine sa avem doua functii mici si un main simplu, comparativ cu un main complex :D;
//    //  2. In functii putem simplifica gandirea, prin a executa return
//    //     de indata ce am gasit ceea ce cautam (in cazul nostru data mai mare).
//
//
//    return 0;
//}
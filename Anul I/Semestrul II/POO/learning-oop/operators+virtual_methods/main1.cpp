#include <iostream>
#include <cmath>
#include "util/IoBase.h"
#include "util/functions.h"

using namespace std;

class IrrationalFraction;

class Fraction : public IoBase {
protected:
    int a, b;
public:
    // constructori
    Fraction(int a, int b) : a(a), b(b) {}

    Fraction() {}

    // IoBase - overrided functions
    istream &read(istream &is) override {
        IoBase::read(is);
        cout << "a: ";
        is >> a;
        cout << "b: ";
        is >> b;
        return is;
    }

    ostream &write(ostream &os) const override {
        IoBase::write(os);
        cout << "a: " << a;
        cout << ", b: " << b;
        return os;
    }

    friend bool operator<(const Fraction &f1, const IrrationalFraction &f2);

    friend IrrationalFraction operator*(const Fraction &f1, const IrrationalFraction &f2);
};

class IrrationalFraction : public Fraction {
private:
    // adaugam si radicalul dintr-un numar real
    double underSqrt;
public:
    // constructori:
    IrrationalFraction(int a, int b, double underSqrt) : Fraction(a, b), underSqrt(underSqrt) {}

    IrrationalFraction(){}

    // IoBase - overrided functions
    istream &read(istream &is) override {
        Fraction::read(is);
        cout << "underSqrt = ";
        is >> underSqrt;
        return is;
    }

    ostream &write(ostream &os) const override {
        Fraction::write(os);
        os << ", underSqrt: " << underSqrt;
        return os;
    }

    friend bool operator<(const Fraction &f1, const IrrationalFraction &f2);

    friend IrrationalFraction operator*(const Fraction &f1, const IrrationalFraction &f2);
};

bool operator<(const Fraction &f1, const IrrationalFraction &f2){
    return pow(f1.a,2)*pow(f2.b,2)*pow(f2.underSqrt,2)<pow(f2.a,2)* pow(f1.b,2);
}

IrrationalFraction operator*(const Fraction &f1, const IrrationalFraction &f2){
    return IrrationalFraction(f1.a*f2.a, f1.b*f2.b, f2.underSqrt);
}

// Vom implementa cele doua clase
// Vom implementa <
// TODO aici editorul are un feature fain, genereaza toti op >, < etc


/*
Exemplu input:

2 3         -> citim fractia 2/3
1 2 2       -> citim fractia 1/2*sqrt(2)

*/

// functie catre clasa de baza:
// TODO testati ce se intampla daca eliminati ampersand-ul
void show(const Fraction &f) {
    cout << "Fractia este: " << f << '\n';
}

int main() {
    // level 0: constructori si operatori de afisare
    Fraction f1(2,3);
    IrrationalFraction f2(1,2,2);

//    // TODO Level 1: operator de citire
    cin >> f1;
    cin >> f2;
    cout << f1 << " si " << f2 << '\n';

//    // TODO level 2: Operator supraincarcat cu clase diferite
    if (f1 < f2) {
        cout << f1 << " < " << f2 << '\n';
    } else {
        cout << f2 << " < " << f1 << '\n';
    }

//    // TODO Level 3: operatori si metode
    cout << f1 * f2 << '\n';
//    // TODO Intrebari spre rezolvare:
//    //  -----------------------------
//    // TODO Cand scadem doua fractii, una de forma a/b si cealalta a/b*sqrt(c),
//    //      la ce forma ajungem?
      //   Initial vom avea a/b - a/b*sqrt(c), apoi (a*(b*sqrt(c))-a*b)/(b*(b*sqrt(c)))

    // Aveti deja implementata functia globala show(Fraction f).
    // TODO Ce se intampla cand urmatoarele 2 linii de cod?
    // Afiseaza ambele fractii ca fiind de tip Fraction.
    show(f1);
    show(f2);
    // TODO dar daca adaugam & la parametrul din show?
    // Afiseaza cea dea doua fractie cu tot cu underSqrt adaugat in clasa IrrationalFraction ce mosteneste proprietatile clasei Fraction.
}
#include <iostream>

#include "util/IoBase.h"

using namespace std;

class Tablou : public IoBase {
protected:
    double latime;
public:

    Tablou() {}

    Tablou(double latime) : latime(latime) {}

    double cantitateUlei() {
        return Area() * 0.1;
    }

    double Area(){
        return Inaltime()*latime;
    }

    virtual double Inaltime(){};
};

class Mic : public Tablou {
private:
    double ratie;
public:

    Mic() {}

    Mic(double latime, double ratie) {
        try {
            if (latime > 0 && latime <= 10){
                this->latime = latime;
            } else {
                throw (latime);
            }
        }
        catch (double latime){
            cout << "Latimea tablourilor mici trebuie sa se afle in intervalul (0,10]cm!\n";
            cout << "Latimea este:" << latime << '\n';
            exit(1);
        }
        try {
            if (ratie >= 1 && ratie <= 3){
                this->ratie = ratie;
            } else {
                throw ratie;
            }
        }
        catch (double ratie){
            cout << "Ratia tablourilor mici trebuie sa se afle in intervalul [1,3]!\n";
            cout << "Ratia este:" << ratie << '\n';
            exit(1);
        }
    }

    double Inaltime() override {
        return latime/ratie;
        // latime/inaltime = ratie
        //inaltime == latime/ratie
    }
};

class Mediu : public Tablou {
private:
    double ratie;
public:

    Mediu() {}

    Mediu(double latime, double ratie) {
        try {
            if (latime >= 19 && latime <= 57){
                this->latime = latime;
            } else {
                throw (latime);
            }
        }
        catch (double latime){
            cout << "Latimea tablourilor medii trebuie sa se afle in intervalul [19,57]cm!\n";
            cout << "Latimea este:" << latime << '\n';
            exit(1);
        }
        try {
            if (ratie >= 0.618 && ratie <= 1.618){
                this->ratie = ratie;
            } else {
                throw ratie;
            }
        }
        catch (double ratie){
            cout << "Ratia tablourilor medii trebuie sa se afle in intervalul [0.618, 1.618]!\n";
            cout << "Ratia este:" << ratie << '\n';
            exit(1);
        }
    }

    double Inaltime() override {
        return latime/ratie;
        // latime/inaltime = ratie
        //inaltime == latime/ratie
    }
};

class Mare : public Tablou {
private:
    double ratie;
public:

    Mare() {}

    Mare(double latime, double ratie) {
        try {
            if (latime >= 100 && latime <= 1000){
                this->latime = latime;
            } else {
                throw (latime);
            }
        }
        catch (double latime){
            cout << "Latimea tablourilor mari trebuie sa se afle in intervalul [100, 1000]cm!\n";
            cout << "Latimea este:" << latime << '\n';
            exit(1);
        }
        try {
            if (ratie >= 1 && ratie <= 10){
                this->ratie = ratie;
            } else {
                throw ratie;
            }
        }
        catch (double ratie){
            cout << "Ratia tablourilor mari trebuie sa se afle in intervalul [1,10]!\n";
            cout << "Ratia este:" << ratie << '\n';
            exit(1);
        }
    }

    double Inaltime() override {
        return latime/ratie;
        // latime/inaltime = ratie
        //inaltime == latime/ratie
    }
};

int main() {
    Mic tablou_mic = Mic(10,2);
//    Mic tablou_mic_eroare = Mic(100,2);
    Mediu tablou_mediu = Mediu(25,1);
//    Mediu tablou_mediu_eroare = Mediu(25,2);
    Mare tablou_mare = Mare(500, 5);
//    Mare tablou_mare_eroare = Mare(50, 20);

    cout << tablou_mic.cantitateUlei() << '\n';
//    cout << tablou_mic_eroare.cantitateUlei() << '\n';
    cout << tablou_mediu.cantitateUlei() << '\n';
//    cout << tablou_mediu_eroare.cantitateUlei() << '\n';
    cout << tablou_mare.cantitateUlei() << '\n';
//    cout << tablou_mare_eroare.cantitateUlei() << '\n';

    return 0;
}
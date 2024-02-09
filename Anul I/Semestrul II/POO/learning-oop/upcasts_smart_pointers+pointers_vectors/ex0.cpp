#include <bits/stdc++.h>

// sau daca nu avem bits/
//  putem include <memory>
#include <memory> // shared_ptr, make_shared

// includem interfata din laboratorul trecut
#include "util/IoBase.h"

using namespace std;

class Chair : public IoBase {
protected:
    double price;
    string color;
public:
    Chair(double price, const string &color) : price(price), color(color) {}

    // Afisarea si citirea cu ajutorul functiilor virtuale va deveni mai utila astazi,
    //  deoarece am mostenit IoBase, in CLion folosim Ctrl+O pentru a implementa read/write
    ostream &write(ostream &os) const override {
        IoBase::write(os);
        cout << "price: " << price;
        cout << ", color: " << color;
        return os;
    }
};

class ArmChair : public Chair {
protected:
    string armRestMaterial;
public:
    ArmChair(double price, const string &color, const string &armRestMaterial) : Chair(price, color),
                                                                                 armRestMaterial(armRestMaterial) {}

    ostream &write(ostream &os) const override {
        Chair::write(os);
        cout << ", armRestMaterial: " << armRestMaterial;
        return os;
    }
};

class Sofa : public Chair {
private:
    int maxPeople, length;
public:
    Sofa(double price, const string &color, int maxPeople, int length) : Chair(price, color), maxPeople(maxPeople),
                                                                         length(length) {}

    ostream &write(ostream &os) const override {
        Chair::write(os);
        cout << ", maxPeople: " << maxPeople;
        cout << ", length: " << length;
        return os;
    }
};

class MassageChair : public ArmChair {
private:
    int cntLevels, cableLength;
public:
    MassageChair(double price, const string &color, const string &armRestMaterial, int cntLevels, int cableLength)
            : ArmChair(price, color, armRestMaterial), cntLevels(cntLevels), cableLength(cableLength) {}

    ostream &write(ostream &os) const override {
        ArmChair::write(os);
        cout << ", cntLevels: " << cntLevels;
        cout << ", cableLength: " << cableLength;
        return os;
    }
};

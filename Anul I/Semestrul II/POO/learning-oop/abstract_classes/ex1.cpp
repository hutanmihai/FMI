#include <iostream>

#include "util/IoBase.h"
#include "util/functions.h"

using namespace std;

/**
 * TODO discutam despre metode virtual si object slicing pe un exemplu mai simplu
 *  pe care sigur il auziti si la seminar!
 *  .
 *  Avem clasa de baza CakeShape = o forma de tort despre care stim inaltimea,
 *   dar nu si baza (patrat, dreptunghi, etc)
 *  Chiar si asa, putem calcula volumul, cu ajutorul unei functii virtuale
 *   care va calcula aria bazei:
 */

/*
 *
 */
class CakeShape {
protected:
    double height;
public:
    // calculam volumul
    virtual double volume() {
        return baseArea() * height;
    }

    // spunem ca aria bazei va fi calculata in copii,
    //  prin suprascrierea metodei virtuale:
    virtual double baseArea() {
        // returnam zero, deoarece nu stim forma:
        return 0;
    }

    // constructorii
    CakeShape(double height) : height(height) {}

    CakeShape() : height(0) {}
};

// TODO Pentru fiecare dintre clasele de mai jos vom:
//      * adauga laturile/raza;
//      * genera constructorii cu parametrii;
//      * si vom calcula aria bazei, prin suprascriere.

class SquareCake : public CakeShape {
private:
    double side;
public:
    double baseArea() override {
        return side * side;
    }

    SquareCake(double height, double side) : CakeShape(height), side(side) {}

};

class RectangleCake : public CakeShape {
private:
    double side1, side2;
public:
    // overrided functions:
    double baseArea() override {
        return side1 * side2;
    }

    // constructori
    RectangleCake(double height, double side1, double side2) : CakeShape(height), side1(side1), side2(side2) {}

    RectangleCake() : side1(0), side2(0) {}
};

const double PI = 3.1459;

class CircleCake : public CakeShape {
protected:
    double radius;
public:
    // overrided functions:
    double baseArea() override {
        return PI * radius * radius;
    }

    // constructori
    CircleCake(double height, double radius) : CakeShape(height), radius(radius) {}

    CircleCake(double radius) : radius(radius) {}

    CircleCake() : radius(0) {}
};

class ConeShape : public CakeShape {
protected:
    double radius;
public:
    ConeShape() {}

    ConeShape(double radius) : radius(radius) {}

    ConeShape(double height, double radius) : CakeShape(height), radius(radius) {}

    double baseArea() override {
        return PI * radius * radius;
    }

    double volume() override {
        return baseArea() * height / 3;
    }
};

class SpecialShape : public virtual ConeShape, public virtual CircleCake {
public:
    SpecialShape(double height, double radius, double radius1) : ConeShape(height, radius), CircleCake(height,radius1) {}

    double volume() {
        return ConeShape::volume() + CircleCake::volume();
    }
};


int main() {
    // pentru prima clasa, dar si o clasa copil:
    CakeShape cake(4);
    SquareCake cube(2, 2);

    cout << cake.volume() << '\n'; // 0
    cout << cube.volume() << '\n'; // 8

    // pentru clasele derivate
    SquareCake squareCake(4, 5);
    RectangleCake rectangleCake(1, 5, 2);
    CircleCake circleCake(1, 5);
    ConeShape coneCake(1,8);
    SpecialShape specialCake(1,8,5);


    cout << squareCake.volume() << '\n'; //     100
    cout << rectangleCake.volume() << '\n'; //  10
    cout << circleCake.volume() << '\n'; //     78.6475
    cout << coneCake.volume() << '\n';
    cout << specialCake.volume() << '\n';
    return 0;
}
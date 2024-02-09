#include <iostream>
#include "util/IoBase.h"
#include "util/functions.h"

using namespace std;

/*
 * TODO discutam despre metode virtual si object slicing pe un exemplu mai simplu
 *  pe care sigur il auziti si la seminar!
 *  .
 *  Avem clasa de baza CakeShape = o forma de tort despre care stim inaltimea,
 *   dar nu si baza (patrat, dreptunghi, etc)
 *  Chiar si asa, putem calcula volumul, cu ajutorul unei functii virtuale
 *   care va calcula aria bazei:
 */
class CakeShape {
protected:
    double height;
public:
    // calculam volumul
    double volume() {
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
    double big_side;
    double small_side;
public:
    double baseArea() override {
        return big_side * small_side;
    }

    RectangleCake(double height, double big_side, double small_side) : CakeShape(height), big_side(big_side), small_side(small_side) {}
};

class CircleCake : public CakeShape {
private:
    double radius;
public:
    double baseArea() override {
        double pi = 3.1415;
        return radius*radius*pi;
    }

    CircleCake(double height, double radius) : CakeShape(height), radius(radius) {}
};


int main() {
    // pentru prima clasa, dar si o clasa copil:
    CakeShape cake(4);
    SquareCake cube(2, 2);

    cout << cake.volume() << '\n'; // 0
    cout << cube.volume() << '\n'; // 8

//    // pentru clasele derivate
    SquareCake squareCake(4, 5);
    RectangleCake rectangleCake(1, 5, 2);
    CircleCake circleCake(1, 5);

    cout << squareCake.volume() << '\n'; //     100
    cout << rectangleCake.volume() << '\n'; //  10
    cout << circleCake.volume() << '\n'; //     78.6475

    return 0;
}
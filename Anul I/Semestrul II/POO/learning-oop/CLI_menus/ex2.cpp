#include <bits/stdc++.h>
#include "util/IoBase.h"

using namespace std;

// Vom porni de la intrebarile:
// Ce ar trebui sa faca un meniu interactiv? Ce pasi sunt necesari pentru a-l folosi.

// Orice meniu va putea:
//  * lista optiunile
//  * alege corect una dintre optiuni
//  * va putea fi rulat la infinit (=interactiv din "meniul interactiv")

class BaseMenu {
public:
    virtual void listOptions() {}

    virtual int chooseOption(int first, int last) {}

    virtual void mainLoop() {}
};

class Building : public IoBase {
protected:
    string color, nume_proprietar;
public:
    Building() {}

    Building(const string &color, const string &numeProprietar) : color(color), nume_proprietar(numeProprietar) {}

    istream &read(istream &is) override {
        IoBase::read(is);
        cin.ignore();
        cout << "Numele Proprietarului:";
        getline(is, nume_proprietar);
        cout << "Culoarea cladirii: ";
        getline(is, color);
        return is;
    }

    ostream &write(ostream &os) const override {
        IoBase::write(os);
        os << "Numele proprietarului este " << nume_proprietar << " si culoare cladirii este " << color << ".\n";
        return os;
    }

    void setColor(const string &color) {
        Building::color = color;
    }

    void setNumeProprietar(const string &numeProprietar) {
        nume_proprietar = numeProprietar;
    }
};

class Apartment : public Building {
private:
    int floor;
public:
    Apartment() {}

    Apartment(const string &color, const string &numeProprietar, int floor) : Building(color, numeProprietar),
                                                                              floor(floor) {}

    istream &read(istream &is) override {
        Building::read(is);
        cout << "Etajul:";
        is >> floor;
        return is;
    }

    ostream &write(ostream &os) const override {
        Building::write(os);
        os << "Etajul este " << floor << ".\n";
        return os;
    }

    void setFloor(int floor) {
        Apartment::floor = floor;
    }
};

class House : public Building {
private:
    int cntFloors;
public:
    House() {}

    House(const string &color, const string &numeProprietar, int cntFloors) : Building(color, numeProprietar),
                                                                              cntFloors(cntFloors) {}

    istream &read(istream &is) override {
        Building::read(is);
        cout << "Numarul de etaje:";
        is >> cntFloors;
        return is;
    }

    ostream &write(ostream &os) const override {
        Building::write(os);
        os << "Numarul de etaje este: " << cntFloors << ".\n";
        return os;
    }

    void setCntFloors(int cntFloors) {
        House::cntFloors = cntFloors;
    }
};

shared_ptr<Building> citire(int tip) {
    if (tip == 5) {
        Apartment apartment;
        cin >> apartment;
        return make_shared<Apartment>(apartment);
    } else if (tip == 6) {
        House house;
        cin >> house;
        return make_shared<House>(house);
    }
}

class SimpleMenu : public BaseMenu {
private:
    vector<shared_ptr<Building>> building;
public:
    void listOptions() override {
        cout << "1.Adauga o noua cladire. \n";
        cout << "2.Afiseaza toate cladirile. \n";
        cout << "3.Sterge una dintre cladirile retinute. \n";
        cout << "4.Modifica una dintre cladirile existente. \n";
        cout << "5.Iesire. \n";
    }

    int chooseOption(int first, int last) override {
        int alegere = -1;
        while (alegere < first || alegere > last) {
            cout << '\n';
            cout << "Alegeti un numar intre " << first << " si " << last << '\n';
            listOptions();
            cout << "Alegere:";
            cin >> alegere;
        }
        return alegere;
    }

    void alegere1() {
        cout << "Alegeti tipul cladirii \n";
        cout << "1.Apartament." << '\n' << "2.Casa" << '\n';
        cout << "Alegere:";
        int alegere;
        cin >> alegere;
        if (alegere == 1) {
            shared_ptr<Building> newBuilding;
            newBuilding = citire(5);
            building.push_back(newBuilding);
        } else if (alegere == 2) {
            shared_ptr<Building> newBuilding;
            newBuilding = citire(6);
            building.push_back(newBuilding);
        }
    }

    void alegere2() {
        cout << "Acestea sunt toate cladirile existente: \n";
        int i = 0;
        for (auto cladire: building) {
            cout << ++i << '.' << *cladire;
        }
        cout << '\n';
    }

    void alegere3() {
        alegere2();
        cout << "Introduceti a cata cladire vreti sa o stergeti:";
        int index;
        cin >> index;
        index--;
        building.erase(building.begin() + index);
        cout << "Cladirea a fost stearsa cu succes!\n";
    }

    void alegere4() {
        alegere2();
        cout << "Introduceti a cata cladire vreti sa o modificati:";
        int index;
        cin >> index;
        index--;
        Apartment *asApartment = dynamic_cast<Apartment *>(building[index].get());
        House *asHouse = dynamic_cast<House *>(building[index].get());
        if (asApartment) {
            int alegere = 0;
            while (alegere != 4) {
                cout << "Introduceti ce vreti sa modificati alegand una din optiunile de mai jos:";
                cout << "1.Numele proprietarului.\n";
                cout << "2.Culoare.\n";
                cout << "3.Etajul.\n";
                cout << "4.Iesire.\n";
                cout << "Alegere:";
                cin >> alegere;
                if (alegere == 1) {
                    cout << "Introduceti noul proprietar:";
                    cin.ignore();
                    string nume;
                    getline(cin, nume);
                    building[index]->setNumeProprietar(nume);
                } else if (alegere == 2) {
                    cout << "Introduceti noua culoare:";
                    cin.ignore();
                    string culoare;
                    getline(cin, culoare);
                    building[index]->setColor(culoare);
                } else if (alegere == 3) {
                    cout << "Introduceti noul etaj:";
                    cin.ignore();
                    int etaj;
                    cin >> etaj;
                    asApartment->setFloor(etaj);
                } else if (alegere == 4) {
                    cout << "Ati parasit meniul de modificare!";
                }
            }
        } else if (asHouse) {
            int alegere = 0;
            while (alegere != 4) {
                cout << "Introduceti ce vreti sa modificati alegand una din optiunile de mai jos:";
                cout << "1.Numele proprietarului.\n";
                cout << "2.Culoare.\n";
                cout << "3.Numarul de etaje.\n";
                cout << "4.Iesire.\n";
                cout << "Alegere:";
                cin >> alegere;
                if (alegere == 1) {
                    cout << "Introduceti noul proprietar:";
                    cin.ignore();
                    string nume;
                    getline(cin, nume);
                    building[index]->setNumeProprietar(nume);
                } else if (alegere == 2) {
                    cout << "Introduceti noua culoare:";
                    cin.ignore();
                    string culoare;
                    getline(cin, culoare);
                    building[index]->setColor(culoare);
                } else if (alegere == 3) {
                    cout << "Introduceti noul etaj:";
                    cin.ignore();
                    int etaj;
                    cin >> etaj;
                    asHouse->setCntFloors(etaj);
                } else if (alegere == 4) {
                    cout << "Ati parasit meniul de modificare!";
                }
            }
        }
    }

    void mainLoop() override {
        while (true) {
            int alegere = chooseOption(1, 5);
            if (alegere == 1) {
                alegere1();
            } else if (alegere == 2) {
                alegere2();
            } else if (alegere == 3) {
                alegere3();
            } else if (alegere == 4) {
                alegere4();
            } else if (alegere == 5) {
                break;
            }

        }
        cout << '\n'
             << "Programul s-a terminat cu success";
    }
};

int main() {
    SimpleMenu menu;
    menu.mainLoop(); // păstrăm codul simplu: funcția mainLoop „ruleaza” meniul la infinit.

}


#include <bits/stdc++.h>
#include "util/IoBase.h"

using namespace std;

class BaseMenu {
public:
    virtual void listOptions() {}

    virtual int chooseOption(int first, int last) {}

    virtual void mainLoop() {}
};

class Building : public IoBase {
private:
    string color, owner;
    int height;
public:
    Building() {}

    Building(const string &color, const string &owner, int height) : color(color), owner(owner), height(height) {}

    const string &getColor() const {
        return color;
    }

    void setColor(const string &color) {
        Building::color = color;
    }

    const string &getOwner() const {
        return owner;
    }

    void setOwner(const string &owner) {
        Building::owner = owner;
    }

    int getHeight() const {
        return height;
    }

    void setHeight(int height) {
        Building::height = height;
    }

    friend bool operator<(const Building l, const Building r) {
        return l.height < r.height;
    }

    ostream &write(ostream &os) const override {
        IoBase::write(os);
        os << "Numele proprietarului este " << owner << " si culoare cladirii este " << color
           << " si inaltimea cladirii este " << height << ".\n";
        return os;
    }
};

class CrudMenu : public BaseMenu {
private:
    vector<Building> cladiri;
    map<string, function<void(vector<Building> &)> > options;
public:
    CrudMenu() {}

    CrudMenu(const vector<Building> &cladiri, const map<string, function<void(vector<Building> &)>> &options)
            : cladiri(cladiri), options(options) {}

    void listOptions() override {
        int i = 1;
        for (auto option: options) {
            cout << i++ << option.first << '\n';
        }
        cout << i << "Iesire\n";
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

    void mainLoop() override {
        while (true) {
            int alegere = chooseOption(1, options.size() + 1);
            if (alegere == options.size() + 1) {
                break;
            }
            auto pars = options.begin();
            advance(pars, alegere - 1);
            pars->second(cladiri);
        }
        cout << "============================\n" << "Programul s-a incheiat!";
    }
};

// PUTEM folosi functii globale care sa acceseze sirul de elemente
void sorteaza(vector<Building> &vector) {
    sort(vector.begin(), vector.end());
}

int main() {
    // PUTEM folosi lambda functions pentru a crea metodele
    //  function<TIP_RETURNAT(LISTA_TIP_ARGUMENTE)>
    function<void(const vector<Building> &)> afiseaza = [](const vector<Building> &v) -> void {
        for (auto building: v) {
            cout << building << '\n';
        }
    };

    CrudMenu menu(
            { // vectorul de cladiri (culoare, proprietar, inaltime)
                    Building("red", "Gabriel", 7),
                    Building("blue", "Penelope", 4),
                    Building("blue5", "Penelope", 20),
                    Building("blue3", "Penelope", 3),
                    Building("blue2", "Penelope", 1)
            },
            {  // map-ul care contine etichetele optiunilor si functiile rulata
                    {"Afiseaza", afiseaza},
                    {"Sorteaza", sorteaza}
            }
    );
    menu.mainLoop();
    return 0;
}


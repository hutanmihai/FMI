#include <bits/stdc++.h>

#include "util/IoBase.h"
#include "util/functions.h"

using namespace std;

class Jucarii : public IoBase {
protected:
    string denumire, tip;
    double volum;
public:
    Jucarii() {}

    Jucarii(const string &denumire, const string &tip, double volum) : denumire(denumire), tip(tip), volum(volum) {}

    istream &read(istream &is) override {
        IoBase::read(is);
        cout << "Denumirea jucariei:";
        cin.ignore();
        getline(is, denumire);
        cout << "Tipul jucariei:";
        getline(is, tip);
        cout << "Volumul jucariei: ";
        is >> volum;
        return is;
    }

    ostream &write(ostream &os) const override {
        IoBase::write(os);
        os << "Denumirea jucariei este: " << denumire << '\n';
        os << "Tipul jucariei este: " << tip << '\n';
        os << "Volumul jucariei este: " << volum << '\n';
        return os;
    }

};

class Clasice : public Jucarii {
private:
    string material, culoare;
public:
    Clasice() {}

    Clasice(const string &denumire, const string &tip, double volum, const string &material, const string &culoare)
            : Jucarii(denumire, tip, volum), material(material), culoare(culoare) {}

    istream &read(istream &is) override {
        Jucarii::read(is);
        cout << "Materialul jucariei:";
        getline(is, material);
        cout << "Culoarea jucariei:";
        getline(is, culoare);
        return is;
    }

    ostream &write(ostream &os) const override {
        Jucarii::write(os);
        os << "Materialul jucariei este: " << material << '\n';
        os << "Culoarea jucariei este: " << culoare << '\n';
        return os;
    }

};

class Educative : public virtual Jucarii {
protected:
    string abilitate;
public:
    Educative() {}

    Educative(const string &denumire, const string &tip, double volum, const string &abilitate) : Jucarii(denumire, tip,
                                                                                                          volum),
                                                                                                  abilitate(
                                                                                                          abilitate) {}

    istream &read(istream &is) override {
        Jucarii::read(is);
        cout << "Abiliatea dezvolatata de jucarie:";
        getline(is, abilitate);
        return is;
    }

    ostream &write(ostream &os) const override {
        Jucarii::write(os);
        os << "Abilitatea dezvoltata de jucarie este: " << abilitate << '\n';
        return os;
    }

};

class Electronice : public virtual Jucarii {
protected:
    int nrbaterii;
public:
    Electronice() {}

    Electronice(const string &denumire, const string &tip, double volum, int nrbaterii) : Jucarii(denumire, tip, volum),
                                                                                          nrbaterii(nrbaterii) {}

    istream &read(istream &is) override {
        Jucarii::read(is);
        cout << "Numarul de baterii al jucariei:";
        is >> nrbaterii;
        return is;
    }

    ostream &write(ostream &os) const override {
        Jucarii::write(os);
        os << "Numarul de baterii al jucariei este: " << nrbaterii << '\n';
        return os;
    }
};

class Moderne : public virtual Educative, public virtual Electronice {
private:
    string brand, model;
public:
    Moderne() {}

    Moderne(const string &denumire, const string &tip, double volum, string brand, string model) : Jucarii(
            denumire, tip, volum), brand(brand), model(model) {
        nrbaterii = 1;
        abilitate = "generala";
    };

    istream &read(istream &is) override {
        Jucarii::read(is);
        cout << "Brandul jucariei:";
        is >> brand;
        cout << "Modelul jucariei:";
        is >> model;
        return is;
    }

    ostream &write(ostream &os) const override {
        Jucarii:
        write(os);
        os << "Abilitatea dezvoltata este:" << abilitate << '\n' << "Numarul de baterii al jucariei este:" << nrbaterii
           <<
           '\n' << "Brandul jucariei este:" << brand << '\n' << "Modelul jucariei este:" << model << '\n';
        return os;
    }
};

class Copil : public IoBase {
protected:
    string nume, prenume, adresa;
    int varsta, nrfaptebune;
    vector<shared_ptr<Jucarii>> jucarii;
public:
    Copil() {}

    Copil(const string &nume, const string &prenume, const string &adresa, int varsta, int nrfaptebune,
          const vector<shared_ptr<Jucarii>> &jucarii) : nume(nume), prenume(prenume), adresa(adresa), varsta(varsta),
                                                        nrfaptebune(nrfaptebune), jucarii(jucarii) {}

    istream &read(istream &is) override {
        IoBase::read(is);
        cout << "Numele copilului:";
        cin.ignore();
        getline(is, nume);
        cout << "Prenumele copilului:";
        getline(is, prenume);
        cout << "Adresa copilului:";
        getline(is, adresa);
        cout << "Varsta copilului:";
        is >> varsta;
        cout << "Numarul faptelor bune ale copilului:";
        is >> nrfaptebune;
        return is;
    }

    ostream &write(ostream &os) const override {
        IoBase::write(os);
        os << "Numele copilului este: " << nume << '\n';
        os << "Prenumele copilului este: " << prenume << '\n';
        os << "Adresa copilului este: " << adresa << '\n';
        os << "Varsta copilului este: " << varsta << '\n';
        os << "Numarul faptelor bune ale copilului este: " << nrfaptebune << '\n';
        return os;
    }

    void setJucarii(vector<shared_ptr<Jucarii>> vecnou) {
        this->jucarii = vecnou;
    }

    vector<shared_ptr<Jucarii>> getJucarii(){
        return jucarii;
    }

    string getNume(){
        return nume;
    }

    int getNrFapteBune(){
        return nrfaptebune;
    }
};

class Cuminte : public Copil {
private:
    int nrdulciuri;
public:
    Cuminte() {}

    Cuminte(const string &nume, const string &prenume, const string &adresa, int varsta, int nrfaptebune,
            const vector<shared_ptr<Jucarii>> &jucarii, int nrdulciuri) : Copil(nume, prenume, adresa, varsta,
                                                                                nrfaptebune, jucarii),
                                                                          nrdulciuri(nrdulciuri) {}

    istream &read(istream &is) override {
        Copil::read(is);
        cout << "Numarul de dulciuri ale copilului:";
        is >> nrdulciuri;
        return is;
    }

    ostream &write(ostream &os) const override {
        Copil::write(os);
        os << "Numarul de dulciuri ale copilului este: " << nrdulciuri << '\n';
        return os;
    }

};

class Neastamparat : public Copil {
private:
    int nrcarbuni;
public:
    Neastamparat() {}

    Neastamparat(const string &nume, const string &prenume, const string &adresa, int varsta, int nrfaptebune,
                 const vector<shared_ptr<Jucarii>> &jucarii, int nrcarbuni) : Copil(nume, prenume, adresa, varsta,
                                                                                    nrfaptebune, jucarii),
                                                                              nrcarbuni(nrcarbuni) {}

    istream &read(istream &is) override {
        Copil::read(is);
        cout << "Numarul de carbuni ale copilului:";
        is >> nrcarbuni;
        return is;
    }

    ostream &write(ostream &os) const override {
        Copil::write(os);
        os << "Numarul de carbuni ai copilului este: " << nrcarbuni << '\n';
        return os;
    }
};

shared_ptr<Copil> citireCopil() {
    cout << "Alege tipul copilului:\n";
    cout << "1.Cuminte.\n" << "2.Neastamparat.\n";
    cout << "Introduceti alegerea facuta:";
    int tip;
    cin >> tip;
    shared_ptr<Copil> copil;
    if (tip == 1) {
        copil = make_shared<Cuminte>();
    } else if (tip == 2) {
        copil = make_shared<Neastamparat>();
    }
    cin >> *copil;
    return copil;
}

shared_ptr<Jucarii> citireJucarie() {
    cout << "Alege tipul jucariei:\n";
    cout << "1.Clasica.\n" << "2.Educativa.\n" << "3.Electronica.\n" << "4.Moderna.\n";
    cout << "Introduceti alegerea facuta:";
    int tip;
    cin >> tip;
    shared_ptr<Jucarii> jucarie;
    if (tip == 1) {
        jucarie = make_shared<Clasice>();
    } else if (tip == 2) {
        jucarie = make_shared<Educative>();
    } else if (tip == 3) {
        jucarie = make_shared<Electronice>();
    } else if (tip == 4) {
        jucarie = make_shared<Moderne>();
    }
    cin >> *jucarie;
    return jucarie;
}

bool comparare(shared_ptr<Copil> c1, shared_ptr<Copil> c2){
    return c1->getNrFapteBune() < c2->getNrFapteBune();
}

class Meniu {
private:
    vector<shared_ptr<Copil>> copii;
public:
    void listeazaOptiuni() {
        cout << "1.Citirea a n copii.\n";
        cout << "2.Afisarea a n copii.\n";
        cout << "3.Citirea a m cadouri pentru fiecare copil.\n";
        cout << "4.Afisarea a m cadouri pentru fiecare copil.\n";
        cout << "5.Gasirea unui copil dupa nume.\n";
        cout << "6.Ordonarea copiilor in functie de numarul de fapte bune.\n";
        cout << "7.Oprirea programului.\n";
    }

    int alegeOptiune() {
        cout << "Alegeti una dintre optiunile de mai jos:\n";
        listeazaOptiuni();
        cout << "Introduceti optiunea aleasa:";
        int optiune;
        cin >> optiune;
        return optiune;
    }

    void mainLoop() {
        while (true) {
            int optiune = alegeOptiune();
            if (optiune == 1) {
                citireCopii();
            } else if (optiune == 2) {
                afisareCopii();
            } else if (optiune == 3) {
                citireCadouri();
            } else if (optiune == 4) {
                afisareCadouri();
            } else if (optiune == 5) {
                gasireNume();
            } else if (optiune == 6) {
                sortareCopii();
            } else if (optiune == 7) break;
        }
    }

    void citireCopii() {
        int n;
        cout << "Numarul de copii pe care vrem sa ii citim:";
        cin >> n;
        for (int i = 0; i < n; ++i) {
            copii.push_back(citireCopil());
        }
    }

    void afisareCopii() {
        cout << "Cei " << copii.size() << " copii sunt:\n";
        for (int i = 0; i < copii.size(); ++i) {
            cout << *copii[i] << '\n';
        }
    }

    void citireCadouri() {
        for (auto copil: copii) {
            int m;
            cout << "Numarul de cadouri pe care vrem sa le adaugam fiecarui copil:";
            cin >> m;
            vector<shared_ptr<Jucarii>> jucarii;
            for (int i = 0; i < copii.size(); ++i) {
                for (int i = 0; i < m; ++i) {
                    jucarii.push_back(citireJucarie());
                }
                copii[i]->setJucarii(jucarii);
                jucarii.clear();
            }
        }
    }

    void afisareCadouri(){
        cout << "Acestea sunt cadourile copiilor:\n";
        for (int i = 0; i < copii.size(); ++i) {
            cout << "Cadourile copilului cu numarul " << i+1 << " sunt:\n";
            vector<shared_ptr<Jucarii>> curent = copii[i]->getJucarii();
            for (int j = 0; j < curent.size(); ++j) {
                cout << *curent[j] << '\n';
            }
        }
    }

    void gasireNume(){
        cout << "Introduceti numele pe care doriti sa il cautati:\n";
        string nume;
        cin.ignore();
        getline(cin,nume);
        for (int i = 0; i < copii.size(); ++i) {
            if (nume == copii[i]->getNume()){
                cout << *copii[i] << '\n';
            }
        }
    }

    void sortareCopii(){
        sort(copii.begin(),copii.end(), comparare);
    }
};

int main() {

    Meniu meniu;
    meniu.mainLoop();
    return 0;
}
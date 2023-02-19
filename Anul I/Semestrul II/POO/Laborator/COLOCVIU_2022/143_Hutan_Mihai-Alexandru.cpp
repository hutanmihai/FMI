/* Hutan Mihai-Alexandru 143
Rulat cu Clion
g++.exe (Built by MingGW-W64 version 9.0)
C++ 14
Tutore de laborator: Deaconu Stefan-Eduard */

#include <bits/stdc++.h>

using namespace std;

template<typename T>
istream &operator>>(istream &is, vector<T> &vec) {
    vec.clear();
    int n;
    cout << "n: ";
    cin >> n;
    cin.get();
    for (int i = 0; i < n; ++i) {
        T item;
        cin >> item;
        vec.push_back(item);
    }
    cin.get();
    return is;
}

template<typename T>
ostream &operator<<(ostream &os, const vector<T> &vec) {
    for (auto &elem: vec) {
        os << elem << ' ';
    }
    os << '\n';
    return os;
}

class IO_var {
public:
    virtual istream &read(istream &is) {
        return is;
    }

    virtual ostream &write(ostream &os) const {
        return os;
    }

    friend ostream &operator<<(ostream &os, const IO_var &var) {
        return var.write(os);
    }

    friend istream &operator>>(istream &is, IO_var &var) {
        return var.read(is);
    }
};

class Bilet : public IO_var {
protected:
    double pret;
    static unsigned int idStatic;
    int id;
public:
    Bilet() {
        ++idStatic;
        id = idStatic;
    };

    virtual ~Bilet() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int getId() const;
};


unsigned int Bilet::idStatic = 0;

istream &Bilet::read(istream &is) {
    cout << "Bilet adaugat!\n";
    return is;
}

ostream &Bilet::write(ostream &os) const {
    os << "Id-ul biletului este " << id << ", iar pretul acestuia este " << pret << ".\n";
    return os;
}

int Bilet::getId() const {
    return id;
}

class DeSuprafata : public Bilet {
public:
    DeSuprafata();

    virtual ~DeSuprafata() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &DeSuprafata::read(istream &is) {
    Bilet::read(is);
    return is;
}

ostream &DeSuprafata::write(ostream &os) const {
    Bilet::write(os);
    return os;
}

DeSuprafata::DeSuprafata() { pret = 2; }

class DeMetrou : public Bilet {
public:
    DeMetrou() { pret = 2.5; };

    virtual ~DeMetrou() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &DeMetrou::read(istream &is) {
    Bilet::read(is);
    return is;
}

ostream &DeMetrou::write(ostream &os) const {
    Bilet::write(os);
    return os;
}

class DeTranzit : public Bilet {
private:
    int timp;
    int ora, minut;
public:
    DeTranzit() {
        pret = 3;
        timp = 90;
    };

    virtual ~DeTranzit() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int getTimp() const;

    int getOra() const;

    int getMinut() const;
};

istream &DeTranzit::read(istream &is) {
    cout << "Introduceti ora actuala (ora la care se creeaza acest bilet):";
    is >> ora;
    cin.get();
    cout << "Introduceti minutul actual (minutul la care se creeaza acest bilet):";
    is >> minut;
    cin.get();
    cout << "Bilet adaugat cu succes!";
    return is;
}

ostream &DeTranzit::write(ostream &os) const {
    Bilet::write(os);
    os << "Acest bilet a fost creat la ora " << ora << ':' << minut << '\n';
    return os;
}

int DeTranzit::getTimp() const {
    return timp;
}

int DeTranzit::getOra() const {
    return ora;
}

int DeTranzit::getMinut() const {
    return minut;
}

class Card : public IO_var {
protected:
    static unsigned int idStatic;
    int id;
public:
    Card() {
        ++idStatic;
        id = idStatic;
    };

    int getId() const;

    virtual void AdaugaBilet(){};
};

unsigned int Card::idStatic = 0;

int Card::getId() const {
    return id;
}

class CdeSuprafata : public Card {
private:
    vector<DeSuprafata> bilete1;
    vector<DeMetrou> bilete2;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void AdaugaBilet() override;
};

istream &CdeSuprafata::read(istream &is) {
    cout
            << "Introduceti valoare n, valoare ce reprezinta numarul de bilete de suprafata pe care vreti sa le adaugati cardului.\n";
    is >> bilete1;
    cout
            << "Introduceti valoare n, valoare ce reprezinta numarul de bilete de subteran pe care vreti sa le adaugati cardului.\n";
    is >> bilete2;
    return is;
}

ostream &CdeSuprafata::write(ostream &os) const {
    os << "Biletele incarcate pe acest card sunt:\n";
    os << "Cele de tip suprafata:\n";
    os << bilete1 << '\n';
    os << "Cele de tip subteran:\n";
    os << bilete2 << '\n';
    return os;
}

void CdeSuprafata::AdaugaBilet() {
    cout << "Alegeti ce bilet vreti sa adaugati cardului.\n";
    cout << "1.De suprafata.\n2.De subteran.\n";
    int alegere;
    DeSuprafata bilet1;
    DeMetrou bilet2;
    cin >> alegere;
    cin.get();
    if (alegere == 1) {
        cin >> bilet1;
        bilete1.push_back(bilet1);
    } else {
        cin >> bilet2;
        bilete2.push_back(bilet2);
    }
}

class CdeSubteran : public Card {
private:
    vector<DeSuprafata> bilete1;
    vector<DeMetrou> bilete2;

public:
    ostream &write(ostream &os) const override;

    istream &read(istream &is) override;

    void AdaugaBilet() override;
};


ostream &CdeSubteran::write(ostream &os) const {
    os << "Biletele incarcate pe acest card sunt:\n";
    os << "Cele de tip suprafata:\n";
    os << bilete1 << '\n';
    os << "Cele de tip subteran:\n";
    os << bilete2 << '\n';
    return os;
}

istream &CdeSubteran::read(istream &is) {
    cout
            << "Introduceti valoare n, valoare ce reprezinta numarul de bilete de suprafata pe care vreti sa le adaugati cardului.\n";
    is >> bilete1;
    cout
            << "Introduceti valoare n, valoare ce reprezinta numarul de bilete de subteran pe care vreti sa le adaugati cardului.\n";
    is >> bilete2;
    return is;
}

void CdeSubteran::AdaugaBilet() {
    cout << "Alegeti ce bilet vreti sa adaugati cardului.\n";
    cout << "1.De suprafata.\n2.De subteran.\n";
    int alegere;
    DeSuprafata bilet1;
    DeMetrou bilet2;
    cin >> alegere;
    cin.get();
    if (alegere == 1) {
        cin >> bilet1;
        bilete1.push_back(bilet1);
    } else {
        cin >> bilet2;
        bilete2.push_back(bilet2);
    }
}

class CdeTranzit : public Card {
private:
    vector<DeTranzit> bilete;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void AdaugaBilet() override;
};

istream &CdeTranzit::read(istream &is) {
    cout
            << "Introduceti valoare n, valoare ce reprezinta numarul de bilete de tranzit pe care vreti sa le adaugati cardului.\n";
    is >> bilete;
    return is;
}

ostream &CdeTranzit::write(ostream &os) const {
    os << "Biletele incarcate in acest card sunt:\n";
    os << bilete;
    return os;
}

void CdeTranzit::AdaugaBilet() {
    DeTranzit bilet;
    cin >> bilet;
    bilete.push_back(bilet);
}

class Validator : public IO_var {
    shared_ptr<Card> carduri;
    int nrscanari;
    string locatia;
public:
    Validator(){nrscanari = 0;};
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void scaneaza();
};

void Validator::scaneaza() {

}

istream &Validator::read(istream &is) {
    cout << "Introduceti locatia validatorului:";
    getline(is,locatia);
    return is;
}

ostream &Validator::write(ostream &os) const {
    os << "Locatia validatorului este " << locatia << ", iar numarul scanarilor este " << nrscanari;
    return os;
}

//MENIU SINGLETON
class Meniu {
private:
    vector<Validator> validatoare;
    vector<shared_ptr<Card>> carduri;
    static Meniu *instanta;

    Meniu() = default;

    Meniu(const Meniu &m) = default;

    Meniu &operator=(Meniu &ob) = default;

public:
    static Meniu *getInstanta() {
        if (instanta == nullptr)
            instanta = new Meniu();
        return instanta;
    }

    static void deleteInstanta() {
        if (instanta != nullptr)
            delete instanta;
        instanta = nullptr;
    }

    ~Meniu() = default;

    void afisareaOptiunilor() {
        cout << "1.Creare card.\n";
        cout << "2.Creare aparat validare.\n";
        cout << "3.Adaugare bilet unui card.\n";
        cout << "4.Validarea unui card.\n";
        cout << "5.Modificarea minutului curent.\n";
        cout << "6.Afisarea detaliilor unui card.\n";
        cout << "7.Afisarea detaliilor unui aparat de validare.\n";
        cout << "8.Oprire program!\n";
    }

    void mainLoop() {
        int alegere;
        while (true) {
            cout << "Alegeti una dintre optiunile de mai jos:\n";
            afisareaOptiunilor();
            cout << "Alegerea facuta:";
            try {
                cin >> alegere;
                cin.get();
                if (alegere < 0 || alegere > 8)
                    throw string("Optiune gresita!\n");
                else {
                    if (alegere == 1) {
                        cout << "Alegeti tipul cardului pe care vreti sa il adaugati:\n";
                        cout << "1.Pentru suprafata\n2.Pentru subteran.\n3.Pentru tranzit.\n";
                        cout << "Alegere:";
                        shared_ptr<Card> temp;
                        cin >> alegere;
                        cin.get();
                        if (alegere == 1) {
                            temp = make_shared<CdeSubteran>();
                        } else if (alegere == 2) {
                            temp = make_shared<CdeSuprafata>();
                        } else if (alegere == 3) {
                            temp = make_shared<CdeTranzit>();
                        }
                        cin >> *temp;
                        carduri.push_back(temp);
                        cout << "Succes!\n";
                    } else if (alegere == 2) {
                        Validator validator;
                        cin >> validator;
                        validatoare.push_back(validator);
                        cout << "Succes!\n";
                    } else if (alegere == 3) {
                        cout << "Introduceti id-ul cardului caruia vreti sa ii adaugati un bilet:";
                        int id;
                        int pos;
                        cin >> id;
                        bool gasit = 0;
                        for (int i = 0; i < carduri.size(); ++i) {
                            if (carduri[i]->getId() == id) {
                                gasit = 1;
                                pos = i;
                                break;
                            }
                            if (gasit == 0) {
                                cout << "ID GRESIT!\n";
                            }
                        }
                        if (gasit == 1) {
                            carduri[pos]->AdaugaBilet();
                        }
                    } else if (alegere == 4) {

                    } else if (alegere == 5) {

                    } else if (alegere == 6) {

                    } else if (alegere == 7) {

                    } else if (alegere == 8) {
                        cout << "Program oprit cu succes!\n";
                        break;
                    }
                }
            }
            catch (string &s) {
                cout << s << '\n';
            }
        }
    }
};

Meniu *Meniu::instanta = nullptr;

int main() {
    Meniu *meniu = meniu->getInstanta();
    meniu->mainLoop();
    meniu->deleteInstanta();
    return 0;
}
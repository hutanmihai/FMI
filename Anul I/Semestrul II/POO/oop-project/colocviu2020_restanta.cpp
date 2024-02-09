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


class Comanda : public IO_var {
protected:
    static unsigned int idStatic;
    unsigned int id;
    string numeClient;
    string adresaClient;
    double pretFinal;
    unsigned int ora;
    unsigned int minut;
    vector<pair<int, string>> produse;
public:
    Comanda() {
        pretFinal = 0;
        ++idStatic;
        id = idStatic;
    }

    virtual ~Comanda() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    unsigned int getId() const;

    const string &getNumeClient() const;

    double getPretFinal() const;
};

unsigned int Comanda::idStatic = 0;

istream &Comanda::read(istream &is) {
    cout << "Numele clientului:";
    getline(is, numeClient);
    cout << "Adresa clientului:";
    getline(is, adresaClient);
    cout << "Ora livrarii:";
    is >> ora;
    cin.get();
    cout << "Minutul livrarii:";
    is >> minut;
    cin.get();
    cout << "Numarul de produse al comenzii:";
    int n;
    cin >> n;
    cin.get();
    produse.clear();
    for (int i = 0; i < n; ++i) {
        pair<int, string> temp;
        int canttemp;
        string numetemp;
        cout << "Numele produslui:";
        getline(is, numetemp);
        cout << "Cantitatea acestui produs:";
        is >> canttemp;
        cout << "Pretul produsului:";
        double temppret;
        is >> temppret;
        pretFinal += temppret * canttemp;
        cin.get();
        temp.first = canttemp;
        temp.second = numetemp;
        produse.push_back(temp);
    }
    return is;
}

ostream &Comanda::write(ostream &os) const {
    os << "Id-ul comenzii este " << id << ", numele clientului este " << numeClient << ", adresa sa este "
       << adresaClient << ", pretul total al comenzii este de " <<
       pretFinal << " lei.\n" << "Momentul livrarii este ora " << ora << ":" << minut << ", iar acesta a comandat:\n";
    for (auto &produs: produse) {
        os << produs.first << " x " << produs.second << '\n';
    }
    return os;
}

unsigned int Comanda::getId() const {
    return id;
}

const string &Comanda::getNumeClient() const {
    return numeClient;
}

double Comanda::getPretFinal() const {
    return pretFinal;
}

class Mancare : public Comanda {
protected:
    string numeRestaurant;
public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Mancare::read(istream &is) {
    Comanda::read(is);
    cout << "Numele restaurantului:";
    getline(is, numeRestaurant);
    return is;
}

ostream &Mancare::write(ostream &os) const {
    Comanda::write(os);
    os << "Numele restaurantului este " << numeRestaurant << ".\n";
    return os;
}

class Medicament : public Comanda {
private:
    vector<pair<bool, string>> areAntibiotic;
public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

};

istream &Medicament::read(istream &is) {
    Comanda::read(is);
    areAntibiotic.clear();
    pair<bool, string> temp;
    int tempint;
    for (int i = 0; i < produse.size(); ++i) {
        cout << "Contine produsul " << produse[i].second << " antibiotic?\nIntroduceti 1 pentru da sau 2 pentru nu.\n";
        is >> tempint;
        temp.first = tempint;
        temp.second = produse[i].second;
        cin.get();
        areAntibiotic.push_back(temp);
    }
    return is;
}

ostream &Medicament::write(ostream &os) const {
    Comanda::write(os);
    for (int i = 0; i < produse.size(); ++i) {
        if (areAntibiotic[i].first == 1) {
            os << "Produsul " << areAntibiotic[i].second << " are antibiotic!";
        } else os << "Produsul " << areAntibiotic[i].second << " NU are antibiotic!";
    }
    return os;
}

class Tigari : public Comanda {
private:
    vector<pair<bool, string>> suntClasice;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Tigari::read(istream &is) {
    Comanda::read(is);
    suntClasice.clear();
    pair<bool, string> temp;
    int tempint;
    for (int i = 0; i < produse.size(); ++i) {
        cout << "Este produsul " << produse[i].second << " tigara clasica?\nIntroduceti 1 pentru da sau 2 pentru nu.\n";
        is >> tempint;
        temp.first = tempint;
        temp.second = produse[i].second;
        cin.get();
        suntClasice.push_back(temp);
    }
    return is;
}

ostream &Tigari::write(ostream &os) const {
    Comanda::write(os);
    for (int i = 0; i < produse.size(); ++i) {
        if (suntClasice[i].first == 1) {
            os << "Produsul " << suntClasice[i].second << " este tigara clasica!";
        } else os << "Produsul " << suntClasice[i].second << " este rezerva tigara electronica!";
    }
    return os;
}

class FastFood : public Mancare {
private:
    double discount;
    bool areDiscount;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

};

istream &FastFood::read(istream &is) {
    Mancare::read(is);
    cout << "Se aplica discount?\n1.DA\n2.NU\nAlegere:";
    is >> areDiscount;
    cin.get();
    if (areDiscount != 0) {
        cout << "Introduceti procentul discountului:";
        is >> discount;
        cin.get();
    } else discount = 0;
    return is;
}

ostream &FastFood::write(ostream &os) const {
    Mancare::write(os);
    if (areDiscount == 1) {
        os << "Aceasta comanda are discount de " << discount << "%.\n";
    } else os << "Aceasta comanda nu are discount!\n";
    return os;
}

class Restaurant : public Mancare {
private:
    bool doresteTacamuri;
public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Restaurant::read(istream &is) {
    Mancare::read(is);
    cout << "Doreste tacamuri?\n1.DA\n2.NU\nAlegere:";
    is >> doresteTacamuri;
    cin.get();
    return is;

}

ostream &Restaurant::write(ostream &os) const {
    Mancare::write(os);
    if (doresteTacamuri == 1) {
        os << "Clientul doreste tacamuri!\n";
    } else os << "Clientul NU doreste tacamuri!\n";
    return os;
}

bool comparare(shared_ptr<Comanda> cmd1,shared_ptr<Comanda> cmd2){
    return cmd1->getPretFinal() < cmd2->getPretFinal();
}

//MENIU SINGLETON
class Meniu {
private:
    vector<shared_ptr<Comanda>> comenzi;

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
        cout << "1.Citire comenzi.\n";
        cout << "2.Adaugare comanda.\n";
        cout << "3.Afiseaza comenzile.\n";
        cout << "4.Stergere comanda dupa id.\n";
        cout << "5.Cautare comanda dupa id.\n";
        cout << "6.Cautare comanda dupa numele clientului.\n";
        cout << "7.Ordonare comenzi dupa pret in mod crescator.\n";
        cout << "8.Gestionare comenzi.\n";
        cout << "9.Oprire program!\n";
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
                if (alegere < 0 || alegere > 9)
                    throw string("Optiune gresita!\n");
                else {
                    if (alegere == 1) {
                        cout << "Numarul de comenzi pe care vrem sa le introducem:";
                        int n;
                        cin >> n;
                        for (int i = 0; i < n; ++i) {
                            cout << "Alegeti tipul comenzii pe care vreti sa o faceti:\n";
                            cout << "1.FastFood.\n2.Restaurant.\n3.Medicamente.\n4.Tigari.\n";
                            int optiune;
                            cin >> optiune;
                            cin.get();
                            shared_ptr<Comanda> comanda;
                            if (optiune == 1) {
                                comanda = make_shared<FastFood>();
                            } else if (optiune == 2) {
                                comanda = make_shared<Restaurant>();
                            } else if (optiune == 3) {
                                comanda = make_shared<Medicament>();
                            } else if (optiune == 4) {
                                comanda = make_shared<Tigari>();
                            }
                            cin >> *comanda;
                            comenzi.push_back(comanda);
                            break;
                        }
                    } else if (alegere == 2) {
                        cout << "Alegeti tipul comenzii pe care vreti sa o faceti:\n";
                        cout << "1.FastFood.\n2.Restaurant.\n3.Medicamente.\n4.Tigari.\n";
                        int optiune;
                        cin >> optiune;
                        cin.get();
                        shared_ptr<Comanda> comanda;
                        if (optiune == 1) {
                            comanda = make_shared<FastFood>();
                        } else if (optiune == 2) {
                            comanda = make_shared<Restaurant>();
                        } else if (optiune == 3) {
                            comanda = make_shared<Medicament>();
                        } else if (optiune == 4) {
                            comanda = make_shared<Tigari>();
                        }
                        cin >> *comanda;
                        comenzi.push_back(comanda);
                    } else if (alegere == 3) {
                        for(auto const &comanda:comenzi){
                            cout << *comanda << '\n';
                        }
                    } else if (alegere == 4) {
                        cout << "Id-ul comenzii pe care vreti sa o stergeti:";
                        int id;
                        cin >> id;
                        cin.get();
                        for (int i = 0; i < comenzi.size(); ++i) {
                            if (comenzi[i]->getId() == id){
                                comenzi.erase(comenzi.begin()+i);
                            }
                        }
                    } else if (alegere == 5) {
                        cout << "Id-ul comenzii pe care vreti sa o cautati:";
                        int id;
                        cin >> id;
                        cin.get();
                        for (int i = 0; i < comenzi.size(); ++i) {
                            if (comenzi[i]->getId() == id){
                                cout << *comenzi[i];
                            }
                        }
                    } else if (alegere == 6) {
                        cout << "Numele clientului al carui comanda o cautati:";
                        string nume;
                        getline(cin, nume);
                        for (int i = 0; i < comenzi.size(); ++i) {
                            if (comenzi[i]->getNumeClient() == nume){
                                cout << *comenzi[i];
                            }
                        }
                    } else if (alegere == 7) {
                        sort(comenzi.begin(),comenzi.end(),comparare);
                        break;
                    } else if (alegere == 8) {
                        //TODO
                        break;
                    } else if (alegere == 9) {
                        cout << "Program oprit cu succes!\n";
                        break;
                    }
                }
            }
            catch (string s) {
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
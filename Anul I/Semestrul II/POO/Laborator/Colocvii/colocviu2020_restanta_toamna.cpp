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

class Produs : public IO_var {
protected:
    double pret;
    int cantitate;
    static unsigned int idStatic;
    unsigned int id;

public:
    Produs() {
        ++idStatic;
        id = idStatic;
    };

    ~Produs() = default;

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void setPret(int pret);

    void setCantitate(int cantitate);

    double getPret() const;

    int getCantitate() const;

};


unsigned int Produs::idStatic = 0;

void Produs::setPret(int pret) {
    this->pret = pret;
}

void Produs::setCantitate(int cantitate) {
    this->cantitate = cantitate;
}

double Produs::getPret() const {
    return pret;
}

int Produs::getCantitate() const {
    return cantitate;
}

istream &Produs::read(istream &is) {
    cout << "Pretul produsului:";
    is >> pret;
    cout << "Cantitatea:";
    is >> cantitate;
    cin.get();
    return is;
}

ostream &Produs::write(ostream &os) const {
    os << "Pretul produsului este " << pret << "lei, iar cantitatea este " << cantitate << " bucati.\n";
    return os;
}

class Carte : public Produs {
private:
    string titlu;
    vector<string> autori;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    string getTitlu() const;

};

string Carte::getTitlu() const {
    return titlu;
}

istream &Carte::read(istream &is) {
    Produs::read(is);
    cout << "Introduceti titlul cartii:";
    getline(is, titlu);
    cout << "Introduceti numarul autorilor:";
    int n;
    cin >> n;
    cin.get();
    for (int i = 0; i < n; ++i) {
        cout << "Numele autorului cu numarul " << i + 1 << ":";
        string temp;
        is >> temp;
        autori.push_back(temp);
    }
    return is;
}

ostream &Carte::write(ostream &os) const {
    Produs::write(os);
    os << "Titltul cartii este " << titlu << ", iar autorii sunt:\n";
    for (auto e: autori) {
        os << e << '\n';
    }
    return os;
}

class DVD : public Produs {
protected:
    int nrMinute;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &DVD::read(istream &is) {
    Produs::read(is);
    cout << "Numarul de minute al DVD-ului:";
    is >> nrMinute;
    cin.get();
    return is;
}

ostream &DVD::write(ostream &os) const {
    Produs::write(os);
    os << "Numarul de minute al DVD-ului este " << nrMinute << " minute.\n";
    return os;
}

class Muzica : public DVD {
private:
    string numeAlbum;
    vector<string> interpreti;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Muzica::read(istream &is) {
    DVD::read(is);
    cout << "Introduceti numele albumului:";
    getline(is, numeAlbum);
    cout << "Introduceti numarul de interpreti:";
    int n;
    is >> n;
    cin.get();
    for (int i = 0; i < n; ++i) {
        cout << "Introduceti numele interpretului cu numarul " << i + 1 << ":";
        string temp;
        is >> temp;
        interpreti.push_back(temp);
    }
    return is;
}

ostream &Muzica::write(ostream &os) const {
    DVD::write(os);
    os << "Titlul albumului este " << numeAlbum << ", iar interpretii sunt:\n";
    for (auto e: interpreti) {
        os << e << "\n";
    }
    return os;
}

class Film : public DVD {
private:
    string numeFilm;
    string genFilm;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Film::read(istream &is) {
    DVD::read(is);
    cout << "Introduceti numele filmului:";
    getline(is, numeFilm);
    cout << "Introduceti genul filmului:";
    getline(is, genFilm);
    return is;
}

ostream &Film::write(ostream &os) const {
    DVD::write(os);
    os << "Numele filmului este " << numeFilm << ", iar genul acestuia este " << genFilm << ".\n";
}

class ObiecteDeColectie : public Produs {
protected:
    string denumire;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &ObiecteDeColectie::read(istream &is) {
    Produs::read(is);
    cout << "Introduceti denumirea obiectului:";
    getline(is, denumire);
    return is;
}

ostream &ObiecteDeColectie::write(ostream &os) const {
    Produs::write(os);
    os << "Denumirea obiectului este " << denumire << ".\n";
}

class Figurina : public ObiecteDeColectie {
private:
    string categorie;
    string brand;
    string material;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

};

istream &Figurina::read(istream &is) {
    ObiecteDeColectie::read(is);
    cout << "Introduceti categoria:";
    getline(is, categorie);
    cout << "Introduceti brandul:";
    getline(is, brand);
    cout << "Introduceti materialul:";
    getline(is, material);
    return is;
}

ostream &Figurina::write(ostream &os) const {
    ObiecteDeColectie::write(os);
    os << "Categoria figurinei este " << categorie << ", brandul este " << brand << ", iar materialul este " << material
       << ".\n";
    return os;
}

class Poster : public ObiecteDeColectie {
private:
    string format;

public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

};

istream &Poster::read(istream &is) {
    ObiecteDeColectie::read(is);
    cout << "Introduceti formatul posterului:";
    getline(is, format);
    return is;
}

ostream &Poster::write(ostream &os) const {
    ObiecteDeColectie::write(os);
    os << "Formatul posterului este " << format << ".\n";
    return os;
}

bool comparare(shared_ptr<Produs> &p1, shared_ptr<Produs> &p2){
    return p1->getPret() < p2->getPret();
}

//MENIU SINGLETON
class Meniu {
private:
    vector<shared_ptr<Produs>> produse;

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
        cout << "1.Citirea a n produse.\n";
        cout << "2.Afisarea produselor.\n";
        cout << "3.Editarea unui produs.\n";
        cout << "4.Ordonarea dupa pret.\n";
        cout << "5.Cautarea unei carti dupa titlu.\n";
        cout << "6.Afisarea produsului cu cea mai mare cantitate dispoinibila.\n";
        cout << "7.Oprire program!\n";
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
                if (alegere < 0 || alegere > 7)
                    throw string("Optiune gresita!\n");
                else {
                    if (alegere == 1) {
                        cout << "Introduceti numarul de produse ce vor fi citite:";
                        int n;
                        cin >> n;
                        cin.get();
                        for (int i = 0; i < n; ++i) {
                            cout << "Alegeti tipul de produs:\n";
                            cout << "1.Carte.\n2.DVD-Muzica.\n3.DVD-FILM.\n4.Figurina.\n5.Poster.\n";
                            cout << "Alegerea facuta:";
                            int temp;
                            shared_ptr<Produs> produs;
                            cin >> temp;
                            if (temp == 1) {
                                produs = make_shared<Carte>();
                            } else if (temp == 2) {
                                produs = make_shared<Muzica>();
                            } else if (temp == 3) {
                                produs = make_shared<Film>();
                            } else if (temp == 4) {
                                produs = make_shared<Figurina>();
                            } else if (temp == 5) {
                                produs = make_shared<Poster>();
                            }
                            cin >> *produs;
                            produse.push_back(produs);
                        }
                    } else if (alegere == 2) {
                        for (int i = 0; i < produse.size(); ++i) {
                            cout << *produse[i] << '\n';
                        }
                    } else if (alegere == 3) {
                        break;
                    } else if (alegere == 4) {
                        sort(produse.begin(),produse.end(), comparare);
                    } else if (alegere == 5) {
                        cout << "Titlul cartii pe care o cautam:";
                        string titlu;
                        bool gasit = 0;
                        getline(cin, titlu);
                        for (auto &var:produse) {
                            auto isCarte = dynamic_cast<Carte*>(var.get());
                            if (isCarte && isCarte->getTitlu() == titlu) {
                                gasit = 1;
                                cout << isCarte << '\n';}
                        }
                        if (gasit == 0){
                            cout << "Nu exista cartea!\n";
                        }
                    } else if (alegere == 6) {
                        int max = -1;
                        int pos = -1;
                        for (int i = 0; i < produse.size(); ++i) {
                            if (produse[i]->getCantitate() > max){
                                max = produse[i]->getCantitate();
                                pos = i;
                            }
                        }
                        cout << *produse[pos];
                    } else if (alegere == 7) {
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
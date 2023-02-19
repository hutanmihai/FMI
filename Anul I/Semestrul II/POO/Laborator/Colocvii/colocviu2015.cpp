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

    friend ostream &operator<<(ostream &os, const IO_var &base) {
        return base.write(os);
    }

    friend istream &operator>>(istream &is, IO_var &base) {
        return base.read(is);
    }
};

class Date : public IO_var {
private:
    //@TODO SAU PROTECTED
    int an, luna, zi;
public:
    Date();

    Date(const Date &data);

    Date(int an, int luna, int zi);

    virtual ~Date();

    Date &operator=(const Date &data);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    friend bool operator>(const Date &data1, const Date &data2);

    friend Date operator+(Date &data1, int zile);

    int getAn() const;

    int getLuna() const;

    int getZi() const;

    void setAn(int an);

    void setLuna(int luna);

    void setZi(int zi);

};

Date::Date() {
    an = luna = zi = 0;
}

Date::Date(const Date &data) : zi(data.zi), luna(data.luna), an(data.an) {}

Date::Date(int an, int luna, int zi) : an(an), luna(luna), zi(zi) {}

Date::~Date() {}

Date &Date::operator=(const Date &data) {
    an = data.an;
    luna = data.luna;
    zi = data.zi;
    return *this;
}

istream &Date::read(istream &is) {
    IO_var::read(is);
    cout << "Anul:";
    is >> an;
    cout << "Luna:";
    while (true) {
        try {
            is >> luna;
            cin.get();
            if (luna < 1 || luna > 12)
                throw string("Luna a fost introdusa gresit!\nIntroduceti o luna intre 1 si 12!");
            else break;
        }
        catch (string s) {
            cout << s << '\n';
        }
    }
    cout << "Ziua:";
    while (true) {
        try {
            is >> zi;
            cin.get();
            if (zi < 1 || zi > 31)
                throw string("Introduceti o zi corecta (intre 1 si 31)!");
            else break;
        }
        catch (string s) {
            cout << s << '\n';
        }
    }
    return is;
}

ostream &Date::write(ostream &os) const {
    IO_var::write(os);
    os << "Anul este " << an << ".\n";
    os << "Luna este " << luna << ".\n";
    os << "Ziua este " << zi << ".\n";
    return os;
}

bool operator>(const Date &data1, const Date &data2) {
    if (data1.an > data2.an)
        return 1;
    else if (data1.an == data2.an && data1.luna > data2.luna)
        return 1;
    else if (data1.an == data2.an && data1.luna == data2.luna && data1.zi > data2.zi)
        return 1;
    return 0;
}

Date operator+(Date &data1, int zile) {
    int zitemp = data1.getZi() + zile;
    if (zitemp > 31) {
        zitemp = zitemp - 31;
        int lunatemp = data1.getLuna() + 1;
        if (lunatemp == 13) {
            lunatemp = lunatemp - 12;
            int antemp = data1.getAn() + 1;
            data1.setAn(antemp);
        } else {
            data1.setLuna(lunatemp);
        }
    } else data1.setZi(zitemp);
    return data1;
}

int Date::getAn() const {
    return an;
}

int Date::getLuna() const {
    return luna;
}

int Date::getZi() const {
    return zi;
}

void Date::setAn(int an) {
    this->an = an;
}

void Date::setLuna(int luna) {
    this->luna = luna;
}

void Date::setZi(int zi) {
    this->zi = zi;
}

class Produs : public IO_var {
protected:
    string denumire;
    string unitateDeMasura;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    const string &getUnitateDeMasura() const;
};

istream &Produs::read(istream &is) {
    IO_var::read(is);
    cout << "Denumirea produsului:";
    getline(is, denumire);
    cout << "Unitatea de masura (buc/kg/volum):";
    getline(is, unitateDeMasura);
    return is;
}

ostream &Produs::write(ostream &os) const {
    IO_var::write(os);
    os << "Denumirea produsului este " << denumire << ", iar unitatea de masura este " << unitateDeMasura << ".\n";
    return os;
}

const string &Produs::getUnitateDeMasura() const {
    return unitateDeMasura;
}

class Perisabile : public virtual Produs {
protected:
    int perioadaValabilitate;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int getPerioadaValabilitate() const;
};

istream &Perisabile::read(istream &is) {
    Produs::read(is);
    cout << "Introduceti perioada de valabilitate ca numar de zile:";
    is >> perioadaValabilitate;
    cin.get();
    return is;
}

ostream &Perisabile::write(ostream &os) const {
    Produs::write(os);
    os << "Perioada de valabilitate a produsului este de " << perioadaValabilitate << " zile.\n";
}

int Perisabile::getPerioadaValabilitate() const {
    return perioadaValabilitate;
}

class Promotie : public virtual Produs {
protected:
    double discount;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

};

istream &Promotie::read(istream &is) {
    Produs::read(is);
    cout << "Discountul produslui:";
    is >> discount;
    cin.get();
    return is;
}

ostream &Promotie::write(ostream &os) const {
    Produs::write(os);
    os << "Discountul produsului este de " << discount << "%.\n";
    return os;
}

class Diamant : public Perisabile, public Promotie {
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;
};

istream &Diamant::read(istream &is) {
    Perisabile::read(is);
    Promotie::read(is);
    return is;
}

ostream &Diamant::write(ostream &os) const {
    Perisabile::write(os);
    Promotie::write(os);
    return os;
}

class Lot : public IO_var {
private:
    shared_ptr<Produs> produs;
    int cantitate;
    Date dataIntrare;
    int pretUnitate;
public:

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    const Date &getDataIntrare() const;

    int getCantitate() const;

    const shared_ptr<Produs> &getProdus() const;
};

istream &Lot::read(istream &is) {
    IO_var::read(is);
    cout << "Data intrarii produslui in magazin:\n";
    is >> dataIntrare;
    cout << "Alegeti tipul de produs ce este in lot:\n";
    cout << "1.Perisabil.\n2.Discount.\n3.Perisabil cu discount.\n";
    int alegere;
    shared_ptr<Produs> produs;
    while (true) {
        try {
            cin >> alegere;
            cin.get();
            if (alegere == 1) {
                produs = make_shared<Perisabile>();
                is >> *produs;
                break;
            } else if (alegere == 2) {
                produs = make_shared<Promotie>();
                is >> *produs;
                break;
            } else if (alegere == 3) {
                produs = make_shared<Diamant>();
                is >> *produs;
                break;
            } else throw string("Introduceti un tip de produs valabil! (un intreg de la 1 la 3)");
        }
        catch (string s) {
            cout << s << '\n';
        }
    }
    cout << "Cantiatea produsului intr-un lot:";
    is >> cantitate;
    cin.get();
    cout << "Pretul produslui per unitate";
    is >> pretUnitate;
    cin.get();
    return is;
}

ostream &Lot::write(ostream &os) const {
    IO_var::write(os);
    os << "Produsul:\n";
    os << *produs;
    os << "Cantitatea produsului in lot este de " << cantitate << produs->getUnitateDeMasura() << ".\n";
    os << "Data intrarii in magazin este:\n";
    os << dataIntrare;
    os << "Pretul produsului per unitate este de " << pretUnitate << " lei.\n";
    return os;
}

const Date &Lot::getDataIntrare() const {
    return dataIntrare;
}

int Lot::getCantitate() const {
    return cantitate;
}

const shared_ptr<Produs> &Lot::getProdus() const {
    return produs;
}

//MENIU SINGLETON
class Meniu {
private:
    vector<Lot> stocLot;
    vector<shared_ptr<Produs>> stocProduse;
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

    void optiunile() {
        cout << "1.Adauga produs nou.\n";
        cout << "2.Afisare produse.\n";
        cout << "3.Adauga lot nou.\n";
        cout << "4.Afisare loturi primite intre doua date calendaristice.\n";
        cout << "5.Afisarea loturilor ce pot vi vandute (nevide si neexpirate) la data curenta.\n";
        cout << "6.Vinde o anumita cantitate ceruta din stocul magazinului.\n";
        cout << "7.Oprire program!\n";
    }

    void mainLoop() {
        int alegere;
        while (true) {
            cout << "Alegeti una dintre optiunile de mai jos:\n";
            optiunile();
            cout << "Alegerea facuta:";
            try {
                cin >> alegere;
                cin.get();
                if (alegere < 0 || alegere > 7)
                    throw string("Optiune gresita!");
                else {
                    if (alegere == 1) {
                        cout << "Introduceti produsul ce vreti sa il adaugati in magazin:\n";
                        cout << "Alegeti tipul de produs ce este in lot:\n";
                        cout << "1.Perisabil.\n2.Discount.\n3.Perisabil cu discount.\n";
                        shared_ptr<Produs> produs;
                        while (true) {
                            try {
                                cin >> alegere;
                                cin.get();
                                if (alegere == 1) {
                                    produs = make_shared<Perisabile>();
                                    cin >> *produs;
                                    stocProduse.push_back(produs);
                                    cout << "Produs adaugat cu succes!\n";
                                    break;
                                } else if (alegere == 2) {
                                    produs = make_shared<Promotie>();
                                    cin >> *produs;
                                    stocProduse.push_back(produs);
                                    cout << "Produs adaugat cu succes!\n";
                                    break;
                                } else if (alegere == 3) {
                                    produs = make_shared<Diamant>();
                                    cin >> *produs;
                                    stocProduse.push_back(produs);
                                    cout << "Produs adaugat cu succes!\n";
                                    break;
                                } else throw string("Introduceti un tip de produs valabil! (un intreg de la 1 la 3)\n");
                            }
                            catch (string s) {
                                cout << s << '\n';
                            }
                        }
                    } else if (alegere == 2) {
                        for (int i = 0; i < stocProduse.size(); ++i) {
                            cout << *stocProduse[i] << '\n';
                        }
                    } else if (alegere == 3) {
                        Lot lotNou;
                        cin >> lotNou;
                        stocLot.push_back(lotNou);
                        cout << "Lot adaugat cu succes!\n";
                    } else if (alegere == 4) {
                        Date data1, data2;
                        cout << "Introduceti prima data:\n";
                        cin >> data1;
                        cout << "Introduceti a doua data:\n";
                        cin >> data2;
                        for (auto lot: stocLot) {
                            if (lot.getDataIntrare() > data1 && data2 > lot.getDataIntrare()) {
                                cout << lot << '\n';
                            }
                        }
                    } else if (alegere == 5) {
                        cout << "Introduceti data de astazi:\n";
                        Date dataAzi;
                        cin >> dataAzi;
                        for (auto lot: stocLot) {
                            if (lot.getCantitate() > 0) {
                                Date datatemp;
                                datatemp = lot.getDataIntrare();
                                shared_ptr<Produs> produs = lot.getProdus();
                                auto isPerisabil = dynamic_cast<Perisabile *>(produs.get());
                                auto isDiamant = dynamic_cast<Diamant *>(produs.get());
                                if (isPerisabil) {
                                    Date dataExpirare;
                                    dataExpirare = datatemp + isPerisabil->getPerioadaValabilitate();
                                    if (dataAzi > dataExpirare) {
                                        cout << lot;
                                    }
                                } else if (isDiamant) {
                                    Date dataExpirare;
                                    dataExpirare = datatemp + isDiamant->getPerioadaValabilitate();
                                    if (dataAzi > dataExpirare) {
                                        cout << lot;
                                    }
                                } else cout << lot;
                            }
                        }
                    } else if (alegere == 6) {
                        //TODO
                        break;
                    } else if (alegere == 7) {
                        cout << "Program terminat cu succes!\n";
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



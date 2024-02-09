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
    int an, luna, zi;
public:
    Date();

    virtual ~Date() = default;

    Date(int an, int luna, int zi);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int getAn() const;

    void setAn(int an);

    int getLuna() const;

    void setLuna(int luna);

    int getZi() const;

    void setZi(int zi);
};

Date::Date() { an = luna = zi = 0; }

Date::Date(int an, int luna, int zi) : an(an), luna(luna), zi(zi) {}

istream &Date::read(istream &is) {
    IO_var::read(is);
    cout << "Anul:";
    is >> an;
    cout << "Luna:";
    while (true) {
        try {
            is >> luna;
            cin.get();
            if (luna < 1 || luna > 12) throw ("ATI INTRODUS LUNA GRESIT!");
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
            if (zi < 1 || zi > 31) throw ("ATI INTRODUS ZIUA GRESIT!");
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
    os << "DATA:\n";
    os << "Anul este " << an << ", luna este " << luna << ", iar ziua este " << zi << ".\n";
    return os;
}

int Date::getAn() const {
    return an;
}

void Date::setAn(int an) {
    Date::an = an;
}

int Date::getLuna() const {
    return luna;
}

void Date::setLuna(int luna) {
    Date::luna = luna;
}

int Date::getZi() const {
    return zi;
}

void Date::setZi(int zi) {
    Date::zi = zi;
}

class Masca : public IO_var {
protected:
    string tip_protectie;
    double pret;
public:
    Masca();

    virtual ~Masca() {};

    Masca(string tip, double pret);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    virtual void calcPret();

    void setPret(double pret) {
        this->pret = pret;
    }
};

Masca::Masca() {
    tip_protectie = "";
    pret = 0;
}

Masca::Masca(string tip, double pret) : tip_protectie(tip), pret(pret) {}

istream &Masca::read(istream &is) {
    IO_var::read(is);
    cout << "Tipul de protectie:";
    getline(is, tip_protectie);
    return is;
}

ostream &Masca::write(ostream &os) const {
    IO_var::write(os);
    os << "Tipul de protectie este " << tip_protectie << ".\n";
    os << "Pretul este " << pret << ".\n";
}

class MascaChirugicala : public Masca {
private:
    string culoare;
    int nr_pliuri;
    bool mod;
public:
    MascaChirugicala();

    virtual ~MascaChirugicala() {};

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void calcPret() override;
};

MascaChirugicala::MascaChirugicala() {
    culoare = "";
    nr_pliuri = 0;
    mod = 0;
    tip_protectie = "";
    pret = 0;
}

istream &MascaChirugicala::read(istream &is) {
    Masca::read(is);
    cout << "Culoarea:";
    getline(is, culoare);
    cout << "Numarul de pliuri:";
    is >> nr_pliuri;
    cout << "Doriti model special? Introduceti 1 pentru da si 2 pentru nu.";
    is >> mod;
    cin.get();
    return is;
}

ostream &MascaChirugicala::write(ostream &os) const {
    Masca::write(os);
    os << "Culoarea este " << culoare << ",iar numarul de pliuri este " << nr_pliuri << ".\n";
    if (mod == 1) {
        os << "Masca este cu model special!\n";
    } else os << "Masca nu este cu model special!\n";
    return os;
}

void MascaChirugicala::calcPret() {
    Masca::calcPret();
    double temp = 0;
    if (tip_protectie == "ffp1") temp += 5;
    if (tip_protectie == "ffp2") temp += 10;
    if (tip_protectie == "ffp3") temp += 15;
    if (mod == 1) {
        temp += temp / 2;
    }
    setPret(temp);
}

class MascaPoli : public Masca {
private:
    string prindere;
public:
    MascaPoli();

    virtual ~MascaPoli() {};

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    void calcPret() override;
};

MascaPoli::MascaPoli() {
    tip_protectie = "";
    pret = 0;
    prindere = "";
}

istream &MascaPoli::read(istream &is) {
    Masca::read(is);
    cout << "Tipul prinderii:";
    getline(is, prindere);
    return is;
}

ostream &MascaPoli::write(ostream &os) const {
    Masca::write(os);
    os << "Tipul prinderii este " << prindere << ".\n";
    return os;
}

void MascaPoli::calcPret() {
    Masca::calcPret();
    setPret(20);
}

class Dezinfectant : public IO_var {
protected:
    int nrspecii;
    vector<string> ingrediente;
    vector<string> suprafete;
    double pret;
    double eficienta;
public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    virtual void calcEficienta();

    void calcPret() {
        if (eficienta < 90) setPret(10);
        else if (eficienta < 95) setPret(20);
        else if (eficienta < 97.5) setPret(30);
        else if (eficienta < 99) setPret(40);
        else if (eficienta < 99.99) setPret(50);
    };

    void setPret(double pret);

    void setEficienta(double eficienta);

    double getEficienta();
};

double Dezinfectant::getEficienta() {
    return eficienta;
}

void Dezinfectant::setPret(double pret) {
    this->pret = pret;
}

void Dezinfectant::setEficienta(double eficienta) {
    this->eficienta = eficienta;
}

istream &Dezinfectant::read(istream &is) {
    IO_var::read(is);
    cout << "Numarul de specii ucise de dezinfectant:";
    is >> nrspecii;
    cin.get();
    cout
            << "Introduceti numarul n, care este egal cu numarul de ingrediente folosite. Apoi introduceti n ingrediente.\n";
    is >> ingrediente;
    cout
            << "Introduceti numarul n, care este egal cu numarul de suprafete pe care poate fi folosit dezinfectantul. Apoi introduceti n suprafete.\n";
    is >> suprafete;
    return is;
}

ostream &Dezinfectant::write(ostream &os) const {
    IO_var::write(os);
    os << "Numarul de specii ucise de dezinfectant este " << nrspecii << ".\n";
    os << "Ingredientele folosite sunt:\n";
    os << ingrediente;
    os << "Suprafetele pe care poate fi folosit dezinfectantul sunt:\n";
    os << suprafete;
    os << "Pretul sau este " << pret << ".\n";
    os << "Eficienta sa este " << eficienta << ".\n";
    return os;
}

class Bacterii : public virtual Dezinfectant {
public:
    void calcEficienta() override {
        double temp;
        temp = nrspecii / pow(10, 9);
        setEficienta(temp);
    }
};

class Fungi : public virtual Dezinfectant {
public:
    void calcEficienta() override {
        double temp;
        temp = nrspecii / (pow(10, 6) * 1.5);
        setEficienta(temp);
    }
};

class Virusi : public virtual Dezinfectant {
public:
    void calcEficienta() override {
        double temp;
        temp = nrspecii / pow(10, 8);
        setEficienta(temp);
    }
};

class ALL : public Bacterii, public Fungi, public Virusi {
public:
    void calcEficienta() override {
        double temp;
        temp += nrspecii / pow(10, 9);
        temp += nrspecii / (pow(10, 6) * 1.5);
        temp += nrspecii / pow(10, 8);
        setEficienta(temp);
    }
};

class Achizitie : public IO_var {
private:
    Date data;
    string nume;
    vector<shared_ptr<Dezinfectant>> dez;
    vector<shared_ptr<Masca>> masti;
    double total;
public:
    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int getLuna();

    Date getData();

    double getTotal();
};

double Achizitie::getTotal() {
    return total;
}

Date Achizitie::getData() {
    return data;
}

int Achizitie::getLuna() {
    return getData().getLuna();
}

istream &Achizitie::read(istream &is) {
    IO_var::read(is);
    cout << "Data achizitiei:";
    is >> data;
    cout << "Numele clientului:";
    getline(is, nume);
    cout << "Numarul de dezinfectante achizionate:";
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Alegeti tipul dezinfectantului:\n";
        cout << "1.Contra Bacterii.\n2.Contra Fungi.\n3.Contra virusi.\n4.Contra tuturor.\n";
        int optiune;
        cout << "Optiunea:";
        cin >> optiune;
        cin.get();
        shared_ptr<Dezinfectant> dezinfectant;
        if (optiune == 1) {
            dezinfectant = make_shared<Bacterii>();
        } else if (optiune == 2) {
            dezinfectant = make_shared<Fungi>();
        } else if (optiune == 3) {
            dezinfectant = make_shared<Virusi>();
        } else if (optiune == 4) {
            dezinfectant = make_shared<ALL>();
        }
        is >> *dezinfectant;
        dez.push_back(dezinfectant);
    }
    cout << "Numarul de masti achizitionate:";
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Alegeti tipul mastii:\n";
        cout << "1.Chirurgicala.\n2.Policarbonata.\n";
        cout << "Optiunea aleasa:";
        int optiune;
        cin >> optiune;
        cin.get();
        shared_ptr<Masca> msc;
        if (optiune == 1) {
            msc = make_shared<MascaChirugicala>();
        }
        if (optiune == 2) {
            msc = make_shared<MascaPoli>();
        }
        is >> *msc;
        masti.push_back(msc);
    }
    return is;
}

ostream &Achizitie::write(ostream &os) const {
    IO_var::write(os);
    os << "Data achizitiei: " << data << ".\n";
    os << "Numele clientului: " << nume << ".\n";
    os << "Dezinfectantii achizionati:\n\n";
    for (auto elem: dez) {
        os << *elem;
    }
    os << "Mastile achizitionate:\n\n";
    for (auto elem: masti) {
        os << *elem;
        //@TODO TRB POINTER?
    }
    return os;
}

class Meniu {
private:
    vector<shared_ptr<Dezinfectant>> stoc_dez;
    vector<shared_ptr<Masca>> stoc_msc;
    vector<Achizitie> achizitii;
    static Meniu *instanta;

    Meniu() = default;

    Meniu(const Meniu &m) = default;

    Meniu &operator=(const Meniu &m) = default;

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

    ~Meniu() {};

    void listeazaOptiuni() {
        cout << "1.Adauga dezinfectant.\n";
        cout << "2.Adauga masca.\n";
        cout << "3.Adauga achizitie.\n";
        cout << "4.Afiseaza dezinfectantul cel mai eficient.\n";
        cout << "5.Calculeaza venitul dintr-o luna.\n";
        cout << "6.Calculeaza venitul obtinut din mastile chirurgicale cu model.\n";
        cout << "7.Modifica reteta unui dezinfectant.\n";
        cout << "8.Afiseaza cel mai fidel client.\n";
        cout << "9.Afiseaza ziua cu cele mai slabe venituri.\n";
        cout << "10.Calculeaza TVA pentru un anumit an.\n";
        cout << "11.STOP!";
    }

    void mainLoop() {
        int alegere;
        while (true) {
            cout << "Alegeti una dintre optiunile de mai jos:\n";
            listeazaOptiuni();
            cout << "Alegerea facuta:";
            try {
                cin >> alegere;
                cin.get();
                if (alegere < 0 || alegere > 10)
                    throw string("Optiune gresita!");
                else {
                    if (alegere == 1) {
                        adaugDez();
                    } else if (alegere == 2) {
                        adaugMsc();
                    } else if (alegere == 3) {
                        adaugAchi();
                    } else if (alegere == 4) {
                        afisDezEficient();
                    } else if (alegere == 5) {
                        calcVenitLuna();
                    } else if (alegere == 6) {
                        calcVenitMasticuModel();
                    } else if (alegere == 7) {
                        modifReteta();
                    } else if (alegere == 8) {
                        afisClient();
                    } else if (alegere == 9) {
                        badDay();
                    } else if (alegere == 10) {
                        calcTVA();
                    } else if (alegere == 11) break;
                }
            }
            catch (string error) {
                cout << error << '\n';
            }
        }
    }

    void adaugDez();

    void adaugMsc();

    void adaugAchi();

    void afisDezEficient();

    void calcVenitLuna();

    void calcVenitMasticuModel();

    void modifReteta();

    void afisClient();

    void badDay();

    void calcTVA();
};

void Meniu::adaugDez() {
    cout << "Alegeti tipul dezinfectantului:\n";
    cout << "1.Contra Bacterii.\n2.Contra Fungi.\n3.Contra virusi.\n4.Contra tuturor.\n";
    int optiune;
    cout << "Optiunea:";
    cin >> optiune;
    cin.get();
    shared_ptr<Dezinfectant> dezinfectant;
    if (optiune == 1) {
        dezinfectant = make_shared<Bacterii>();
    } else if (optiune == 2) {
        dezinfectant = make_shared<Fungi>();
    } else if (optiune == 3) {
        dezinfectant = make_shared<Virusi>();
    } else if (optiune == 4) {
        dezinfectant = make_shared<ALL>();
    }
    cin >> *dezinfectant;
    stoc_dez.push_back(dezinfectant);
}

void Meniu::adaugMsc() {
    cout << "Alegeti tipul mastii:\n";
    cout << "1.Chirurgicala.\n2.Policarbonata.\n";
    cout << "Optiunea aleasa:";
    int optiune;
    cin >> optiune;
    cin.get();
    shared_ptr<Masca> msc;
    if (optiune == 1) {
        msc = make_shared<MascaChirugicala>();
    }
    if (optiune == 2) {
        msc = make_shared<MascaPoli>();
    }
    cin >> *msc;
    stoc_msc.push_back(msc);
}


void Meniu::adaugAchi() {
    Achizitie achizitie;
    cin >> achizitie;
    achizitii.push_back(achizitie);
}

void Meniu::afisDezEficient() {
    double max = 0;
    int poz;
    for (int i = 0; i < stoc_dez.size(); ++i) {
        if (stoc_dez[i]->getEficienta() > max) {
            max = stoc_dez[i]->getEficienta();
            poz = i;
        }
    }
    cout << "Cel mai eficient dezinfectant este:\n";
    cout << stoc_dez[poz];
}

void Meniu::calcVenitLuna() {
    cout << "Luna pe care vrem sa o calculam:";
    int luna;
    cin >> luna;
    cin.get();
    double suma = 0;
    for (int i = 0; i < achizitii.size(); ++i) {
        if (achizitii[i].getData().getLuna() == luna) {
            suma += achizitii[i].getTotal();
        }
    }
    cout << "Venitul in luna " << luna << "a fost " << suma << ".\n";
}

void Meniu::calcVenitMasticuModel() {
    double venit = 0;
    for (int i = 0; i < achizitii.size(); ++i) {
//        @TODO
    }
    cout << "Venitul din mastile chirurgicale este " << venit << ".\n";
}

void Meniu::modifReteta() {

}

void Meniu::afisClient() {

}

void Meniu::badDay() {

}

void Meniu::calcTVA() {

}

Meniu *Meniu::instanta = nullptr;


int main() {

    Meniu *meniu = meniu->getInstanta();
    meniu->mainLoop();
    meniu->deleteInstanta();

    return 0;
}
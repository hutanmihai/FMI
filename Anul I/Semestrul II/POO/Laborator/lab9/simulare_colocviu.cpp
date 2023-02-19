#include <bits/stdc++.h>

#include "util/IoBase.h"

using namespace std;

class Malware : public IoBase {
protected:
    double rating_impact;
    int zi, luna, an;
    string nume, metoda;
    vector<string> registrii;
public:
    Malware();

    Malware(int zi, int luna, int an, const string &nume, const string &metoda,
            const vector<string> &registrii);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    double getRatingImpact() const;

    void setRatingImpact(double ratingImpact);

    int getZi() const;

    void setZi(int zi);

    int getLuna() const;

    void setLuna(int luna);

    int getAn() const;

    void setAn(int an);

    const string &getNume() const;

    void setNume(const string &nume);

    const string &getMetoda() const;

    void setMetoda(const string &metoda);

    const vector<string> &getRegistrii() const;

    void setRegistrii(const vector<string> &registrii);

    virtual ~Malware();


    virtual int calculRating() {
        for (string registru: registrii) {
            if (registru == "HKLM-run" || registru == "HKCU-run") rating_impact += 20;
        }
        return rating_impact;
    };
};

Malware::Malware() {}

Malware::Malware(int zi, int luna, int an, const string &nume, const string &metoda,
                 const vector<string> &registrii) : rating_impact(0), zi(zi), luna(luna), an(an), nume(nume),
                                                    metoda(metoda), registrii(registrii) {}


istream &Malware::read(istream &is) {
    IoBase::read(is);
    cout << "Data infectarii:" << '\n';
    cout << "Ziua:";
    is >> zi;
    cout << "Luna:";
    is >> luna;
    cout << "Anul:";
    is >> an;
    cout << "Numele Malwareului:";
    cin.ignore();
    getline(is, nume);
    cout << "Metoda de infectare:";
    getline(is, metoda);
    cout << "Numarul registrilor infectati:";
    int n;
    cin >> n;
    cin.ignore();
    string nume_registru;
    for (int i = 0; i < n; ++i) {
        cout << "Numele registrului infectat " << i + 1 << ':';
        getline(is, nume_registru);
        registrii.push_back(nume_registru);
    }
    return is;
}

ostream &Malware::write(ostream &os) const {
    IoBase::write(os);
    os << "Data infectarii este:" << '\n';
    os << "Ziua: " << zi << '\n';
    os << "Luna: " << luna << '\n';
    os << "Anul: " << an << '\n';
    os << "Numele Malwareului este: " << nume << '\n';
    os << "Metoda de infectare este: " << metoda << '\n';
    os << "Numarul registrilor infectati: " << registrii.size() << '\n';
    os << "Registrii infectati sunt:\n";
    for (int i = 0; i < registrii.size(); ++i) {
        cout << "Numele registrului infectat " << i + 1 << "este : " << registrii[i] << '\n';
    }
    return os;
}

double Malware::getRatingImpact() const {
    return rating_impact;
}

void Malware::setRatingImpact(double ratingImpact) {
    rating_impact = ratingImpact;
}

int Malware::getZi() const {
    return zi;
}

void Malware::setZi(int zi) {
    Malware::zi = zi;
}

int Malware::getLuna() const {
    return luna;
}

void Malware::setLuna(int luna) {
    Malware::luna = luna;
}

int Malware::getAn() const {
    return an;
}

void Malware::setAn(int an) {
    Malware::an = an;
}

const string &Malware::getNume() const {
    return nume;
}

void Malware::setNume(const string &nume) {
    Malware::nume = nume;
}

const string &Malware::getMetoda() const {
    return metoda;
}

void Malware::setMetoda(const string &metoda) {
    Malware::metoda = metoda;
}

const vector<string> &Malware::getRegistrii() const {
    return registrii;
}

void Malware::setRegistrii(const vector<string> &registrii) {
    Malware::registrii = registrii;
}

Malware::~Malware() {

}

class Rootkit : public virtual Malware {
protected:
    vector<string> importuri;
    vector<string> semnificative;
public:
    Rootkit();

    Rootkit(int zi, int luna, int an, const string &nume, const string &metoda, const vector<string> &registrii,
            const vector<string> &importuri, const vector<string> &semnificative);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int calculRating() override;

    const vector<string> &getImporturi() const;

    void setImporturi(const vector<string> &importuri);

    const vector<string> &getSemnificative() const;

    void setSemnificative(const vector<string> &semnificative);

};

Rootkit::Rootkit() {}

Rootkit::Rootkit(int zi, int luna, int an, const string &nume, const string &metoda, const vector<string> &registrii,
                 const vector<string> &importuri, const vector<string> &semnificative) : Malware(zi, luna, an, nume,
                                                                                                 metoda, registrii),
                                                                                         importuri(importuri),
                                                                                         semnificative(semnificative) {}

istream &Rootkit::read(istream &is) {
    Malware::read(is);
    cout << "Numarul importurilor (fisiere de tip .dll):";
    int n;
    cin >> n;
    string fisier;
    cin.ignore();
    for (int i = 0; i < n; ++i) {
        cout << "Numele fisierului .dll importat cu numarul " << i + 1 << ":";
        getline(is, fisier);
        importuri.push_back(fisier);
    }
    cout << "Numarul string-urilor semnificative:";
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Stringul semnificativ numarul " << i + 1 << ":";
        cin.ignore();
        getline(is, fisier);
        semnificative.push_back(fisier);
    }
    return is;
}

ostream &Rootkit::write(ostream &os) const {
    Malware::write(os);
    os << "Numarul importurilor (fisiere de tip .dll) este: " << importuri.size() << '\n';
    for (int i = 0; i < importuri.size(); ++i) {
        os << "Numele fisierului .dll importat cu numarul " << i + 1 << " este: " << importuri[i] << '\n';
    }
    os << "Numarul string-urilor semnificative este: " << semnificative.size() << '\n';
    for (int i = 0; i < semnificative.size(); ++i) {
        os << "Stringul semnificativ cu numarul " << i + 1 << " este: " << semnificative[i] << '\n';
    }
    return os;
}

int Rootkit::calculRating() {
    Malware::calculRating();
    for (string cuvant: importuri) {
        if (cuvant == "System Service Descriptor Table" || cuvant == "SSDT" || cuvant == "NtCreateFile")
            rating_impact += 100;
    }
    for (string cuvant: semnificative) {
        if (cuvant == "ntoskrnl.exe") rating_impact *= 2;
    }
    return rating_impact;
}

const vector<string> &Rootkit::getImporturi() const {
    return importuri;
}

void Rootkit::setImporturi(const vector<string> &importuri) {
    Rootkit::importuri = importuri;
}

const vector<string> &Rootkit::getSemnificative() const {
    return semnificative;
}

void Rootkit::setSemnificative(const vector<string> &semnificative) {
    Rootkit::semnificative = semnificative;
}

class Keylogger : public virtual Malware {
protected:
    vector<string> functii;
    vector<string> taste;
public:
    Keylogger();

    Keylogger(int zi, int luna, int an, const string &nume, const string &metoda, const vector<string> &registrii,
              const vector<string> &functii, const vector<string> &taste);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int calculRating() override;

    const vector<string> &getFunctii() const;

    void setFunctii(const vector<string> &functii);

    const vector<string> &getTaste() const;

    void setTaste(const vector<string> &taste);

};

Keylogger::Keylogger() {}

Keylogger::Keylogger(int zi, int luna, int an, const string &nume, const string &metoda,
                     const vector<string> &registrii, const vector<string> &functii, const vector<string> &taste)
        : Malware(zi, luna, an, nume, metoda, registrii), functii(functii), taste(taste) {}

istream &Keylogger::read(istream &is) {
    Malware::read(is);
    cout << "Numarul functiilor folosite:";
    int n;
    cin >> n;
    string nume;
    cin.ignore();
    for (int i = 0; i < n; ++i) {
        cout << "Numele functiei folosite cu numarul " << i + 1 << ":";
        getline(is, nume);
        functii.push_back(nume);
    }
    cout << "Numarul tastelor speciale:";
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Tasta speciala numarul " << i + 1 << ":";
        cin.ignore();
        getline(is, nume);
        taste.push_back(nume);
    }
    return is;
}

ostream &Keylogger::write(ostream &os) const {
    Malware::write(os);
    os << "Numarul functiilor folosite este: " << functii.size() << '\n';
    for (int i = 0; i < functii.size(); ++i) {
        os << "Numele functiei folosite cu numarul " << i + 1 << " este: " << functii[i] << '\n';
    }
    os << "Numarul tastelor speciale este: " << taste.size() << '\n';
    for (int i = 0; i < taste.size(); ++i) {
        os << "Tasta speciala numarul: " << i + 1 << " este: " << taste[i] << '\n';
    }
    return os;
}

int Keylogger::calculRating() {
    Malware::calculRating();
    for (string cuvant: taste) {
        if (cuvant == "[Up]" || cuvant == "[Num Lock]" || cuvant == "[Down]" || cuvant == "[Right]" ||
            cuvant == "[UP]" || cuvant == "[Left]" || cuvant == "[PageDown]")
            rating_impact += 10;
    }
    for (string cuvant: functii) {
        if (cuvant == "CreateFileW" || cuvant == "OpenProcess" || cuvant == "ReadFile" || cuvant == "WriteFile" ||
            cuvant == "RegisterHotKey" || cuvant == "SetWindowsHookEx")
            rating_impact += 30;
    }
    return rating_impact;
}

const vector<string> &Keylogger::getFunctii() const {
    return functii;
}

void Keylogger::setFunctii(const vector<string> &functii) {
    Keylogger::functii = functii;
}

const vector<string> &Keylogger::getTaste() const {
    return taste;
}

void Keylogger::setTaste(const vector<string> &taste) {
    Keylogger::taste = taste;
}

class Kernel_Keylogger : public virtual Rootkit, public virtual Keylogger {
private:
    bool ascunde_fisiere, ascunde_registrii;
public:
    Kernel_Keylogger();

    Kernel_Keylogger(int zi, int luna, int an, const string &nume, const string &metoda,
                     const vector<string> &registrii, const vector<string> &importuri,
                     const vector<string> &semnificative, const vector<string> &functii,
                     const vector<string> &taste, bool ascunde_fisere, bool ascunde_registrii) : Rootkit(zi, luna, an,
                                                                                                         nume, metoda,
                                                                                                         registrii,
                                                                                                         importuri,
                                                                                                         semnificative),
                                                                                                 Keylogger(zi, luna, an,
                                                                                                           nume, metoda,
                                                                                                           registrii,
                                                                                                           functii,
                                                                                                           taste),
                                                                                                 ascunde_fisiere(
                                                                                                         ascunde_fisere),
                                                                                                 ascunde_registrii(
                                                                                                         ascunde_registrii) {}

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int calculRating() override;

    bool isAscundeFisiere() const;

    void setAscundeFisiere(bool ascundeFisiere);

    bool isAscundeRegistrii() const;

    void setAscundeRegistrii(bool ascundeRegistrii);

};

Kernel_Keylogger::Kernel_Keylogger() {}

istream &Kernel_Keylogger::read(istream &is) {
    Malware::read(is);
    cout << "Numarul functiilor folosite:";
    int n;
    cin >> n;
    string nume;
    cin.ignore();
    for (int i = 0; i < n; ++i) {
        cout << "Numele functiei folosite cu numarul " << i + 1 << ":";
        getline(is, nume);
        functii.push_back(nume);
    }
    cout << "Numarul tastelor speciale:";
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; ++i) {
        cout << "Tasta speciala numarul " << i + 1 << ":";
        getline(is, nume);
        taste.push_back(nume);
    }
    cout << "Numarul importurilor (fisiere de tip .dll):";
    cin >> n;
    string fisier;
    for (int i = 0; i < n; ++i) {
        cout << "Numele fisierului .dll importat cu numarul " << i + 1 << ":";
        cin.ignore();
        getline(is, fisier);
        importuri.push_back(fisier);
    }
    cout << "Numarul string-urilor semnificative:";
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Stringul semnificativ numarul " << i + 1 << ":";
        cin.ignore();
        getline(is, fisier);
        semnificative.push_back(fisier);
    }
    cout << "Ascunde fisiere?\n";
    cout << "1.DA\n2.NU\n";
    cout << "Introduceti numarul alegerii facute:";
    cin >> n;
    if (n == 1) {
        ascunde_fisiere = true;
    } else ascunde_fisiere = false;
    cout << "Ascunde registrii?\n";
    cout << "1.DA\n2.NU\n";
    cout << "Introduceti numarul alegerii facute:";
    cin >> n;
    if (n == 1) {
        ascunde_registrii = true;
    } else ascunde_registrii = false;
    return is;
}

ostream &Kernel_Keylogger::write(ostream &os) const {
    Malware::write(os);
    os << "Numarul functiilor folosite este: " << functii.size() << '\n';
    for (int i = 0; i < functii.size(); ++i) {
        os << "Numele functiei folosite cu numarul " << i + 1 << " este: " << functii[i] << '\n';
    }
    os << "Numarul tastelor speciale este: " << taste.size() << '\n';
    for (int i = 0; i < taste.size(); ++i) {
        os << "Tasta speciala numarul: " << i + 1 << " este: " << taste[i] << '\n';
    }
    os << "Numarul importurilor (fisiere de tip .dll) este: " << importuri.size() << '\n';
    for (int i = 0; i < importuri.size(); ++i) {
        os << "Numele fisierului .dll importat cu numarul " << i + 1 << " este: " << importuri[i] << '\n';
    }
    os << "Numarul string-urilor semnificative este: " << semnificative.size() << '\n';
    for (int i = 0; i < semnificative.size(); ++i) {
        os << "Stringul semnificativ cu numarul " << i + 1 << " este: " << semnificative[i] << '\n';
    }
    if (ascunde_fisiere == true) {
        os << "Kernel-Keylogger-ul ascunde fisiere!\n";
    } else os << "Kernel-Keylogger-ul NU ascunde fisiere!\n";
    if (ascunde_registrii == true) {
        os << "Kernel-Keylogger-ul ascunde registrii!\n";
    } else os << "Kernel-Keylogger-ul NU ascunde registrii!\n";
    return os;
}

int Kernel_Keylogger::calculRating() {
    Rootkit::calculRating();
    Keylogger::calculRating();
    //SE DUBLA APELAREA FUNCTIEI CALCUL RATING DIN CLASA DE BAZA MALWARE ASA CA O SCADEM O DATA
    for (string registru: registrii) {
        if (registru == "HKLM-run" || registru == "HKCU-run") rating_impact -= 20;
    }
    if (ascunde_fisiere == 1) {
        rating_impact += 20;
    }
    if (ascunde_registrii == 1) {
        rating_impact += 30;
    }
    return rating_impact;
}

bool Kernel_Keylogger::isAscundeFisiere() const {
    return ascunde_fisiere;
}

void Kernel_Keylogger::setAscundeFisiere(bool ascundeFisiere) {
    ascunde_fisiere = ascundeFisiere;
}

bool Kernel_Keylogger::isAscundeRegistrii() const {
    return ascunde_registrii;
}

void Kernel_Keylogger::setAscundeRegistrii(bool ascundeRegistrii) {
    ascunde_registrii = ascundeRegistrii;
}

class Ransomware : public Malware {
private:
    int rating_criptare;
    double rating_obfuscare;
public:
    Ransomware();

    Ransomware(int zi, int luna, int an, const string &nume, const string &metoda, const vector<string> &registrii,
               int ratingCriptare, double ratingObfuscare);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    int calculRating() override;

    int getRatingCriptare() const;

    void setRatingCriptare(int ratingCriptare);

    double getRatingObfuscare() const;

    void setRatingObfuscare(double ratingObfuscare);
};

Ransomware::Ransomware() {}

Ransomware::Ransomware(int zi, int luna, int an, const string &nume, const string &metoda,
                       const vector<string> &registrii, int ratingCriptare, double ratingObfuscare) : Malware(zi, luna,
                                                                                                              an, nume,
                                                                                                              metoda,
                                                                                                              registrii),
                                                                                                      rating_criptare(
                                                                                                              ratingCriptare),
                                                                                                      rating_obfuscare(
                                                                                                              ratingObfuscare) {}

istream &Ransomware::read(istream &is) {
    Malware::read(is);
    cout << "Rating-ul criptarii:";
    is >> rating_criptare;
    cout << "Rating-ul obfuscarii:";
    is >> rating_obfuscare;
    return is;
}

ostream &Ransomware::write(ostream &os) const {
    Malware::write(os);
    os << "Rating-ul criptarii este: " << rating_criptare << ", iar rating-ul obfuscarii este: " << rating_obfuscare
       << '\n';
    return os;
}

int Ransomware::calculRating() {
    Malware::calculRating();
    rating_impact += rating_obfuscare;
    rating_impact += rating_criptare;
    return rating_impact;
}

int Ransomware::getRatingCriptare() const {
    return rating_criptare;
}

void Ransomware::setRatingCriptare(int ratingCriptare) {
    rating_criptare = ratingCriptare;
}

double Ransomware::getRatingObfuscare() const {
    return rating_obfuscare;
}

void Ransomware::setRatingObfuscare(double ratingObfuscare) {
    rating_obfuscare = ratingObfuscare;
}

class Computer : public IoBase {
private:
    static int id;
    int cod;
    double rating_final;
    vector<shared_ptr<Malware>> lista_malware;
public:
    Computer();

    Computer(double ratingFinal, const vector<shared_ptr<Malware>> &listaMalware);

    Computer(const vector<shared_ptr<Malware>> &listaMalware);

    istream &read(istream &is) override;

    ostream &write(ostream &os) const override;

    double getRatingFinal() const;

    static int getId();

    static void setId(int id);

    int getCod() const;

    void setCod(int cod);

    void setRatingFinal(double ratingFinal);

    const vector<shared_ptr<Malware>> &getListaMalware() const;

    void setListaMalware(const vector<shared_ptr<Malware>> &listaMalware);

};

int Computer::id = 0;

Computer::Computer() {}

Computer::Computer(double ratingFinal, const vector<shared_ptr<Malware>> &listaMalware) : rating_final(ratingFinal),

                                                                                          lista_malware(listaMalware) {}

Computer::Computer(const vector<shared_ptr<Malware>> &listaMalware) : lista_malware(listaMalware) {
    ++id;
    cod = Computer::id;
    rating_final = 0;
    for (int i = 0; i < lista_malware.size(); ++i) {
        rating_final += lista_malware[i]->calculRating();
    }
}

istream &Computer::read(istream &is) {
    IoBase::read(is);
    cout << "Numarul de malweri ce afecteaza acest calculator:";
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cout << "Alegeti tipul de malware:\n";
        cout << "1.Rootkit.\n2.Keylogger.\n3.Kernel-Keylogger.\n4.Ransomware.";
        cout << "Introduceti alegerea facuta:";
        int m;
        cin >> m;
        shared_ptr<Malware> malware;
        if (m == 1) {
            malware = make_shared<Rootkit>();
        } else if (m == 2) {
            malware = make_shared<Keylogger>();
        } else if (m == 3) {
            malware = make_shared<Kernel_Keylogger>();
        } else if (m == 4) {
            malware = make_shared<Ransomware>();
        }
        is >> *malware;
        lista_malware.push_back(malware);
    }
    return is;
}

ostream &Computer::write(ostream &os) const {
    IoBase::write(os);
    os << "ID-ul calculatorului este: " << cod << '\n';
    os << "Rating-ul final este: " << rating_final << '\n';
    os << "Malweri: \n";
    for (int i = 0; i < lista_malware.size(); ++i) {
        os << *lista_malware[i] << '\n';
    }
    return os;
}

const vector<shared_ptr<Malware>> &Computer::getListaMalware() const {
    return lista_malware;
}

double Computer::getRatingFinal() const {
    return rating_final;
}

int Computer::getId() {
    return id;
}

void Computer::setId(int id) {
    Computer::id = id;
}

int Computer::getCod() const {
    return cod;
}

void Computer::setCod(int cod) {
    Computer::cod = cod;
}

void Computer::setRatingFinal(double ratingFinal) {
    rating_final = ratingFinal;
}

void Computer::setListaMalware(const vector<shared_ptr<Malware>> &listaMalware) {
    lista_malware = listaMalware;
}

class Meniu {
private:
    vector<Computer> computerele_firmei;
public:
    void listeazaOptiuni() {
        cout << "1.Afisarea informatiilor pentru fiecare calculator.\n";
        cout << "2.Afișarea informațiilor pentru fiecare calculator fiind ordonate după ratingul final.\n";
        cout << "3.Afișarea primelor k calculatoare ordonate după ratingul final.\n";
        cout << "4.Afisarea procentului de computere infectate din firmă.\n";
        cout << "5.OPRIRE PROGRAM\n";
    }

    int alegeOptiune() {
        cout << "Alegeti una dintre optiunile de mai jos:\n";
        int alegere;
        listeazaOptiuni();
        cout << "Alegerea facuta:";
        cin >> alegere;
        return alegere;
    }

    void mainLoop() {
        cout << "Numarul de calculatoare:";
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            Computer calculator;
            cin >> calculator;
            computerele_firmei.push_back(Computer(calculator.getListaMalware()));
        }
        while (true) {
            int alegere = alegeOptiune();
            if (alegere == 1) {
                afisInfomartii();
            } else if (alegere == 2) {
                afisInformatiiOrd();
            } else if (alegere == 3) {
                afisPrimeleK();
            } else if (alegere == 4) {
                afisProcent();
            } else if (alegere == 5) break;
        }
    }

    void afisInfomartii();

    void afisInformatiiOrd();

    void afisPrimeleK();

    void afisProcent();
};

bool comparare(const Computer &c1, const Computer &c2) {
    return c1.getRatingFinal() < c2.getRatingFinal();
}

void Meniu::afisInfomartii() {
    for (int i = 0; i < computerele_firmei.size(); ++i) {
        cout << computerele_firmei[i] << '\n';
    }
    cout << '\n';
}

void Meniu::afisInformatiiOrd() {
    sort(computerele_firmei.begin(), computerele_firmei.end(), comparare);
    afisInfomartii();
    cout << '\n';
}

void Meniu::afisPrimeleK() {
    sort(computerele_firmei.begin(), computerele_firmei.end(), comparare);
    cout << "K=";
    int k;
    cin >> k;
    for (int i = 0; i < k; ++i) {
        cout << computerele_firmei[i];
    }
    cout << '\n';
}

void Meniu::afisProcent() {
    double procent;
    int nr = 0;
    for (int i = 0; i < computerele_firmei.size(); ++i) {
        if (computerele_firmei[i].getRatingFinal() != 0)
            ++nr;
    }
    if (computerele_firmei.size()) {
        procent = 100.0 * (double(nr) / double(computerele_firmei.size()));
        cout << "Procentul calculatoarelor infectate este: " << procent << '\n';
    } else cout << "Nu exista calculatoare!\n";
}

int main() {
    Meniu meniu;
    meniu.mainLoop();
    return 0;
}

//2
//2
//1
//1
//1
//1
//ATAC
//ATAC2
//2
//HKLM-run
//HKCU-run
//1
//SSDT
//1
//ntoskrnl.exe
//2
//1
//2
//3
//BOMBA
//BOMBA2
//0
//1
//ReadFile
//1
//[UP]
//1
//3
//3
//4
//5
//BUM
//BUM2
//0
//0
//1
//[UP]
//1
//SSDT
//0
//1
//1


//CALCULATOR ID 1 AR TRB SA AIBA RATING FINAL 320 IAR ID 2 RATING 160

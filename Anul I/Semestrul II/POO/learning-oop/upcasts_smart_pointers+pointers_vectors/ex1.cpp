#include <bits/stdc++.h>
#include "util/IoBase.h"
using namespace std;

class Fruct : public IoBase {

protected:
    string nume;
    string soi;

public:
    Fruct() {}

    Fruct(const string &nume, const string &soi) : nume(nume), soi(soi) {}

    istream &read(istream &is) override {
        cout << "Numele fructului: ";
        cin.get();
        is>>nume;
        cout<< "Soiul fructului: ";
        cin.get();
        is>>soi;
        return is;
    }

    ostream &write(ostream &os) const override {
        cout << "Numele fructului este: ";
        os << nume << '\n';
        cout << "Soiul fructului este: ";
        os << soi << '\n';
        return os;
    }
};

class Suc : public IoBase{

protected:
    int litri;

public:
    Suc() {}

    Suc(int litri) : litri(litri) {}

    istream &read(istream &is) override {
        cout << "Litri de suc: ";
        cin.get();
        is >> litri;
        return is;
    }

    ostream &write(ostream &os) const override {
        cout << "Numarul de litri de suc este: ";
        os << litri << '\n';
        return os;
    }

    virtual int getCantitate(){
        return litri;
    }
};

class SucuriSimple : public Suc {

private:
    Fruct fruct;

public:
    SucuriSimple() {}

    SucuriSimple(int litri, const Fruct &fruct) : Suc(litri), fruct(fruct) {}

    istream &read(istream &is) override {
        Suc::read(is);
        cout << "Fructul folosit in sucul simplu: " << '\n';
        is >> fruct;
        return is;
    }

    ostream &write(ostream &os) const override {
        Suc::write(os);
        cout << "Fructul folosit in sucul simplu este: " << '\n';
        os << fruct << '\n';
        return os;
    }
};

class SucuriMixte : public Suc {

protected:
    vector<Fruct> fructe;

public:
    SucuriMixte() {}

    SucuriMixte(int litri, const vector<Fruct> &fructe) : Suc(litri), fructe(fructe) {}

    istream &read(istream &is) override {
        Suc::read(is);
        cout << "Numarul de fructe folosite in mix: ";
        int n;
        cin >> n;
        cout << '\n';
        for (int i = 0; i < n; ++i) {
            cout << "Fructul " << i+1 << ": ";
            Fruct fructcurent;
            is >> fructcurent;
            fructe.push_back(fructcurent);
            cout << '\n';
        }
        return is;
    }

    ostream &write(ostream &os) const override {
        Suc::write(os);
        os << "Fructele folosite in mix sunt: " << '\n';
        for (auto fruct : fructe){
            os << fruct << ' ';
        }
        os << '\n';
        return os;
    }
};

class SucuriGheata : public SucuriMixte {

private:
    int gheata;

public:
    SucuriGheata() {}

    SucuriGheata(int litri, const vector<Fruct> &fructe, int gheata) : SucuriMixte(litri, fructe), gheata(gheata) {}

    istream &read(istream &is) override {
        SucuriMixte::read(is);
        cout << "Cantitatea de gheata: ";
        is >> gheata;
        return is;
    }

    ostream &write(ostream &os) const override {
        SucuriMixte::write(os);
        os << "Cantitate de gheata este: ";
        os << gheata << '\n';
        return os;
    }

    int getCantitate() override {
        return litri+gheata;
    }
};

//int getCantitate(){
//    return
//}

int main(){
    vector<shared_ptr<Suc> > stock = {
            make_shared<SucuriSimple>(
                    SucuriSimple(550, Fruct("Apple", "Granny Smith"))
            ),
            make_shared<SucuriMixte>(
                    SucuriMixte(
                            560,
                            {
                                    Fruct("Apple", "Granny Smith"),
                                    Fruct("Banana", "Musa balbisiana"),
                            }
                    )
            ),
            make_shared<SucuriGheata>(
                    SucuriGheata(
                            560,
                            {
                                    Fruct("Apple", "Granny Smith"),
                                    Fruct("Banana", "Musa balbisiana"),
                            },
                            150
                    )
            ),
    };

    for (auto suc : stock) {
        cout << suc -> getCantitate() << ' ';
    }


    return 0;
}



#include <bits/stdc++.h>
#include "util/IoBase.h"
using namespace std;

class Participant : public IoBase{

protected:
    string CNP;

public:
    Participant() {}

    Participant(const string &cnp) : CNP(cnp) {}

    istream &read(istream &is) override {
        cout << "CNP-ul participantului: ";
        is >> CNP;
    }

    ostream &write(ostream &os) const override {
        os << "CNP-ul participantului este: ";
        os << CNP;
    }
};

class Elev : public Participant {

private:
    string limbaj;

public:
    Elev() {}

    Elev(const string &cnp, const string &limbaj) : Participant(cnp), limbaj(limbaj) {}

    istream &read(istream &is) override {
        Participant::read(is);
        cout << "Limbajul de programare folosit de elev: ";
        is >> limbaj;
    }

    ostream &write(ostream &os) const override {
        Participant::write(os);
        os << "Limbajul de programare folosit de elev este: ";
        os << limbaj;
        os << '\n';
    }
};

class Superiori : public Participant {

protected:
    vector<string> limbaje;

public:
    Superiori() {}

    Superiori(const string &cnp, const vector<string> &limbaje) : Participant(cnp), limbaje(limbaje) {}

    istream &read(istream &is) override {
        Participant::read(is);
        int n;
        cout << "Numarul de limbaje de programare: ";
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cout << "Limbajul de programare " << i+1 << " :";
            string limbaj_curent;
            is >> limbaj_curent;
            limbaje.push_back(limbaj_curent);
        }
    }

    ostream &write(ostream &os) const override {
        Participant::write(os);
        os << "Limbajele de programare folosite de participant sunt: ";
        for (auto limbaj : limbaje){
            os << limbaj << ' ';
        }
        os << '\n';
    }
};

class Student : public Superiori {

private:
    int an;

public:
    Student() {}

    Student(const string &cnp, const vector<string> &limbaje, int an) : Superiori(cnp, limbaje), an(an) {}

    istream &read(istream &is) override {
        Superiori::read(is);
        cout << "Anul de studiu: ";
        is >> an;
    }

    ostream &write(ostream &os) const override {
        Superiori::write(os);
        cout << "Anul de studiu este: ";
        os << an;
    }
};

class Profesional : public Superiori {

private:
    string nume_firma;

public:
    Profesional() {}

    Profesional(const string &cnp, const vector<string> &limbaje, const string &numeFirma) : Superiori(cnp, limbaje),nume_firma(numeFirma) {}

    istream &read(istream &is) override {
        Superiori::read(is);
        cout << "Numele firmei la care lucreaza: ";
        is >> nume_firma;
    }

    ostream &write(ostream &os) const override {
        Superiori::write(os);
        os << "Numele firmei la care lucreaza este: ";
        os << nume_firma;
    }
};

class Echipa : public IoBase{

private:
    vector<shared_ptr<Participant>> membrii;
    string nume;
    string domeniu;
    Profesional mentor;
    int nr_maxim = 5;

public:
    Echipa() {}

    Echipa(const vector<shared_ptr<Participant>> &membrii, const string &nume, const string &domeniu,
           const Profesional &mentor) : membrii(membrii), nume(nume), domeniu(domeniu), mentor(mentor) {}

    void eliminaMembru(int index){
        membrii.erase(membrii.begin()+index);
    }

    void adaugaMembru(shared_ptr<Participant> p){
        membrii.push_back(p);
    }

    void inregistreazaNouMembru(){
        cout << "Alege tipul de membru: \n";
        cout << "1.Elev \n";
        cout << "2.Student \n";
        cout << "3.Programator profesional \n";

        int type;
        cin >> type;
        shared_ptr<Participant> newParticipant;

        if (type == 1){
            newParticipant = make_shared<Elev>();
        }
        else if (type == 2){
            newParticipant = make_shared<Student>();
        }
        else if (type == 3){
            newParticipant = make_shared<Profesional>();
        }
        else {
            cout << "INPUT GRESIT";
        }

        cin >> *newParticipant;
        membrii.push_back(newParticipant);
    }

    void modificaMentor(Profesional programator){
        mentor = programator;
    }

    int locuriLibere(){
        return nr_maxim-membrii.size();
    }
};

int main(){

    return 0;
}
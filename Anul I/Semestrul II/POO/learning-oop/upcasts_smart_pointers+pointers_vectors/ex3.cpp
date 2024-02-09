#include <bits/stdc++.h>
#include "util/IoBase.h"

using namespace std;

class Employee : public IoBase {

protected:
    int salariu;
    string functia;
    string nume;
    int ani_experienta;

public:
    Employee() {}

    Employee(int salariu, const string &functia, const string &nume, int aniExperienta) : salariu(salariu),
                                                                                          functia(functia), nume(nume),
                                                                                          ani_experienta(
                                                                                                  aniExperienta) {}

    istream &read(istream &is) override {
        cout << "Numele angajatului: ";
        is >> nume;
        cout << "Functia angajatului: ";
        is >> functia;
        cout << "Salariul de baza al angajatului: ";
        is >> salariu;
        cout << "Anii de experienta ai angajatului: ";
        is >> ani_experienta;
        return is;
    }

    ostream &write(ostream &os) const override {
        cout << "Numele angajatului este: ";
        os << nume << '\n';
        cout << "Functia angajatului este: ";
        os << functia << '\n';
        cout << "Salariul de baza al angajatului este: ";
        os << salariu << '\n';
        cout << "Anii de experienta ai angajatului este: ";
        os << ani_experienta << '\n';
        return os;
    }

    int getAniExperienta() {
        return ani_experienta;
    }

    virtual double salariuNet() {
        return salariu / 2;
    };
};

class Programmer : public Employee {

protected:
    int ore_extra;

public:
    Programmer() {}

    Programmer(int salariu, const string &functia, const string &nume, int aniExperienta, int oreExtra) : Employee(
            salariu, functia, nume, aniExperienta), ore_extra(oreExtra) {}

    istream &read(istream &is) override {
        Employee::read(is);
        cout << "Numarul de ore extra: ";
        is >> ore_extra;
        return is;
    }

    ostream &write(ostream &os) const override {
        Employee::write(os);
        os << "Numarul de ore extra este: " << ore_extra << '\n';
        return os;
    }

    double salariuNet() override {
        double bonus_income = 2.5 * salariu / 160;
        return salariu + ore_extra * bonus_income;
    }
};

class FullStackDeveloper : public Programmer {

public:
    FullStackDeveloper() {}

    FullStackDeveloper(int salariu, const string &functia, const string &nume, int aniExperienta, int oreExtra)
            : Programmer(salariu, functia, nume, aniExperienta, oreExtra) {}

};

class DevOps : public Programmer {

public:
    DevOps() {}

    DevOps(int salariu, const string &functia, const string &nume, int aniExperienta, int oreExtra) : Programmer(
            salariu, functia, nume, aniExperienta, oreExtra) {}

};

class Manager : public Employee {

public:
    Manager() {}

    Manager(int salariu, const string &functia, const string &nume, int aniExperienta) : Employee(salariu, functia,
                                                                                                  nume,
                                                                                                  aniExperienta) {}
};

bool testIfPossible(vector<shared_ptr<Employee>> angajati) {
    bool ani = false;
    bool fsd = false;
    bool dvo = false;
    bool mng = false;
    for (auto angajat: angajati) {
        auto *asFullstack = dynamic_cast<FullStackDeveloper *>(angajat.get());
        auto *asDevOps = dynamic_cast<DevOps *>(angajat.get());
        auto *asManager = dynamic_cast<Manager *>(angajat.get());
        if (asFullstack) {
            if (asFullstack->getAniExperienta() >= 2) {
                ani = true;
            }
            fsd = true;
        }
        if (asDevOps) {
            if (asDevOps->getAniExperienta() >= 2) {
                ani = true;
            }
            dvo = true;
        }
        if (asManager) {
            mng = true;
        }
    }
    if (ani and fsd and dvo and mng) {
        return true;
    } else return false;
}

void backtracking_numar(int k, vector<int> &st, const vector<shared_ptr<Employee>> &a, int &sum) {
    for (int i = 0; i <= 1; i++) {
        st[k] = i;
        if (k == a.size() - 1) {
            vector<shared_ptr<Employee>> angajati;
            for (int i = 0; i < a.size(); i++) {
                if (st[i] == 1) {
                    angajati.push_back(a[i]);
                }
            }
            bool ok = testIfPossible(angajati);
            if (ok) {
                for (int i = 0; i < angajati.size(); i++) {
                    cout << *angajati[i] << "\n";
                }
                cout << "Asta a fost o solutie\n";
                sum++;
            }
        } else {
            backtracking_numar(k + 1, st, a, sum);
        }
    }
};

void backtracking_echipe(int k, vector<int> &st, const vector<shared_ptr<Employee>> &a,
                         vector<vector<shared_ptr<Employee>>> &teams) {
    for (int i = 0; i <= 1; i++) {
        st[k] = i;
        if (k == a.size() - 1) {
            vector<shared_ptr<Employee>> angajati;
            for (int i = 0; i < a.size(); i++) {
                if (st[i] == 1) {
                    angajati.push_back(a[i]);
                }
            }
            bool ok = testIfPossible(angajati);
            if (ok) {
                teams.push_back(angajati);
            }
        } else {
            backtracking_echipe(k + 1, st, a, teams);
        }
    }
};

int numarulEchipelor(vector<shared_ptr<Employee>> angajati) {
    vector<int> st;
    st.resize(angajati.size());
    int sum = 0;
    backtracking_numar(0, st, angajati, sum);
    return sum;
}

vector<vector<shared_ptr<Employee>>> getListOfTeams(vector<shared_ptr<Employee>> angajati) {
    vector<int> st;
    vector<vector<shared_ptr<Employee>>> Echipe;
    st.resize(angajati.size());
    backtracking_echipe(0, st, angajati, Echipe);
    return Echipe;
}

class Team {

private:
    vector<shared_ptr<Employee>> angajati;
    float buget_maxim;

public:
    Team() {}

    Team(const vector<shared_ptr<Employee>> &angajati, float bugetMaxim) : angajati(angajati),
                                                                           buget_maxim(bugetMaxim) {}

    bool testIfPossible_method();

    int numarulEchipelor_method();

    vector<vector<shared_ptr<Employee>>> getListOfTeams_method();

    vector<Team> sortedTeams();

    int maximumTeamCount();
};

bool Team::testIfPossible_method() {
    int fsd = 0;
    int dvo = 0;
    int mng = 0;

    int fsd_cuexp = 0;
    int dvo_cuexp = 0;

    for (auto &angajat: angajati) {
        FullStackDeveloper *asFullstack = dynamic_cast<FullStackDeveloper *>(angajat.get());
        Manager *asManager = dynamic_cast<Manager *>(angajat.get());
        DevOps *asDevOp = dynamic_cast<DevOps *>(angajat.get());

        if (asFullstack) {
            if (asFullstack->getAniExperienta() >= 2) {
                fsd_cuexp++;
            }
            fsd++;
        } else if (asDevOp) {
            dvo++;
            if (asDevOp->getAniExperienta() >= 2) {
                dvo_cuexp++;
            }
        } else if (asManager) {
            mng++;
        }

    }

    if (mng >= 1 and dvo >= 1 and fsd >= 1 and (fsd_cuexp >= 1 or dvo_cuexp >= 1)) {
        return true;
    } else return false;
}

int Team::numarulEchipelor_method() {
    vector<int> st;
    st.resize(angajati.size());
    int sum = 0;
    backtracking_numar(0, st, angajati, sum);
    return sum;
}

vector<vector<shared_ptr<Employee>>> Team::getListOfTeams_method() {
    vector<int> st;
    vector<vector<shared_ptr<Employee>>> teams;
    st.resize(angajati.size());
    backtracking_echipe(0, st, angajati, teams);
    return teams;
}

vector<Team> Team::sortedTeams() {
    vector<vector<shared_ptr<Employee>>> echipe;
    echipe = getListOfTeams_method();
    vector<Team> teams;
    float sum1;
    float sum2;
    for (int i = 0; i < echipe.size() - 1; i++) {
        sum1 = 0;
        for (int j = 0; j < echipe[i].size(); j++) {
            sum1 += echipe[i][j]->salariuNet();
        }
        for (int j = i + 1; i < echipe.size(); j++) {
            sum2 = 0;
            for (int l = 0; l < echipe[j].size(); l++) {
                sum2 += echipe[j][l]->salariuNet();
            }
            if (sum1 > sum2) {
                swap(echipe[i], echipe[j]);
            }
        }
    }
    for (int i = 0; i < echipe.size(); i++) {
        Team t;
        t.angajati = echipe[i];
        float buget = 0;
        for (int j = 0; j < echipe[i].size(); i++) {
            buget += echipe[i][j]->salariuNet();
        }
        t.buget_maxim = buget;
        teams.push_back(t);
    }
    return teams;
}

int Team::maximumTeamCount() {
    vector<vector<shared_ptr<Employee>>> echipe;
    echipe = getListOfTeams_method();
    int nr_teams_budget = 0;
    for (int i = 0; i < echipe.size(); i++) {
        float local_budget = 0;
        for (int j = 0; j < echipe[i].size(); j++) {
            local_budget += echipe[i][j]->salariuNet();
        }
        if (local_budget <= buget_maxim) {
            nr_teams_budget++;
        }
    }
    return nr_teams_budget;
}

int main() {

    return 0;
}
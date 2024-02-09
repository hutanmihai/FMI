#include <bits/stdc++.h>
#include "util/IoBase.h"

using namespace std;

class BaseMenu {
protected:
    string label;

public:
    BaseMenu() {}

    BaseMenu(const string &label) : label(label) {}

    virtual void listOptions() {}

    virtual int chooseOption(int first, unsigned long long last) {}

    virtual void mainLoop() {}
};

class SimpleMenu : public BaseMenu {
private:
    vector<string> comenzi;
public:
    SimpleMenu() {}

    SimpleMenu(const string &label, const vector<string> &comenzi) : BaseMenu(label), comenzi(comenzi) {}

    void listOptions() override {
        int k;
        cout << "Comenzile posibile sunt:\n";
        for (int i = 0; i < comenzi.size(); ++i) {
            cout << i + 1 << ". " << comenzi[i] << '\n';
            k = i + 1;
        }
        cout << ++k << ". " << "Iesire\n";
    }

    int chooseOption(int first, unsigned long long int last) override {
        int alegere = -1;
        while (alegere < first || alegere > last) {
            cout << '\n';
            cout << "Alegeti un numar intre " << first << " si " << last << '\n';
            listOptions();
            cout << "Alegere:";
            cin >> alegere;
        }
        return alegere;
    }

    static void create() {
        cout << "Clasa a fost creata cu succes!\n";
    }

    static void text() {
        cout << "Text file a fost creat cu succes!\n";
    }

    static void browse() {
        cout << "Fisierul a fost deschis cu succes!\n";
    }

    void mainLoop() override {
        while (true) {
            int alegere = chooseOption(1, comenzi.size() + 1);
            if (label == "Create") {
                if (alegere == 1) {
                    create();
                } else if (alegere == 2) {
                    text();
                } else if (alegere == 3) {
                    break;
                }
            } else if (label == "Open") {
                if (alegere == 1) {
                    browse();
                } else if (alegere == 2) {
                    break;
                }
            }
        }
        cout << "======================================" << '\n' << "Submeniu inchis!\n";
    }
};

class ComposedMenu : public BaseMenu {
private:
    map<string, shared_ptr<BaseMenu>> submeniu;
    vector<string> comenzi;
public:
    ComposedMenu() {}

    ComposedMenu(const string &label, const map<string, shared_ptr<BaseMenu>> &submeniu, const vector<string> &comenzi)
            : BaseMenu(label), submeniu(submeniu), comenzi(comenzi) {}

    void listOptions() override {
        cout << "Optiunile sunt:\n";
        int i = 1;
        for (auto menu: submeniu) {
            cout << i++ << ". " << menu.first << '\n';
        }
        for (auto comanda: comenzi)
            cout << i++ << ". " << comanda << '\n';
        cout << i << ". " << "Iesire\n";
    }

    int chooseOption(int first, unsigned long long int last) override {
        int alegere = -1;
        while (alegere < first || alegere > last) {
            cout << '\n';
            cout << "Alegeti un numar intre " << first << " si " << last << '\n';
            listOptions();
            cout << "Alegere:";
            cin >> alegere;
        }
        return alegere;
    }

    void create() {
        cout << "Am deschis submeniul!\n";
        auto pars = submeniu.begin();
        pars->second->mainLoop();
    }

    void open() {
        cout << "Am deschis submeniul!\n";
        auto pars = submeniu.begin();
        advance(pars, 1);
        pars->second->mainLoop();
    }

    static void del() {
        cout << "Fisierul a fost sters cu succes!\n";
    }

    void mainLoop() override {
        while (true) {
            int alegere = chooseOption(1, submeniu.size() + comenzi.size() + 1);
            if (alegere == 1) {
                create();
            } else if (alegere == 2) {
                open();
            } else if (alegere == 3) {
                del();
            } else if (alegere == 4) {
                break;
            }
        }
        cout << "======================================" << '\n' << "Program inchis!\n";
    }
};

int main() {

    return 0;
}
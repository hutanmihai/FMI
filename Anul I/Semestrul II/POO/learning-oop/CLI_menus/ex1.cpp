#include <bits/stdc++.h>
#include "util/IoBase.h"

using namespace std;

// Vom porni de la intrebarile:
// Ce ar trebui sa faca un meniu interactiv? Ce pasi sunt necesari pentru a-l folosi.

// Orice meniu va putea:
//  * lista optiunile
//  * alege corect una dintre optiuni
//  * va putea fi rulat la infinit (=interactiv din "meniul interactiv")

class BaseMenu {
public:
    virtual void listOptions() {}

    virtual int chooseOption(int first, int last) {}

    virtual void mainLoop() {}
};

class SimpleMenu : public BaseMenu {
public:
    void listOptions() override {
        cout << "1.Adauga o noua cladire. \n";
        cout << "2.Sterge o cladire existenta. \n";
        cout << "3.Modifica o cladire. \n";
        cout << "4.Iesire. \n";
    }

    int chooseOption(int first, int last) override {
        int alegere = -1;
        while (alegere < first || alegere > last){
            cout << '\n';
            cout << "Alegeti un numar intre " << first << " si " << last << '\n';
            listOptions();
            cout << "Alegere:";
            cin >> alegere;
        }
        return alegere;
    }

    void alegere1() {
        cout << "Aici vom adauga o noua cladire." << '\n';
    }

    void alegere2() {
        cout << "Aici vom sterge una dintre cladirile existente." << '\n';
    }

    void alegere3() {
        cout << "Aici vom modifica datele uneia dintre cladirile existente." << '\n';
    }

    void mainLoop() override {
        while (true) {
            int alegere = chooseOption(1, 4);
            if (alegere == 1) {
                alegere1();
            } else if (alegere == 2) {
                alegere2();
            } else if (alegere == 3) {
                alegere3();
            } else if (alegere == 4) {
                break;
            }
        }
        cout << '\n'
             << "Programul s-a terminat cu success";
    }
};


int main() {
    SimpleMenu menu;
    menu.mainLoop(); // păstrăm codul simplu: funcția mainLoop „ruleaza” meniul la infinit.

}


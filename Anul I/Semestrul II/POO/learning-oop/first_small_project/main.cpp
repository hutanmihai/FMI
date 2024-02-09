// Spalatorie atutomata

#include <iostream>

using namespace std;

class Durata {
    int minute;
    int secunde;

public:
    Durata() {
        minute = 0;
        secunde = 0;
    }

    Durata(int _minute, int _secunde) {
        minute = _minute;
        secunde = _secunde;
    }

    int getTime() {
        int _secunde;
        _secunde = minute * 60 + secunde;
        return _secunde;
    }
};

class MasinaSpalat {
    bool liber;
    Durata timp;
    int capsule;

public:
    MasinaSpalat() {
        liber = false;
        timp = Durata();
        capsule = 0;
    }

    MasinaSpalat(bool _liber, Durata _timp, int _capsule) {
        liber = _liber;
        timp = _timp;
        capsule = _capsule;
    }

    int getCapsule() {
        return capsule;
    }

    int getTime() {
        return timp.getTime();
    }

    void decrCapsule() {
        capsule--;
    }

    void setTime(Durata _timp) {
        timp = _timp;
    }

    void setOccupied() {
        liber = false;
    }

    void setUnoccupied() {
        liber = true;
    }

    bool getOccupied() {
        return liber;
    }

    Durata getDurata(){
        return timp;
    }

    Durata compareTime(Durata _timp){
        int timp1 = _timp.getTime();
        int timp =  this-> timp.getTime();
        if (timp1 >= timp){
            return Durata(0,0);
        }
        else{
            timp -= timp1;
            int minute = timp / 60;
            int secunde = timp % 60;
            return Durata(minute,secunde);
        }
    }
};

class Spalatorie {
    int nrmasini;
    MasinaSpalat masini[5];

public:
    Spalatorie() {
        nrmasini = 0;
    }

    Spalatorie(int _nrmasini, MasinaSpalat _masini[]) {
        nrmasini = _nrmasini;
        for (int i = 0; i < nrmasini; ++i) {
            masini[i] = _masini[i];
        }
    }

    int getNumarMasini() {
        return nrmasini;
    }

    MasinaSpalat getMasina(int i) {
        return masini[i];
    }

    void listeazaMasini() {
        cout << "Spalatoria in prezent:" << endl;
        for (int i = 0; i < nrmasini; ++i) {
            if (masini[i].getOccupied() == 1 && masini[i].getCapsule() != 0) {
                cout << i << '.' << " " << "Masina este libera." << endl;
            } else if (masini[i].getOccupied() == 0 && masini[i].getCapsule() != 0) {
                int minute;
                int secunde;
                secunde = masini[i].getTime();
                minute = secunde / 60;
                secunde = secunde % 60;
                cout << i << '.' << " " << "Masina este ocupata pentru inca " << minute << ':' << secunde << '.'
                     << endl;
            } else if (masini[i].getOccupied() == 1 && masini[i].getCapsule() == 0) {
                cout << i << '.' << " " << "Masina este neutilizabila! Nu mai are capsule!" << endl;
            }
        }
    }

    void adaugaJob(int _nrmasina, Durata _timp) {
        if (masini[_nrmasina].getCapsule() == 0) {
            cout << "Masina " << _nrmasina << " nu mai are capsule" << endl;
        } else if (masini[_nrmasina].getOccupied() == 0) {
            cout << "Masina " << _nrmasina << " este ocupata!" << endl;
        } else {
            masini[_nrmasina].decrCapsule();
            masini[_nrmasina].setTime(_timp);
            masini[_nrmasina].setOccupied();
        }
    }

    void actualizeazaTimp(Durata _timp1) {
        for (int i = 0; i < nrmasini; ++i) {
            masini[i].setTime(masini[i].compareTime(_timp1));
            if (masini[i].getTime()==0) masini[i].setUnoccupied();
            else masini[i].setOccupied();
            }
        }
};

void listeazaMasiniLibere(Spalatorie spalatorie) {
    int _nrmasini = spalatorie.getNumarMasini();
    int vec[5], j = 0;
    for (int i = 0; i < _nrmasini; ++i) {
        MasinaSpalat masina = spalatorie.getMasina(i);
        if (masina.getOccupied() == 1) {
            vec[j++] = i;
        }
    }
    cout << "Urmatoarele masini de spalat sunt libere: ";
    for (int i = 0; i < j; ++i) {
        cout << vec[i] << ' ';
    }
    cout << endl;
}

int main() {
    // declararea spalatoriei
    MasinaSpalat masini[5] = {
            MasinaSpalat(true, Durata(0, 0), 3),
            MasinaSpalat(true, Durata(0, 0), 2),
            MasinaSpalat(true, Durata(0, 0), 5),
    };
    Spalatorie spalatorie(
            3,
            masini
    );

// listare initiala
    spalatorie.listeazaMasini();
    listeazaMasiniLibere(spalatorie);

    spalatorie.adaugaJob(
            1,
            Durata(1, 20)
    );
    spalatorie.listeazaMasini();

    spalatorie.actualizeazaTimp(Durata(1, 19));
    spalatorie.listeazaMasini();

    spalatorie.actualizeazaTimp(Durata(1, 0));
    spalatorie.listeazaMasini(); // metoda

// adaugam inca o spalare la masina 1, ca sa ramana fara capsule
    spalatorie.adaugaJob(
            1,
            Durata(0, 35)
    );
    spalatorie.actualizeazaTimp(Durata(3, 0));

// Incercam sa adaugam inca o spalare. Ar trebui sa afiseze mesajul "Masina 1 nu mai are capsule!"
    spalatorie.adaugaJob(
            1,
            Durata(0, 35)
    );
// Ceea ce se poate observa si din listarea masinilor:
    spalatorie.listeazaMasini();

    return 0;
}
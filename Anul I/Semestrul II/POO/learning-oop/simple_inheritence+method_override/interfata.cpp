//#include <bits/stdc++.h>
//using namespace std;
//
//class IoBase {
//private:
//public:
//    friend ostream &operator<<(ostream &os, const IoBase &base) {
//        return base.write(os);
//    }
//    friend istream &operator>>(istream &is, IoBase &base) {
//        return base.read(is);
//    }
//    // metoda citire
//    virtual istream& read(istream& is) { // nu este nevoie de obiectul citit, pt ca avem this
//        return is; // vom vedea ca in interfete deseori nu avem functionalitati
//    }
//    // metoda scriere
//    virtual ostream& write(ostream& os) const { // nu este nevoie de obiectul citit, pt ca avem this
//        return os; // vom vedea ca in interfete deseori nu avem functionalitati
//    }
//};
//
//class PongGame : public IoBase {
//    string player1, player2;
//public:
//    istream &read(istream &is) override {
//        IoBase::read(is); // in general, punem la inceputul apelul
//        cout << "player1: ";
//        is >> player1;
//        cout << "player2: ";
//        is >> player2;
//        return is;
//    }
//
//    ostream &write(ostream &os) const override {
//        IoBase::write(os); // in general, punem la inceputul apelul
//        os<< "player1: " << player1;
//        os<< " player2: " << player2;
//        return os;
//    }
//};
//
//
//
//
//int main(){
//
//
//    return 0;
//}
//#include <bits/stdc++.h>
//#include "Fraction.h"
///*
//* Daca nu aveti bits/stdc++.h puteti include fiecare header:
//*/
//#include <iostream>
//
//using namespace std;
//
//class Student {
//private:
//    string name;
//    int group, semigroup;
//    vector<int> note;
//public:
//    Student(const string &name, int group, int semigroup, const vector<int> &note) : name(name), group(group),
//                                                                                     semigroup(semigroup), note(note) {}
//
//    Student() : group(0), semigroup(0) {}
//
//    // b)
//    // operatori de flux
//    friend ostream &operator<<(ostream &os, const Student &student) {
//        os << "name: " << student.name
//           << " group: " << student.group
//           << " semigroup: " << student.semigroup
//           << " note: ";
//        for (auto nota: student.note) {
//            os << nota << ' ';
//        }
//        return os;
//    }
//
//    friend istream &operator>>(istream &is, Student &student) { // FARA const, deoarece modificam valoarea
//        cout << "name: ";
//        is >> student.name;
//        cout << " group: ";
//        is >> student.group;
//        cout << " semigroup: ";
//        is >> student.semigroup;
//        cout << " note: ";
//        cout << "nr. Note = ";
//        int n, nota;
//        is >> n;
//        // golim vectorul
//        student.note.clear();
//        for (int i = 0; i < n; ++i) {
//            is >> nota;
//            student.note.push_back(nota);
//        }
//        return is;
//    }
//
//    // c)
//    // operatorul +=
//    void operator+=(int notaNoua) {
//        note.push_back(notaNoua);
//    }
//};
//
//int main() {
//    Student s;
//
////    cin >> s;
////    cout << s;
//
//    s = Student(
//            "Enrique Neville",  // numele
//            154,               // grupa
//            2,              // semigrupa
//            {9, 10, 7}); // pentru vector<int> putem folosi direct {note}.
//    s += 10;
//    cout << s << endl;
//    /*
//     * Va afisa:
//     * name: Enrique Neville group: 154 semigroup: 2 note: 9 10 7 10
//     */
//}

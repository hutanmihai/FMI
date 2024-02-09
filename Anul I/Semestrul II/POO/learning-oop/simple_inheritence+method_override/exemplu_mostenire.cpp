//#include <bits/stdc++.h>
//using namespace std;
//
//struct Nota {
//    int value;
//    string subject;
//};
//
//template<typename T>
//istream &operator>>(istream &is, vector<T> &vec){
//    cout << "Nr elemente: ";
//    int n;
//    cin >> n;
//    for (int i = 0; i < n; ++i) {
//        T element;
//        cin >> element;
//        vec.push_back(element);
//    }
//};
//
//template<typename T>
//ostream &operator<<(ostream &os, const vector<T> &vec){
//    for (int i = 0; i < vec.size(); ++i) {
//        os << vec[i] << ' ';
//    }
//};
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
//// aceasta este clasa de baza/parinte
//class PersoanaEvaluata : public IoBase{
//protected:
//    vector<Nota> note;// atributele din clasa de bază se pun sub eticheta protected:
//public:
//    // constructor cu toti parametrii
//    PersoanaEvaluata() {}
//
//    PersoanaEvaluata(const vector<Nota> &note) : note(note) {}
//    // metoda mean va fi comuna tuturor claselor derivate din PersoanaEvaluata
//    double mean() {
//        double sum = 0;
//        for(auto nota : note) {
//            sum += nota.value;
//        }
//        return sum / note.size();
//    }
//
//    istream &read(istream &is) override {
//        int n;
//        cout << "Numarul notelor: ";
//        cin >> n;
//        cin.get();
//        Nota curent;
//        for (int i = 0; i < n; ++i) {
//            cout << "Materia: ";
//            getline(cin, curent.subject);
//            cout << "Nota: ";
//            cin >> curent.value;
//            cin.get();
//            note.push_back(curent);
//        }
//    }
//
//    ostream &write(ostream &os) const override {
//        for (auto element : note){
//            os << "Materia :" << element.subject << '\n';
//            os << "Note: " << element.value << '\n';
//        }
//    }
//};
//
////Clasa elev, derivata din PersoanaEvaluata
//
//// acestea sunt clasele derivate:
//class Pupil : public PersoanaEvaluata{ // aceasta este sintaxa pentru „moștenire publică”
//private:
//    // adaugam noi atribute
//    string cycle;
//public:
//    Pupil() {}
//    // constructori:
//
//    // TODO va rog sa-i implementati si in clasele derivate, pentru antrenament:
//    Pupil(const vector<Nota> &note, const string &cycle) : PersoanaEvaluata(note), cycle(cycle) {}
//
//    // adaugam SI noi metode
//    void showGradeSheet() {
//        for(auto nota:note){
//            cout << "Subject: "<< nota.subject << ", value:" << nota.value << "\n";
//        }
//    }
//    void gradesGroupedBySubject() {
//        vector<string> materii;
//        for(auto nota:note){
//            for(auto materie:materii){
//                if(materie == nota.subject) {
//                    break;
//                }
//                else materii.push_back(nota.subject);
//            }
//        }
//
//        for(auto materie : materii){
//            cout << "Subject: "<<materie<<", ";
//            for(auto nota : note){
//                cout<<"value: "<<nota.value<<" ";
//            }
//            cout << '\n';
//        }
//    }
//
//    istream &read(istream &is) override {
//        PersoanaEvaluata::read(is);
//        cout << "Cycle: ";
//        getline(is,cycle);
//    }
//
//    ostream &write(ostream &os) const override {
//        PersoanaEvaluata::write(os);
//        os << "Cycle: ";
//        os << cycle << '\n';
//    }
//
//
//};
//
//class Student : public PersoanaEvaluata{
//private:
//    string numele_facultatii;
//public:
//    Student() {}
//
//    Student(const vector<Nota> &note, const string &numeleFacultatii) : PersoanaEvaluata(note),numele_facultatii(numeleFacultatii) {}
//
//    istream &read(istream &is) override {
//        PersoanaEvaluata::read(is);
//        cout << "Numele faculatii: ";
//        getline(is,numele_facultatii);
//    }
//
//    ostream &write(ostream &os) const override {
//        PersoanaEvaluata::write(os);
//        os << "Numele facultatii: ";
//        os << numele_facultatii << '\n';
//    }
//};
//
//class CourseTaker : public PersoanaEvaluata{
//private:
//    string numele_cursului;
//public:
//    CourseTaker() {}
//
//    CourseTaker(const vector<Nota> &note, const string &numeleCursului) : PersoanaEvaluata(note),numele_cursului(numeleCursului) {}
//
//    istream &read(istream &is) override {
//        PersoanaEvaluata::read(is);
//        cout << "Numele cursului: ";
//        getline(is, numele_cursului);
//    }
//
//    ostream &write(ostream &os) const override {
//        PersoanaEvaluata::write(os);
//        os << "Numele cursului: ";
//        os << numele_cursului << '\n';
//    }
//};
//
//
//int main(){
//    vector<Pupil> vp;
//    cin >> vp;
//    cout << vp;
//    vector<int> ints;
//    cin >> ints;
//    cout << ints;
//    return 0;
//}
//

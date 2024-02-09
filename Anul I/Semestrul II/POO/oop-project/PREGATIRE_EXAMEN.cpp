//#include<iostream>
//using namespace std;
//
//class cls
//{
//    int x;
//public:
//    cls(int i=0) {cout<<"c1 "; x=i;}
//    ~cls() {cout<<"d1 ";}
//};
//class cls1
//{
//    int x; cls xx;
//public:
//    cls1(int i=0){cout<<"c2 ";x=i;}
//    ~cls1(){cout<<"d2 ";}
//}c;
//class cls2
//{
//    int x;cls1 xx;cls xxx;
//public:
//    cls2(int i=0) {cout<<"c3 ";x=i;}
//    ~cls2(){ cout<<"d3 ";}
//};
//int main()
//{
//    cls2 s;
//    return 0;
//}
//
// todo EXAMEN 2020
//#include <iostream>
//
//class A {
//protected:
//    int nm;
//public:
//    A(int hbr = 1) : nm(hbr) { std::cout << "?"; }
//
//    int ha() { return nm; }
//
//    virtual void r() const {};
//
//    virtual ~A() {};
//};
//
//class B : public A {
//    int d;
//public:
//    B(int b = 2) : d(b) { std::cout << "!!"; }
//
//    void r(int z) const { std::cout << nm << " " << z << "\n"; }
//};
//
//void warranty(const A &am) {
//    am.r(8);
//}
//
//int main() {
//    A ha;
//    B un(ha.ha());
//    warranty(un);
//}
//@todo nu compileaza, functia r trebuie apelata fara parametru GOOD
//#include <iostream>
//
//class A {
//protected:
//    int nm;
//public:
//    A(int hbr = 1) : nm(hbr) { std::cout << "?"; }
//
//    int ha() { return nm; }
//
//    virtual void r() const {};
//
//    virtual ~A() = 0;
//};
//
//class B : public A {
//    int d;
//public:
//    B(int b = 2) : d(b) { std::cout << "!!"; }
//
//    void r(int z) const { std::cout << nm << " " << z << "\n"; }
//};
//
//void warranty(const A &am) {
//    am.r();
//}
//
//int main() {
//    A ha;
//    B un(ha.ha());
//    warranty(un);
//}
//@todo nu compileaza, clasa A este clasa abstracta, iar clasa B care este copilul sau nu suprascrie toate metodele !SE INCEARCA INSTANTIERE UNEI CLASE ABSTRACTE
//#include <iostream>
//
//class A {
//protected:
//    int nm;
//public:
//    A(int hbr = 1) : nm(hbr) { std::cout << "?"; }
//
//    int ha() { return nm; }
//
//    virtual void r() const {};
//
//    virtual ~A() {};
//};
//
//class B : public A {
//    int d;
//public:
//    B(int b = 2) : d(b) { std::cout << "!!"; }
//
//    void r(int z) const { std::cout << nm << " " << z << "\n"; }
//};
//
//void warranty(const A &am) {
//    am.r();
//}
//
//int main() {
//    A ha;
//    B un(ha.ha());
//    warranty(un);
//}
//@todo compileza, afiseaza: ??!!
//
//#include <iostream>
//
//class A {
//protected:
//    int nm;
//public:
//    A(int hbr = 1) : nm(hbr) { std::cout << "??"; }
//
//    int ha() { return nm; }
//
//    virtual void r() const {};
//
//    virtual ~A() {};
//};
//
//class B : public A {
//    int d;
//public:
//    B(int b = 2) : d(b) { std::cout << "!"; }
//
//    void r(int z) const { std::cout << nm << " " << z << "\n"; }
//};
//
//void warranty(const A &am) {
//    am.r();
//}
//
//int main() {
//    A ha;
//    B un(ha.ha());
//    warranty(un);
//}
//@todo compileaza, afiseaza ????!
//
//#include <iostream>
//
//class A {
//protected:
//    int nm;
//public:
//    A(int hbr = 1) : nm(hbr) { std::cout << "??"; }
//
//    int ha() { return nm; }
//
//    virtual void r() const {};
//
//    virtual ~A() {};
//};
//
//class B : public A {
//    int d;
//public:
//    B(int b = 2) : d(b) { std::cout << "!"; }
//
//    void r(int z) const { std::cout << nm << " " << z << "\n"; }
//};
//
//void warranty(const B &am) {
//    am.r(8);
//}
//
//int main() {
//    A ha;
//    B un(ha.ha());
//    warranty(un);
//}
//todo compileaza, afiseaza: ????!1 8
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int y = 0) : x(y) {}
//
//    int getx() {
//        return x;
//    };
//
//    A operator+(A *o) {
//        A r(*this);
//        r.x = r.x + o->x - 1;
//        return r;
//    }
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.x;
//    return o;
//}
//
//int main() {
//    A o1(101);
//    cout << (o1 + &o1);
//    return 0;
//}
//todo nu compileaza, suprascrierea operatorului << gresita, trebuie inclusa in clasa ca functie friend / sau folosim getx
//
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int y = 0) : x(y) {}
//
//    int getx() {
//        return x;
//    };
//
//    A operator+(A *o) {
//        A r(*this);
//        r.x = r.x + o->x + 1;
//        return r;
//    }
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a + a;
//    return o;
//}
//
//int main() {
//    A o1(101);
//    cout << (o1 + &o1);
//    return 0;
//}
//todo nu compileaza, suprascriere operatorului se face pe un ob a si un pointer de tip a, nu pe a si a
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int y = 0) : x(y) {}
//
//    int getx() {
//        return x;
//    };
//
//    A operator+(A *o) {
//        A r(*this);
//        r.x = r.x + o->x;
//        return r;
//    }
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.getx();
//    return o;
//}
//
//int main() {
//    A o1(101);
//    cout << (o1 + &o1);
//    return 0;
//}
//todo compileaza, afiseaza 202
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int y = 0) : x(y) {}
//
//    int getx() {
//        return x;
//    };
//
//    A operator+(A *o) {
//        A r(*this);
//        r.x = r.x + o->x - 1;
//        return r;
//    }
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.getx();
//    return o;
//}
//
//int main() {
//    A o1(103);
//    cout << (o1 + &o1);
//    return 0;
//}
//todo compileaza afiseaz 205
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int y = 0) : x(y) {}
//
//    int getx() {
//        return x;
//    };
//
//    A operator+(A *o) {
//        A r(*this);
//        r.x = r.x + o->x + 1;
//        return r;
//    }
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.getx();
//    return o;
//}
//
//int main() {
//    A o1(103);
//    cout << (o1 + &o1);
//    return 0;
//}
//todo compileaza afiseaza 207
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int &i) : x(i) {}
//
//    int get_x() {
//        return x;
//    }
//
//    A operator+(int &);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int &i) {
//    A t(i);
//    return t;
//}
//
//int main() {
//    int b = 77, c = 9;
//    A a(7);
//    cout << a + b + c << " " << a + c;
//    return 0;
//}
//todo nu compileaza, !CONSTRUCROUL LUI A CERE REFERINTA,trebuie scos &
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int &i) : x(i) {}
//
//    int get_x() {
//        return x;
//    }
//
//    A operator+(int &);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int &i) {
//    A t(i);
//    return t;
//}
//
//int main() {
//    int b = 77, c = 9;
//    A a(b);
//    cout << a + 7 + c << " " << a + c;
//    return 0;
//}
//todo nu compileaza, scoatem & de la A operator+(int &)
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int &i) : x(i) {}
//
//    int get_x() {
//        return x;
//    }
//
//    A operator+(int &);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int &i) {
//    A t(i);
//    return t;
//}
//
//int main() {
//    int b = 77, c = 9;
//    A a(b);
//    cout << a + b + c << " " << a + 7;
//    return 0;
//}
//todo la fel
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int &i) : x(i) {}
//
//    int get_x() {
//        return x;
//    }
//
//    A operator+(int &);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int &i) {
//    A t(i);
//    return t;
//}
//
//int main() {
//    int b = 77, c = 9;
//    A a(b);
//    cout << a + b + c << " " << a + c;
//    return 0;
//}
//todo compileaza si afiseaza 163 86 ! 9 9
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int &i) : x(i) {}
//
//    int get_x() {
//        return x;
//    }
//
//    A operator+(int &);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int &i) {
//    A t(i);
//    return t;
//}
//
//int main() {
//    int b = 77, c = 9;
//    A a(b);
//    cout << a + b << " " << a + c + b;
//    return 0;
//}
//todo ! 77 77
//
//#include <iostream>
//using namespace std;
//
//class A {
//    static int x;
//    const int y;
//public:
//    A(int i) {
//        x = i;
//        y = -i + 3;
//    }
//
//    int put_x(A a) {
//        return x + a.y;
//    }
//};
//
//int A::x = 8;
//
//int main() {
//    A a(2);
//    cout << a.put_x(26);
//    return 0;
//}
//todo nu compileaza, atribut const neinitializat, facme int y in loc de const int y
//
//#include <iostream>
//using namespace std;
//
//class A {
//    static int x;
//    int y;
//public:
//    A(int i) {
//        x = i;
//        y = -i + 3;
//    }
//
//    int put_x(A a) {
//        return x + a.y;
//    }
//};
//
//int main() {
//    A a(2);
//    cout << a.put_x(26);
//    return 0;
//}
//todo atribut static neinitializat in afara clasei, adaugam dupa clasa: int A::x;
//#include <iostream>
//
//using namespace std;
//
//class A {
//    static int x;
//    const int y = 0;
//public:
//    A(int i) {
//        x = i;
//        x = -i + 3;
//    }
//
//    int put_x(A a) {
//        return x + a.y;
//    }
//};
//
//int A::x = 8;
//
//int main() {
//    A a(2);
//    cout << a.put_x(26);
//    return 0;
//}
//todo compileaza, afiseaza -23
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    static int x;
//    const int y = 10;
//public:
//    A(int i) {
//        x = i;
//        x = -y + 3;
//    }
//
//    int put_x(A a) {
//        return x + a.y;
//    }
//};
//
//int A::x = 8;
//
//int main() {
//    A a(2);
//    cout << a.put_x(26);
//    return 0;
//}
//todo compileaza, afiseaza -13 !3
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    static int x;
//    const int y = 10;
//public:
//    A(int i) {
//        x = i;
//        x = y + 3;
//    }
//
//    int put_x(A a) {
//        return x + a.y;
//    }
//};
//
//int A::x = 8;
//
//int main() {
//    A a(2);
//    cout << a.put_x(26);
//    return 0;
//}
//todo compileaza, afiseaza 23
//
//#include <iostream>
//using namespace std;
//
//class X {
//    int i;
//public:
//    X(int j = 10) {
//        i = j;
//        cout << i << " ";
//    }
//
//    const int afisare(int j) {
//        cout << i << " ";
//        return i + j;
//    };
//};
//
//int main() {
//    const X O(7), &O2 = O, *p = &O2;
//    cout << p->afisare(6);
//    return 0;
//}
//todo nu compileaza, !pointerul p este constant si apelez o funcitie neconstanta, adaug const la functia afisare
//
//#include <iostream>
//using namespace std;
//
//class X {
//    int i;
//public:
//    X(int j = 10) {
//        i = j;
//        cout << i << " ";
//    }
//
//    int const afisare(int j) {
//        cout << i << " ";
//        return i + j;
//    };
//};
//
//int main() {
//    const X O(7), &O2 = O, *p = &O2;
//    cout << p->afisare(6);
//    return 0;
//}
//todo la fel
//
//#include <iostream>
//
//using namespace std;
//
//class X {
//    int i;
//public:
//    X(int j = 10) {
//        i = j;
//        cout << i << " ";
//    }
//
//    int afisare(int j) const {
//        cout << i << " ";
//        return i + j;
//    };
//};
//
//int main() {
//    const X O(1), &O2 = O, *p = &O2;
//    cout << p->afisare(6);
//    return 0;
//}
//todo compileaza si !afiseaza 1 1 7
//
//#include <iostream>
//
//using namespace std;
//
//class X {
//    int i;
//public:
//    X(int j = 10) {
//        i = j;
//        cout << i << " ";
//    }
//
//    int afisare(int j) const {
//        cout << i << " ";
//        return i + j;
//    };
//};
//
//int main() {
//    const X O(7), &O2 = O, *p = &O2;
//    cout << p->afisare(6);
//    return 0;
//}
//todo compileaza, afiseaza 7 7 13
//
//#include <iostream>
//
//using namespace std;
//
//class X {
//    int i;
//public:
//    X(int j = 10) {
//        i = j;
//        cout << i << " ";
//    }
//
//    int afisare(int j) const {
//        cout << i << " ";
//        return i - j;
//    };
//};
//
//int main() {
//    const X O(1), &O2 = O, *p = &O2;
//    cout << p->afisare(6);
//    return 0;
//}
//todo compileaza 1 1 -5
//
//#include <iostream>
//using namespace std;
//
//class A {
//    int i;
//public:
//    A(int x = 8) : i(x) {}
//
//    virtual int f(A a) { return i + a.i; }
//};
//
//class B : public A {
//    int j;
//public:
//    B(int x = -2) : j(x) {}
//
//    int f(B b) { return j + b.j; }
//};
//
//int main() {
//    int i = 20;
//    A * o;
//    if (i % 4) {
//        A a;
//        o = new A(i);
//    }
//    else {
//        B b;
//        o = new B(i);
//    }
//    cout << a->f(*o);
//    return 0;
//}
//todo !a nu e definit, programul intra pe else, a nu e pointer, e obiect, modfiicam cu b.f(o)
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int i;
//public:
//    A(int x = 8) : i(x) {}
//
//    virtual int f(A a) { return i + a.i; }
//};
//
//class B : public A {
//    int j;
//public:
//    B(int x = -2) : j(x) {}
//
//    int f(B b) { return j + b.j; }
//};
//
//int main() {
//    int i = 20;
//    A * o;
//    if (i % 4) {
//        A a;
//        o = new A(i);
//    }
//    else {
//        B b;
//        o = new B(i);
//    }
//    cout << b->f(*o);
//    return 0;
//}
//todo b e nu e definit, b nu e pointer, e obiect
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int i;
//public:
//    A(int x = 8) : i(x) {}
//
//    virtual int f(A a) { return i + a.i; }
//};
//
//class B : public A {
//    int j;
//public:
//    B(int x = -2) : j(x) {}
//
//    int f(B b) { return j + b.j; }
//};
//
//int main() {
//    int i = 20;
//    A * o;
//    if (i % 4) {
//        A a;
//        o = new A(i);
//    }
//    else {
//        B b;
//        o = new B(i);
//    }
//    cout << o->f(*o);
//    return 0;
//}
//todo compileaza afiseaza 16
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int i;
//public:
//    A(int x = -8) : i(x) {}
//
//    virtual int f(A a) { return i + a.i; }
//};
//
//class B : public A {
//    int j;
//public:
//    B(int x = 2) : j(x) {}
//
//    int f(B b) { return j + b.j; }
//};
//
//int main() {
//    int i = 20;
//    A * o;
//    if (i % 4) {
//        A a;
//        o = new A(i);
//    }
//    else {
//        B b;
//        o = new B(i);
//    }
//    cout << o->f(*o);
//    return 0;
//}
//todo compileaza afiseaza -16
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int i;
//public:
//    A(int x = -8) : i(x) {}
//
//    virtual int f(A a) { return i + a.i; }
//};
//
//class B : public A {
//    int j;
//public:
//    B(int x = 2) : j(x) {}
//
//    int f(B b) { return j + b.j; }
//};
//
//int main() {
//    int i = 30;
//    A * o;
//    if (i % 4) {
//        A a;
//        o = new A(i);
//    }
//    else {
//        B b;
//        o = new B(i);
//    }
//    cout << o->f(*o);
//    return 0;
//}
//todo compileaza, afiseaza 60
//
//#include <iostream>
//
//using namespace std;
//
//template<class X>
//X f(X x, X y) { return *x - *y; }
//
//int f(double *x, int y) { return *(x + y); }
//
//int main() {
//    double a = 10.7, *b = new double(21);
//    cout << f(a, b);
//    return 0;
//}
//todo nu compileaza, nu gaseste functie potrivita pt f, adaugam * la param X y si stergem * de la x
//
//#include <iostream>
//using namespace std;
//
//template<class X>
//X f(X x, X y) { return *x - *y; }
//
//int f(double *x, int y) { return *(x + y); }
//
//int main() {
//    double a = 10.7, *b = new double(21);
//    cout << f(b, b);
//    return 0;
//}
//todo nu compileaza, nu gaseste functie f potrivita, trb adaugat * in template la ambii param ????????
//
//#include <iostream>
//using namespace std;
//
//template<class X>
//X f(X x, X y) { return *x - *y; }
//
//int f(double *x, int y) { return *(x + y); }
//
//int main() {
//    double a = 10.7, *b = new double(21);
//    cout << f(b, a);
//    return 0;
//}
//todo compileaza si afiseaza valoare nedeterminata
//
//
//#include <iostream>
//using namespace std;
//
//template<class X>
//X f(X x, X y) { return *x - *y; }
//
//int f(double *x, int y) { return *(x + y); }
//
//int main() {
//    double a = 7.7, *b = new double(21);
//    cout << f(b, a);
//    return 0;
//}
//todo la fel
//
//#include <iostream>
//
//using namespace std;
//
//template<class X>
//X f(X x, X y) { return *x - *y; }
//
//int f(double *x, int y) { return *(x + y); }
//
//int main() {
//    double a = 7.7, *b = new double(21);
//    cout << f(a, a);
//    return 0;
//}
//todo la fel ??
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int i = 2) : x(i) {}
//
//    int get_x() { return x; }
//
//    A operator+(int);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int i) { return x + i; }
//
//int main() {
//    A a = -33;
//    int b = 44;
//    cout << a + b << " " << b + 3;
//    return 0;
//}
//todo compileaza, afiseaza 11 47
//
//
//#include <iostream>
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int i = 2) : x(i) {}
//
//    int get_x() { return x; }
//
//    A operator+(int);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.x;
//    return o;
//}
//
//A A::operator+(int i) { return x + i; }
//
//int main() {
//    A a = -33;
//    int b = 44;
//    cout << a + b << " " << b + 3;
//    return 0;
//}
//todo nu compileaza, x este private in functia operator << deci trebuie scrisa ca fiind functie friend
//
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int i = 2) : x(i) {}
//
//    int get_x() { return x; }
//
//    A operator+(int);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int i) { return x + i; }
//
//int main() {
//    A a = -33;
//    int b = 44;
//    cout << a + b << " " << b + 3;
//    return 0;
//}
//todo la fel ca var 1
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int i = 2) : x(i) {}
//
//    int get_x() { return x; }
//
//    A operator+(int);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int i) { return x + i; }
//
//int main() {
//    A a = 33;
//    int b = -44;
//    cout << a + b << " " << b + 3;
//    return 0;
//}
//todo compileaza, afiseaza -11 -41
//
//
//#include <iostream>
//
//using namespace std;
//
//class A {
//    int x;
//public:
//    A(int i = 2) : x(i) {}
//
//    int get_x() { return x; }
//
//    A operator+(int);
//};
//
//ostream &operator<<(ostream &o, A a) {
//    o << a.get_x();
//    return o;
//}
//
//A A::operator+(int i) { return x + i; }
//
//int main() {
//    A a = -33;
//    int b = -44;
//    cout << a + b << " " << b - 3;
//    return 0;
//}
//todo compileaza, afiseaza -77 -47
//
////@todo EXAMEN 2021
//
//class C{
//    int c;
//public: C(int p=1){c=p;}
//    int & get()const{return c;}
//};
//int f(C op){return op.get();}
//int main(){
//    C o1;
//    int x=f(o1);
//    return 0;
//}
//
//class C{
//    int c;
//public: C(int p=1){c=p;}
//    const int & get(){return c;}
//};
//int f(const C*op){return op->get();}
//int main(){
//    C o1;
//    int x=f(&o1);
//    return 0;
//}
//
//class C{
//    int c;
//public: C(int p=1){c=p;}
//    const int & get(){return c;}
//};
//int f(const C & op){return op.get();}
//int main(){
//    C o1;
//    int x=f(o1);
//    return 0;
//}
//
//class C{
//    int c;
//public: C(int p=1){c=p;}
//    const int & get()const{return c++;}
//};
//int main(){
//    const C o1;
//    int x=o1.get();
//    return 0;
//}
//
//class C{
//    int c;
//public: C(int p=1){c=p;}
//    const int & get(){return c;}
//};
//int f(const C op){return op.get();}
//int main(){
//    C o1;
//    int x=f(o1);
//    return 0;
//}
//
//class B{
//public: virtual B * fv(){return this;}
//    int adun(int p){return p+1;}
//};
//class D:public B{
//public: virtual D * fv(){return this;}
//    int adun (int p){return p+2;}
//};
//int main(){
//    B *p =new D;
//    int x=p->fv()->adun(1);
//    return 0;
//}
//
//class B{
//public: virtual B* fv(){return this;}
//    virtual int adun(int p){return p+1;}
//};
//class D:public B{
//public: virtual B* fv(){return this;}
//    virtual int adun (int p){return p+2;}
//};
//int main(){
//    B *p =new D;
//    int x=p->fv()->adun(1);
//    return 0;
//}
//
//class B{
//public: virtual B* fv(){return this;}
//    int adun(int p){return p+1;}
//};
//class D:public B{
//public: virtual B* fv(){return this;}
//    int adun (int p){return p+2;}
//};
//int main(){
//    B *p =new D;
//    int x=p->fv()->adun(1);
//    return 0;
//}
//
//class B{
//public: virtual B * fv(){return this;}
//    virtual int adun(int p){return p+1;}
//};
//class D:public B{
//public: virtual D * fv(){return this;}
//    virtual int adun (int p){return p+2;}
//};
//int main(){
//    B *p =new D;
//    int x=p->fv()->adun(1);
//    return 0;
//}
//
//class B{
//public: B * fv(){return this;}
//    virtual int adun(int p){return p+1;}
//};
//class D:public B{
//public: B * fv(){return this;}
//    virtual int adun (int p){return p+2;}
//};
//int main(){
//    B *p =new D;
//    int x=p->fv()->adun(1);
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B{
//    int *d;
//public: D(int p){d=new int; *d=p;}
//    D(const D& s):B(s){d=new int; *d=*(s.d);}
//    ~D(){delete d;}
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(3);
//    o1=o2;o2.set(4);
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B{
//    int *d;
//public: D(int p){d=new int; *d=p;}
//    D(const D& s):B(s){d=new int; *d=*(s.d);}
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(o1);
//    o1=o2;o2.set(4);
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B{
//    int *d;
//public: D(int p):B(p){d=new int; *d=p;}
//    D(const D& s){d=new int; *d=*(s.d);}
//    D & operator=(const D & s){d=new int; *d=*(s.d);return *this; }
//    ~D(){delete d;}
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(o1);
//    o1=o2;
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B {
//    int *d;
//public: D(int p):B(p){d=new int; *d=p;}
//    D & operator=(const D & s){d=new int; *d=*(s.d);return *this; }
//    ~D(){delete d;}
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(o1);
//    o2.set(3);
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B {
//    int *d;
//public: D(int p):B(p){d=new int; *d=p;}
//    D & operator=(const D & s){d=new int; *d=*(s.d);return *this; }
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(o1);
//    o2.set(3);
//    return 0;
//}
//
//class B{
//    int b;
//public: B(int p=1){b=p;}
//};
//class D: public B {
//    int *d;
//public: D(int p):B(p){d=new int; *d=p;}
//    D & operator=(const D & s){d=new int; *d=*(s.d);return *this; }
//    ~D(){delete d;}
//    void set(int p){*d=p;}
//};
//int main()
//{D o1(2),o2(o1);
//    o1=o2;o2.set(3);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    float z;
//public:
//    C() { z = 1.3; }
//    float op(float x, float y, float t) {
//        return x + y + z + t;
//    }
//    float op(float x, float y = 1.0) {
//        return x + y + z;
//    }
//    float op() {
//        return z;
//    }
//};
//int main() {
//    C c;
//    float i,j, k;
//    i=c.op(1);
//    j=i+c.op(2.2, 4.8);
//    k=c.op(2.2, 3.5, 4);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    float z;
//public:
//    C() { z = 1.3; }
//    float op(float x, float y, float t) {
//        return x + y + z + t;
//    }
//    float op(float x, float y = 1.0) {
//        return x + y + z;
//    }
//    float op(float x) {
//        return x + z;
//    }
//};
//int main() {
//    C c;
//    float i,j, k;
//    i=c.op(1.2);
//    j=i+c.op(2.2, 4.8);
//    k=c.op(2.2, 3.5, 4);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    float z;
//public:
//    C() { z = 1.3; }
//    float op(float x, float y, float t) {
//        return x + y + z + t;
//    }
//    float op(float x = 1.0, float y) {
//        return x + y + z;
//    }
//    float op() {
//        return z;
//    }
//};
//int main() {
//    C c;
//    float i,j, k;
//    i=c.op(1.2);
//    j=i+c.op(2.2, 4.8);
//    k=c.op(2.2, 3.5, 4);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    float z;
//public:
//    C() { z = 1.3; }
//    float op(float x = 2.0, float y = 1.2, float t = 1.5) {
//        return x + y + z + t;
//    }
//    int op(int y) {
//        return y + z;
//    }
//    double op(double y) {
//        return y + z;
//    }
//};
//int main() {
//    C c;
//    float i,j, k;
//    i=c.op();
//    j=i+c.op(1.2);
//    k=c.op(2);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    float z;
//public:
//    C() { z = 1.3; }
//    float op(float x = 2.0, float y = 1.2, float t = 1.5) {
//        return x + y + z + t;
//    }
//    float op(float y) {
//        return y + z;
//    }
//    double op(double y) {
//        return y + z;
//    }
//};
//int main() {
//    C c;
//    cout << c.op() << "\n";
//    cout << c.op(1.2) << "\n";
//    cout << c.op(1) << "\n";
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class B {
//protected:
//    static int x;
//    int offset;
//public:
//    B()
//    {x++; offset = 100;}
//    ~B() { x--; }
//    static int get_x() { return x; }
//    int get_offset() { return offset; }
//    int f() { return (x + offset) / 2; }
//};
//int B::x = 0;
//class D : public B {
//public:
//    D() { x++; }
//    ~D() { x--; }
//    int f() { return ( (x + offset) / 2 + 1); }
//};
//void func(B* q, int n) {cout << q->get_x() << " ";
//for(int i = 0; i < n; i++) cout << q[i].f() << " ";
//cout<<"\n";
//}
//int main()
//{
//    B* p = new B[2]; func(p, 2); delete[] p;
//    p = new D; func(p, 1); delete p;
//    cout << D::get_x(); return 0;
//}
//
//#include <iostream>
//using namespace std;
//class B {protected:
//    static int x;
//    int offset;
//public:
//    B() { x++;offset = 100; }
//    ~B() { x--; }
//    static int get_x() { return x; }
//    int get_offset() { return offset; }
//    int f() { return (x + offset) / 2; }
//};
//int B::x = 0;
//class D : public B {public:
//    D() { x++; }
//    ~D() { x--; }
//    int f() { return (x + offset) / 2 + 1; }
//};
//void func(B* q, int n){cout << q->get_x() << " ";
//for(int i = 0; i < n; i++) cout << q[i].f() << " ";
//cout<<"\n";}
//int main()
//{
//    B* p = new B[2];func(p, 2);delete[] p;
//    p = new D;func(p, 1); delete p;
//    cout << D::get_x();
//}
//
//#include <iostream>
//using namespace std;
//class B {
//protected:
//    static int x;
//    int offset;
//public:
//    B() {x++; offset = 100; }
//    ~B() { x--; }
//    virtual static int get_x() { return x; }
//    int get_offset() { return offset; }
//    virtual int f() { return (x + offset) / 2; }
//};
//int B::x = 0;
//class D : public B {public:
//    D() { x++; }
//    ~D() { x--; }
//    int f() { return (x + offset) / 2 + 1; }
//};
//void func(B* q, int n){cout << q->get_x() << " ";
//for(int i = 0; i < n; i++)cout << q[i].f() << " ";
//cout<<"\n";}
//int main()
//{
//    B* p = new B[2];func(p, 2);delete[] p;
//    p = new D;func(p, 1);delete p;
//    cout << D::get_x();
//}
//
//#include <iostream>
//using namespace std;
//class B {
//protected:
//    static int x;
//    int offset;
//public:
//    B(){ x++;offset = 100;}
//    ~B() { x--; }
//    static int f() { return x; }
//    int get_offset() { return offset; }
//    virtual int f() { return (x + offset) % 2; }
//};
//int B::x = 0;
//class D : public B {public:
//    D() { x++; }
//    ~D() { x--; }
//    int f() { return (x + offset) % 2 + 1; }
//};
//void func(B* q, int n){
//for(int i = 0; i < n; i++) cout << q[i].f() << " ";
//cout<<"\n";
//}
//int main()
//{
//    B* p = new B[2];func(p, 2);delete[] p;
//    p = new D;func(p, 1);delete p;
//}
//
//#include <iostream>
//using namespace std;
//class B {
//protected:
//    static int x;
//    int offset;
//public:
//    B() { x++; offset = 100; }
//    ~B() { x--; }
//    static int get_x() { return x; }
//    int get_offset() { return offset; }
//    static int f() { return (x + get_offset()) % 2; }
//};
//int B::x = 0;
//class D : public B {public:
//    D() { x++; }
//    ~D() { x--; }
//    int f() { return (x + offset) % 2 + 1; }
//};
//void func(B* q, int n){
//for(int i = 0; i < n; i++)cout << q[i].f() << " ";
//cout<<"\n";
//}
//int main()
//{
//    B* p = new B[2];func(p, 2); delete[] p;
//    p = new D; func(p, 1); delete p;
//    cout << D::get_x();
//}
//
//#include <iostream>
//using namespace std;
//class A{
//    int x;
//public:
//    A(int i = 25){x = i; }
//    int& get_x() const { return x; }
//    void set_x(int i) { x = i; }
//    A& operator=(A a1){
//        set_x(a1.get_x());
//        return *this;
//    }
//};
//int main()
//{
//    A a(18), b(7);
//    (b=a).set_x(27);
//    int i;
//    i=b.get_x();
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class A{
//    int x;
//public:
//    A(int i = 25){ x = i; }
//    int get_x() const{ return x;}
//    void set_x(int i){ x=i; }
//    A operator=(A a1)
//    {
//        set_x(a1.get_x());
//        return a1;
//    }
//};
//int main()
//{
//    A a(18), b(7);
//    (b=a).set_x(27);
//    int i;
//    i=b.get_x();
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class A
//{
//    int *x;
//public:
//    A(int i = 25){ x = new int(i); }
//    int& get_x() const { return *x; }
//    void set_x(int i) { x = new int(i); }
//    A& operator=(A a1)
//    {
//        set_x(a1.get_x());
//        return *this;
//    }
//};
//int main()
//{
//    A a(18), b(7);
//    (b=a).set_x(27);
//    int i;
//    i=b.get_x();
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class A {
//    int *x;
//public:
//    A() { x = new int(0); }
//    A(int i) { x = new int(i); }
//    int& get_x() const { return *x; }
//    void set_x(int i) { x = new int(i); }
//    A operator=(A a1) { set_x(a1.get_x());return a1;}
//};
//class B : public A {
//    int y;
//public:
//    B() : A() { y = 0; }
//    B(int i) : A(i){ y = i;}
//    void afisare() const { cout << y; }
//};
//int main()
//{
//    B a(112), b, *c;
//    int i;
//    i=(b = a).get_x();
//    (c = &a)->afisare();
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class A {
//    int x;
//public:
//    A(){ x = 0; }
//    A(int i) { x = i; }
//    int& get_x() const { return x; }
//    void set_x(int i) { x = i; }
//    A operator=(A a1) { set_x(a1.get_x()); return a1;}
//};
//class B : public A {
//    int y;
//public:
//    B() : A(){ y = 0;}
//    B(int i) : A(i) { y = i; }
//    void afisare() const { cout << y; }
//};
//int main()
//{
//    B a(112), b, *c;
//    int i;
//    i= (b = a).get_x()<<"\n";
//    (c = &a)->afisare();
//    return 0;
//}
//
//class Baza {
//protected:
//    int x,y;
//public:
//    Baza() {
//        this->x = 0;
//        this->y = 0;
//    }
//    Baza(int x, int y) {
//        this->x = x;
//        this->y = y;
//    }
//    int Suma() {return x + y;}
//};
//class Derivata : public Baza {
//    double t;
//public:
//    Derivata(int x, int y, double t) {
//        Baza(x,y);
//        this -> t = t;
//    }
//    double Suma() {return x + y + t;}
//};
//int main() {
//    Derivata d(5, 3, 1.5);
//    int i= d.Suma();
//}
//
//class Baza {
//protected:
//    int x,y;
//public:
//    Baza() {
//        this->x = 0;
//        this->y = 0;
//    }
//    Baza(int x, int y) {
//        this->x = x;
//        this->y = y;
//    }
//    int Suma() {return x + y;}
//};
//class Derivata : public Baza {
//    double t;
//public:
//    Derivata() {
//        this -> t = 2.5;
//    }
//    Derivata(Derivata& derivata) {
//        Baza(derivata.x + 1, derivata.y + 1);
//        this -> t = derivata.t;
//    }
//    double Suma() {return x + y + t;}
//};
//int main() {
//    Derivata d;
//    Derivata d1(d);
//    int i= d1.Suma();
//}
//
//class Baza {
//protected:
//    int x,y;
//public:
//    Baza() {
//        this.x = 0;
//        this.y = 0;
//    }
//    Baza(int x, int y) {
//        this.x = x;
//        this.y = y;
//    }
//    int Suma() {return x + y;}
//};
//class Derivata : public Baza {
//    double t;
//public:
//    Derivata() {
//        this.t = 2.5;
//    }
//    Derivata(Derivata& derivata) {
//        Baza(derivata.x + 1, derivata.y + 1);
//        this.t = derivata.t;
//    }
//    double Suma() {return x + y + t;}
//};
//int main() {
//    Derivata d;
//    Derivata d1(d);
//    int i= d1.Suma();
//}
//
//class Baza {
//protected:
//    int x,y;
//public:
//    Baza(int x, int y) {
//        this->x = x;
//        this->y = y;
//    }
//    int Suma() {return x + y;}
//};
//class Derivata : public Baza {
//    double t;
//public:
//    Derivata() {
//        this -> t = 2.5;
//    }
//    Derivata(Derivata& derivata) {
//        Baza(derivata.x + 1, derivata.y + 1);
//        this -> t = derivata.t;
//    }
//    double Suma() {return x + y + t;}
//};
//int main() {
//    Derivata d;
//    Derivata d1(d);
//    int i= d1.Suma();
//}
//
//class Baza {
//protected:
//    int x,y;
//public:
//    Baza() {
//        this->x = 0;
//        this->y = 0;
//    }
//    Baza(int x, int y) {
//        this->x = x;
//        this->y = y;
//    }
//    int Suma() {return x + y;}
//};
//class Derivata : public Baza {
//    double t;
//public:
//    Derivata() {
//        Baza(1,1);
//        this -> t = 3.5;
//    }
//    Derivata(Derivata& derivata) {
//        Baza(derivata.x + 1, derivata.y + 1);
//        this -> t = derivata.t;
//    }
//    double Suma() {return x + y + t;}
//};
//int main() {
//    Derivata d;
//    Derivata d1(d);
//    int i= d1.Suma();
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    int const *p;
//public:
//    C (int *q) : p(q) {}
//    void reload () { delete p; p = new int;}
//    void set (const int * const q) { *p = *q; }
//};
//int main () {
//    int x = 20210614;
//    C ob(&x);
//    const int& rx = x;
//    ob.reload(); ob.set(&rx);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    int *p;
//public:
//    C (int *q) : p(q) {}
//    void reload () { delete p; p = new int;}
//    void set (int q) const { *p = q; }
//};
//int main () {
//    int x = 20210614;
//    C ob(&x);
//    ob.reload(); ob.set(x);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    int * p;
//public:
//    C (int *q) : p(q) {}
//    void reload () { delete p; p = new int;}
//    void set (const int * const q) { *p = *q + 13; }
//    operator int () {return *p;}
//};
//int main () {
//    int *x = new int(20210601); const int& rx = *x;
//    C ob(x);
//    ob.reload(); ob.set(&rx);
//    cout << ob;
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    int * const p;
//public:
//    C (int q) : p(new int(q)) {}
//    void set (const int& q) const { *p = q + 86; }
//    operator int () const {return *p;}
//};
//int main () {
//    const C ob(91973549);
//    ob.set(422032);
//    cout << ob;
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class C {
//    int * const p;
//public:
//    C (int q) : p(new int(q)) {}
//    void set (const int& q) const { *p = q + 59; }
//    operator int () {return *p;}
//};
//int main () {
//    const C ob(22973890);
//    ob.set(488474);
//    cout << ob;
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class Vector2D {
//    int x, y;
//public:
//    Vector2D(const int& a, const int& b) : x(a), y(b) {}
//    Vector2D operator+ (Vector2D v) {
//        Vector2D w(x + v.x, y + v.y); return w;
//    }
//    friend ostream& operator<< (ostream& out, Vector2D& v) {
//        out << "(" << v.x << ", " << v.y << ")"; return out;
//    }
//};
//int main () {
//    cout << Vector2D(10, 5) + Vector2D(22, 159);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class Vector2D {
//    int x, y;
//public:
//    Vector2D(const int& a, const int& b) : x(a), y(b) {}
//    Vector2D operator+ (Vector2D v) {
//        Vector2D w(x + v.x, y + v.y); return w;
//    }
//    friend ostream& operator<< (ostream& out, const Vector2D& v) {
//        out << "(" << v.x << ", " << v.y << ")"; return out;
//    }
//};
//int main () {
//    cout << Vector2D(2, 5) + Vector2D(4, 8);
//    return 0;
//}
//
//#include <iostream>
//using namespace std;
//class Vector2D {
//    int x, y;
//public:
//    Vector2D(const int& a, const int& b) : x(a), y(b) {}
//    friend Vector2D operator+ (Vector2D& v, Vector2D& u) {
//        Vector2D w(u.x + v.x, u.y + v.y); return w;
//    }
//    friend ostream& operator<< (ostream& out, const Vector2D& v) {
//        out << "(" << v.x << ", " << v.y << ")"; return out;
//    }
//};
//int main () {
//    cout << Vector2D(45, 29) + Vector2D(87, 10);
//    return 0;
//}
//
//#include <iostream>
//                using namespace std;
//                class Vector2D {
//                    int x, y;
//                    const int translate = 10 ;
//                    public:
//                    Vector2D(const int& a, const int& b) : x(a), y(b) {}
//                    Vector2D operator* (const Vector2D& v) {
//                        return Vector2D(translate + x * v.x, translate + y + v.y);
//                    }
//                    friend ostream& operator<< (ostream& out, const Vector2D& v) {
//                        out << "(" << v.x << ", " << v.y << ")"; return out;
//                    }
//                };
//                int main () {
//                    cout << Vector2D(98, 69) * Vector2D(82, 12);
//                    return 0;
//                }
//
//#include <iostream>
//                using namespace std;
//                class Vector2D {
//                    int x, y;
//                    public:
//                    Vector2D(const int& a, const int& b) : x(a), y(b) {}
//                    Vector2D operator* (Vector2D v) const {
//                        return Vector2D(x + v.y, y + v.x);
//                    }
//                    friend ostream& operator<< (ostream& out, const Vector2D& v) {
//                        out << "(" << v.x << ", " << v.y << ")"; return out;
//                    }
//                };
//                int main () {
//                    cout << Vector2D(33, 40).operator*(Vector2D(77, 60));
//                    return 0;
//                }
//
//#include <iostream>
//                using namespace std;
//                class A {
//                    public:
//                    A () {cout << "A";}
//                    ~A () {cout << "~A";}
//                };
//                class B: public A {
//                    public:
//                    B () {cout << "B";}
//                    ~B () {cout << "~B";}
//                };
//                class C: public B {
//                    public:
//                    C () {cout << "C";}
//                    ~C () {cout << "~C";}
//                };
//                int main () {
//                    A *pa = new C(); delete pa;
//                    return 0;
//                }
//
//#include <iostream>
//                using namespace std;
//                class A {
//                    public:
//                    A () {cout << "A";}
//                    ~A () {cout << "~A";}
//                };
//                class B: A {
//                    public:
//                    B () {cout << "B";}
//                    ~B () {cout << "~B";}
//                };
//                class C: public B {
//                    public:
//                    C () {cout << "C";}
//                    ~C () {cout << "~C";}
//                };
//                int main () {
//                    A *pa = new C();
//                    delete pa;
//                    return 0;
//                }
//#include <iostream>
//                using namespace std;
//                class A {
//                    public:
//                    A () {cout << "A";}
//                    virtual ~A () {cout << "~A";}
//                };
//                class B: public A {
//                    public:
//                    B () {cout << "B";}
//                    ~B () {cout << "~B";}
//                };
//                class C: public B {
//                    public:
//                    C () {cout << "C";}
//                    ~C () {cout << "~C";}
//                };
//                int main () {
//                    A *pa = new C(); delete pa;
//                    return 0;
//                }
//
//#include <iostream>
//                using namespace std;
//                class A {
//                    public:
//                    A () {cout << "A";}
//                    ~A () {cout << "~A";}
//                };
//                class B: public A {
//                    public:
//                    B () {cout << "B";}
//                    ~B () {cout << "~B";}
//                };
//                class C: public A, public B {
//                    public:
//                    C () {cout << "C";}
//                    ~C () {cout << "~C";}
//                };
//                int main () {
//                    A *pa = new C(); delete pa;
//                    return 0;
//                }
//
//#include <iostream>
//                using namespace std;
//                class A {
//                    public:
//                    A () {cout << "A";}
//                    ~A () {cout << "~A";}
//                };
//                class B: public A {
//                    public:
//                    B () {cout << "B";}
//                    virtual ~B () {cout << "~B";}
//                };
//                class C: public A, public B {
//                    public:
//                    C () {cout << "C";}
//                    ~C () {cout << "~C";}
//                };
//                int main () {
//                    B *pb = new C(); delete pb;
//                    return 0;
//                }
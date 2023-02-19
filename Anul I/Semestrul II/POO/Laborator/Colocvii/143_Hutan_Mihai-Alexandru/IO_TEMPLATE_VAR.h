#ifndef POO_IO_TEMPLATES_H
#define POO_IO_TEMPLATES_H
#include <iostream>
using namespace std;

class IO_var {
private:
public:
    virtual istream &read(istream &is) {
        return is;
    }

    virtual ostream &write(ostream &os) const {
        return os;
    }

    friend ostream &operator<<(ostream &os, const IO_var &base) {
        return base.write(os);
    }

    friend istream &operator>>(istream &is, IO_var &base) {
        return base.read(is);
    }
};
#endif

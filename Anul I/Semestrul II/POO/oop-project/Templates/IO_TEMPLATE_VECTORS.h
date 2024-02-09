#ifndef POO_IO_TEMPLATES_H
#define POO_IO_TEMPLATES_H
#include <vector>
#include <iostream>
using namespace std;

template<typename T>
istream &operator>>(istream &is, vector<T> &vec);

template<typename T>
ostream &operator<<(ostream &os, const vector<T> &vec);

#endif
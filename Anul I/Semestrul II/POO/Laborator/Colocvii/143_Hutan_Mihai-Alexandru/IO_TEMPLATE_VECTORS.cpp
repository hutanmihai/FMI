#include "IO_TEMPLATE_VECTORS.h"

template<typename T>
istream &operator>>(istream &is, vector<T> &vec) {
    vec.clear();
    int n;
    cout << "n: ";
    cin >> n;
    cin.get();
    for (int i = 0; i < n; ++i) {
        T item;
        cin >> item;
        vec.push_back(item);
    }
    cin.get();
    return is;
}

template<typename T>
ostream &operator<<(ostream &os, const vector<T> &vec) {
    for(auto& elem : vec) {
        os << elem << ' ';
    }
    os << '\n';
    return os;
}

//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int main() {
//    int v[100], n, cnt, s;
//
//    // citim vectorul de 2*n elemente:
//    cin >> n;
//    for (int i = 0; i < 2 * n; ++i) {
//        cin >> v[i];
//    }
//
//    // pe scurt, primele n elemente le vom ordona crescator, si la fel si pe ultimele doua
//    // (Dar nu pe toate, conform cerintei. Daca ati inteles ca trebuia sa sortati toate elementele,
//    //   si in aceasta idee ati reusit :), consider tot corect)
//    //
//    // Dupa aceea, vom alege perechiile de elemente  v[0], v[n]        v[1], v[n+1]     =>   suma maxima
//    // iar daca alegem                               v[0], v[2*n-1]    v[1], v[2*n-1]   =>   suma minima
//
//    sort(v, v + n);
//    sort(v + n, v + 2 * n);
//
//    s = 0;
//    for (int i = 0; i < n; ++i) {
//        s += v[i] * v[n + i];
//    }
//    cout << "Suma maxima: " << s << endl;
//
//    s = 0;
//    for (int i = 0; i < n; ++i) {
//        s += v[i] * v[2 * n - 1 - i];
//    }
//    cout << "Suma minima: " << s << endl;
//
//
//}
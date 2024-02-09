//1)
//a)

#include <iostream>
using namespace std;

int main() {
    int an1,luna1,ziua1,an2,luna2,ziua2;
    cin>>an1>>luna1>>ziua1>>an2>>luna2>>ziua2;
    if (an1>an2){
        cout<<"Prima";
    }
    else if (an1<an2) {
        cout <<"A doua";
    }
    else if (luna1>luna2) {
        cout<<"Prima";
    }
    else if (luna1<luna2){
        cout<<"A doua";
    }
    else if (ziua1>ziua2) {
        cout<<"Prima";
    }
    else if (ziua1<ziua2){
        cout<<"A doua";
    }
    else {
        cout<<"Sunt aceleasi date!";
    }
    return 0;
}
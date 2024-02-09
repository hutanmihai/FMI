//#include <bits/stdc++.h>
//using namespace std;
//
//class ConstructionProduct{
//    int cantitate;
//    string unitate_de_masura, nume;
//    float pret;
//
//public:
//    ConstructionProduct():cantitate(0),pret(0){};
//
//    ConstructionProduct(string &nume, int cantitate, string unitate_de_masura, float pret): nume(nume),cantitate(cantitate),unitate_de_masura(unitate_de_masura),pret(pret){}
//
//     ConstructionProduct operator++(){
//         ConstructionProduct cpy = *this;
//         cantitate++;
//         return *this;
//    }
//
//    ConstructionProduct operator++(int){
//        ConstructionProduct cpy = *this;
//        cantitate++;
//        return *this;
//    }
//
//    ConstructionProduct operator+=(int x){
//         ConstructionProduct cpy = *this;
//         cantitate += x;
//         return *this;
//
//     }
//
//    int getCantitate(){
//        return cantitate;
//    }
//
//    string getUnit(){
//        return unitate_de_masura;
//    }
//
//    string getName(){
//        return nume;
//    }
//
//    float getPrice(){
//        return pret;
//    }
//
//    friend ostream &operator<<(ostream &os, ConstructionProduct &product);
//
//    friend istream &operator>>(istream &is, ConstructionProduct &product);
//};
//
//void afischitanta(vector<ConstructionProduct> &products){
//    float suma = 0;
//    int i = 1;
//    cout << "Chitanta renovare:\n";
//    for (auto product : products) {
//        cout << i++ <<". "<< product.getName() <<" ("<<product.getUnit()<<") "<<"x "<<product.getCantitate()<<"\n";
//        cout << product.getCantitate() << " x " << product.getPrice() << " = " << product.getCantitate() * product.getPrice()<<" RON\n";
//        suma += product.getCantitate() * product.getPrice();
//    }
//    cout << "---\n";
//    cout<<"Total: "<<suma<<" RON\n";
//}
//
//ostream &operator<<(ostream &os, ConstructionProduct &product){
//    os << "nume: " << product.nume <<"\n"<<"cantitate: "<<product.cantitate<<"\n"<<"unitate_de_masura: "<< product.unitate_de_masura<< "\n" << "pret: "<< product.pret << "\n";
//    return os;
//}
//
//istream &operator>>(istream &is, ConstructionProduct &product){
//    cout<<"nume:";
//    getline(is, product.nume);
//    cout << "cantitate:";is>>product.cantitate;
//    is.get();
//    cout << "unitate_de_masura:";
//    getline(is, product.unitate_de_masura);
//    cout<<"pret:"; is>>product.pret;
//    is.get();
//}
//
//
//int main(){
//    vector<ConstructionProduct> products;
//    ConstructionProduct produs;
//    int n;
//    cout<<"nr produse: ";
//    cin >> n;
//    cin.ignore();
//    for (int i = 0; i < n; ++i) {
//        cin >> produs;
//        products.insert(products.end(),produs);
//    }
//    afischitanta(products);
//
//    for(auto product : products){
//        cout << product;
//        ++product;
//        ++product;
//        cout<<product;
//        product++;
//        product++;
//        product++;
//        cout << product;
//        product += 300;
//        cout << product;
//    }
//
//
//
//    return 0;
//}
//

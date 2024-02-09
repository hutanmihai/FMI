//#include <bits/stdc++.h>
//using namespace std;
//
//class Gift {
//protected:
//    string name, giverName;
//public:
//    Gift(const string &name, const string &giverName) : name(name), giverName(giverName) {}
//
//    virtual void offerGift(string receivedBy) {
//        cout << "The gift named " << name
//             << " was received by " << receivedBy
//             << " thanks to the courtesy of " << giverName << '\n';
//    }
//};
//
//// !! Toti constructorii pot fi generate automat in CLion
//
//class GiftCard : public Gift {
//private:
//    int sum;
//public:
//    GiftCard(const string &name, const string &giverName, int sum) : Gift(name, giverName), sum(sum) {}
//    void offerGift(string receivedBy) override {
//        cout << "Congratulations " << '"' << receivedBy << '"'
//             << "! You received a gift card of " << sum << "USD from "
//             << '"' << giverName << '"'
//             << '\n';}
//};
//
//class GiftHoliday : public Gift {
//private:
//    string location;
//public:
//    GiftHoliday(const string &name, const string &giverName, const string &location) : Gift(name, giverName),location(location) {}
//    void offerGift(string receivedBy) override {
//        cout << "Congratulations "<<'"'<<receivedBy<<'"'<<"! Your received a gift holiday from "<<giverName<<" that was sent from "<<location;
//    }
//};
//
//class GiftFavouriteProduct : public Gift {
//private:
//    string category;
//public:
//    GiftFavouriteProduct(const string &name, const string &giverName, const string &category) : Gift(name, giverName),category(category) {}
//
//    void offerGift(string receivedBy) override {
//        cout << "You just got a gift from " << giverName  << " that is part of you favourite category: "<<category<<'\n';
//    }
//};
//
//// Atributele   name, giverName   și metoda   void offerGift(string receivedBy) vor putea fi folosite de oricare dintre tipurile de produse, adică:
//
//
//int main() {
//    Gift simpleGift("No Name", "Eleanor Roosevelt");
//    GiftCard card("Andrei Popescu", "Popescu Miruna", 300);
//    GiftHoliday holiday("Ibiza platita!", "Leonard Coste", "Ibiza, Spain");
//    GiftFavouriteProduct phone("Pentru tine", "Costache Leurdean", "Apple Products");
//
//    simpleGift.offerGift("Ioan");
//    card.offerGift("Persida");
//    holiday.offerGift("Romeo");
//    phone.offerGift("Caligula");
//
//    return 0;
//};
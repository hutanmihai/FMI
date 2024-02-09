//#include <bits/stdc++.h>
//using namespace std;
//
//struct coord{
//    int x;
//    int y;
//};
//
//ostream &operator<<(ostream &os, coord &point){
//    cout<<"x: "<<point.x<<"\n";
//    cout<<"y: "<<point.y<<"\n";
//}
//
//class InterestPoint{
//    int nr_vizitatori;
//    coord punct;
//public:
//    InterestPoint():nr_vizitatori(0),punct({0,0}) {}
//
//    InterestPoint(int nr_vizitatori, coord punct):nr_vizitatori(nr_vizitatori), punct(punct){}
//
//    friend ostream &operator<<(ostream &os, InterestPoint &point);
//
//    friend istream &operator>>(istream &is,InterestPoint &point);
//
//    int getNr_vizitatori(){
//        return nr_vizitatori;
//    }
//
//    coord getPunct(){
//        return punct;
//    }
//};
//
//class BikeTrail{
//    string denumire, oras;
//    vector<InterestPoint> interestpoints;
//public:
//    BikeTrail():denumire(""),oras(""),interestpoints(0){}
//
//    BikeTrail(string denumire, string oras, vector<InterestPoint> interestpoints): denumire(denumire),oras(oras),interestpoints(interestpoints){}
//
//    friend ostream &operator<<(ostream &os, BikeTrail &trail);
//
//    friend istream &operator>>(istream &is,BikeTrail &trail);
//
//    string getDenumire(){
//        return denumire;
//    }
//
//    string getOras(){
//        return oras;
//    }
//
//    vector<InterestPoint> getInterestPoints(){
//        return interestpoints;
//    }
//};
//
//ostream &operator<<(ostream &os, InterestPoint &point){
//    os << "Numar vizitatori: " << point.nr_vizitatori << "\n" << "Coordonate: \n" << "x: "<< point.punct.x << '\n' << "y: " << point.punct.y << '\n';
//}
//
//istream &operator>>(istream &is,InterestPoint &point){
//    cout << "Numar vizitatori: ";
//    is >> point.nr_vizitatori;
//    cout << "Coordonate: \n";
//    cout << "x="; is >> point.punct.x; cout << "\n";
//    cout << "y="; is >> point.punct.y; cout << "\n";
//}
//
//ostream &operator<<(ostream &os, BikeTrail &trail){
//    os << "Denumirea pistei: " << trail.denumire << "\n";
//    os << "Orasul in care se afla: " << trail.oras << "\n";
//    os << "Interest Points: \n";
//    for(auto interestpoint : trail.interestpoints){
//        os << interestpoint << "\n";
//    }
//}
//
//istream &operator>>(istream &is,BikeTrail &trail){
//    cout << "Denumirea pistei: ";
//    getline(is, trail.denumire);
//    cout << "Orasul: ";
//    getline(is, trail.oras);
//    int n;
//    cout << "numarul punctelor de interes: ";
//    cin >> n;
//    cin.get();
//    InterestPoint pct;
//    for (int i = 0; i < n; ++i) {
//        is >> pct;
//        (trail.interestpoints).insert((trail.interestpoints).end(),pct);
//    }
//}
//
//bool comparepoints(InterestPoint point1, InterestPoint point2){
//    return (point1.getNr_vizitatori()<point2.getNr_vizitatori());
//}
//
//int main(){
//    int nr = 0;
//    // c)
//    BikeTrail trail;
//    cin >> trail;
//    vector<InterestPoint> interestpoints;
//    interestpoints = trail.getInterestPoints();
//    for(auto interestpoint : interestpoints){
//        nr++;
//    }
//
//    //d)
///*
//    coord point1,point2,point3;
//    int distmijloc, distfin, nrtotalvizit, distmijl = -1;
//    int distmax = 0;
//    for (int i = 0; i < nr; ++i) {
//        int dist = 0;
//        int total;
//        int last = -1;
//        total = interestpoints[i].getNr_vizitatori();
//        coord pct1 = interestpoints[i].getPunct();
//        for (int j = 0; j < nr; ++j) {
//            if(last == -1){
//                total += interestpoints[j].getNr_vizitatori();
//                last = interestpoints[j].getNr_vizitatori();
//            }
//            else{
//                dist = 0;
//                total -= last;
//                total += interestpoints[j].getNr_vizitatori();
//                last = interestpoints[j].getNr_vizitatori();
//            }
//            coord pct2 = interestpoints[j].getPunct();
//            dist += sqrt(pow((pct1.x-pct2.x),2)+ pow((pct1.y-pct2.y),2));
//            distmijl = dist;
//            for (int k = 0; k < nr; ++k) {
//                total += interestpoints[k].getNr_vizitatori();
//                coord pct3 = interestpoints[k].getPunct();
//                dist += sqrt(pow((pct2.x-pct3.x),2)+ pow((pct2.y-pct3.y),2));
//                if(dist > distmax and i != j and i != k and j != k){
//                    distmax = dist;
//                    distfin = distmax - distmijl;
//                    distmijloc = distmijl;
//                    point1 = pct1;
//                    point2 = pct2;
//                    point3 = pct3;
//                    nrtotalvizit = total;
//                }
//                dist = distmijl;
//
//                total -= interestpoints[k].getNr_vizitatori();
//            }
//        }
//    }
//    cout<<"Punctul 1: \n"<< "x:" << point1.x << "\n" << "y:" << point1.y<< "\n";
//    cout<<"Punctul 2: \n"<< "x:" << point2.x << "\n" << "y:" << point2.y<< "\n";
//    cout<<"Punctul 3: \n"<< "x:" << point3.x << "\n" << "y:" << point3.y<< "\n";
//    cout << "Distanta de la primul la al doilea: " << distmijloc << "\n";
//    cout << "Distanta de la al doilea la al treilea: "<<distfin<<"\n";
//    cout << "Distanta totala: "<<distmax<<"\n";
//    cout << "Numarul total al vizitatorilor: "<<nrtotalvizit<<"\n";
//*/
//
//    //e)
//
//    sort(interestpoints.begin(),interestpoints.end(),comparepoints);
//    InterestPoint point1,point2,point3;
//    point1 = interestpoints[nr-1];
//    point2 = interestpoints[nr-2];
//    point3 = interestpoints[nr-3];
//
//    vector<InterestPoint> points = {point1, point2, point3};
//    InterestPoint pt1,pt2,pt3;
//    int distmin = -1;
//    for (int i = 0; i < 3; ++i) {
//        coord pct1 = points[i].getPunct();
//        for (int j = 0; j < 3; ++j) {
//            coord pct2 = points[j].getPunct();
//            int dist = 0;
//            dist += sqrt(pow((pct1.x-pct2.x),2)+ pow((pct1.y-pct2.y),2));
//            int disttemp = dist;
//            for (int k = 0; k < 3; ++k) {
//                coord pct3 = points[k].getPunct();
//                dist += sqrt(pow((pct2.x-pct3.x),2)+ pow((pct2.y-pct3.y),2));
//                if(distmin == -1 and i != k and i != j and j != k){
//                    distmin = dist;
//                    pt1 = points[i];
//                    pt2 = points[j];
//                    pt3 = points[k];
//                }
//                else{
//                    if (distmin > dist and i != j and j != k and i != k){
//                        distmin = dist;
//                        pt1 = points[i];
//                        pt2 = points[j];
//                        pt3 = points[k];
//                    }
//                dist = disttemp;
//                }
//            }
//        }
//    }
//
//    cout << "Cel mai scurt traseu intre cele mai populare 3 puncte are lungimea de: "<<distmin<<"\n";
//
//    return 0;
//}
//
///*
//Traseu#1
//Constanta
//5
//102  0 0
//404  10 10
//3    1 1
//22   3 2
//1001 5 0
//*/
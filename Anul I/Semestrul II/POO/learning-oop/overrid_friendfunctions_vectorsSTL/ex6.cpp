//#include <bits/stdc++.h>
//
//using namespace std;
//
//class Coords {
//    int x{}, y{};
//public:
//
//    Coords() : x(-1), y(-1) {}
//
//    Coords(int x, int y) : x(x), y(y) {}
//
//    friend istream &operator>>(istream &is, Coords &coords);
//
//    friend ostream &operator<<(ostream &os, Coords &coords);
//
//    bool operator==(Coords &x) {
//        return (this->x == x.x && this->y == x.y);
//    }
//
//    int getX() {
//        return x;
//    }
//
//    int getY() {
//        return y;
//    }
//
//    Coords& operator=(Coords noua){
//        this -> x = noua.getX();
//        this -> y = noua.getY();
//        return *this;
//    }
//};
//
//bool valid(Coords coordonate, int n){
//    return 0<=coordonate.getX() and coordonate.getX()<n and 0 <= coordonate.getY() and coordonate.getY()<n;
//}
//
//class Queue {
//    vector<Coords> coordonate;
//public:
//
//
//    Queue(const vector<Coords> &coordonate) : coordonate(coordonate) {}
//
//    Queue(){}
//
////    Queue(vector<Coords> coordonate) : coordonate(coordonate) {}
//
//    friend istream &operator>>(istream &is, Queue &queue);
//
//    friend ostream &operator<<(ostream &os, Queue &queue);
//
//    void clear() {
//        coordonate.clear();
//    }
//
//    bool isEmpty() {
//        return coordonate.empty();
//    }
//
//    vector<Coords> getCoordonate() {
//        return coordonate;
//    }
//
//    Coords operator[](int i) {
//        if (i < coordonate.size() and i>=0) {
//            return coordonate[i];
//        } else {
//            cout << "Nu exista element pe indicele " << i << '\n';
//            return {-1,-1};
//        }
//    }
//
//    Queue operator+=(Coords noua) {
//        coordonate.push_back(noua);
//        return *this;
//    }
//
//    friend Queue operator--(Queue &queue);
//};
//
//Queue operator--(Queue &queue){
//    if(queue.isEmpty()){
//        return queue;
//    }else{
//        vector<Coords> v;
//        for (int i = 1; i < queue.coordonate.size(); ++i) {
//            v.push_back(queue.coordonate[i]);
//        }
//        queue.coordonate = v;
//        return queue;
//    }
//
//}
//
//class Maze {
//    vector<vector<int>> matrix;
//    Coords start, end;
//public:
//
//    Maze() : matrix(0), start(-1, -1), end(-1, -1) {}
//
//    Maze(vector<vector<int>> matrix, Coords start, Coords end) : matrix(matrix), start(start), end(end) {}
//
//    friend istream &operator>>(istream &is, Maze &maze);
//
//    friend ostream &operator<<(ostream &os, Maze &maze);
//
///*
// 5
// 0
// 0
// 4
// 0
// 5
// 1
// 0
// 1
// 2
// 2
// 2
// 3
// 2
// 4
// 1
// */
//    void fill() {
//        int lung = matrix[0].size();
//        vector<int> linemodified(lung, 0);
//        vector<vector<int>> modified(lung, linemodified);
//        vector<vector<int>> roads(lung,linemodified);
//        modified[start.getY()][start.getX()] = 1;
//        roads[start.getY()][start.getX()]=1;
//        Queue queue;
//        matrix[start.getY()][start.getX()] = 0;
//        queue += start;
//        matrix[end.getY()][end.getX()] = 1;
//        Coords curent;
//        while (!queue.isEmpty()) {
//            curent = queue[0];
//            --queue;
//
//            if (valid(Coords(curent.getX(),curent.getY()+1),lung) and modified[curent.getY() + 1][curent.getX()] != 1 and matrix[curent.getY() + 1][curent.getX()] == 1) {
//                queue += Coords(curent.getX(), curent.getY()+1);
//                modified[curent.getY() + 1][curent.getX()] = 1;
//                matrix[curent.getY()+1][curent.getX()] += matrix[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX(),curent.getY()-1),lung) and modified[curent.getY() - 1][curent.getX()] != 1 and matrix[curent.getY() - 1][curent.getX()] == 1) {
//                queue += Coords(curent.getX() , curent.getY()-1);
//                modified[curent.getY() - 1][curent.getX()] = 1;
//                matrix[curent.getY()-1][curent.getX()] += matrix[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX()+1,curent.getY()),lung) and modified[curent.getY()][curent.getX() + 1] != 1 and matrix[curent.getY()][curent.getX() + 1] == 1) {
//                queue += Coords(curent.getX() + 1, curent.getY());
//                modified[curent.getY()][curent.getX() + 1] = 1;
//                matrix[curent.getY()][curent.getX() + 1] += matrix[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX()-1,curent.getY()),lung) and modified[curent.getY()][curent.getX() - 1] != 1 and matrix[curent.getY()][curent.getX() - 1] == 1) {
//                queue += Coords(curent.getX() - 1, curent.getX());
//                modified[curent.getY()][curent.getX() - 1] = 1;
//                matrix[curent.getY()][curent.getX() - 1] += matrix[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX(),curent.getY()+1),lung)){
//                roads[curent.getY()+1][curent.getX()]+=roads[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX(),curent.getY()-1),lung)){
//                roads[curent.getY()-1][curent.getX()]+=roads[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX()+1,curent.getY()),lung)){
//                roads[curent.getY()][curent.getX()+1]+=roads[curent.getY()][curent.getX()];
//            }
//
//            if (valid(Coords(curent.getX()-1,curent.getY()),lung)){
//                roads[curent.getY()][curent.getX()-1]+=roads[curent.getY()][curent.getX()];
//            }
//
//        }
//        int lungimea = matrix[end.getY()][end.getX()];
//        matrix[start.getY()][start.getX()] = 115;
//        matrix[end.getY()][end.getX()] = 101;
//        for (int i = 0; i < lung; ++i) {
//            for (int j = 0; j < lung; ++j) {
//                if (matrix[i][j] == 115) {
//                    cout << 's' << " ";
//                } else if (matrix[i][j] == 101) {
//                    cout << 'e' << " ";
//                } else cout << matrix[i][j] << " ";
//            }
//            cout << '\n';
//        }
//        cout << "Lungimea minima este "<<lungimea<<" si avem "<<roads[end.getY()][end.getX()]<<" drumuri de lungime "<<lungimea<<".\n";
//    }
//
//
//};
//
//istream &operator>>(istream &is, Maze &maze) {
//    int n;
//    cout << "Dimensiune matrix: ";
//    cin >> n;
//    cout << "Start: ";
//    is >> maze.start;
//    cout << "\n";
//    cout << "End: ";
//    is >> maze.end;
//    cout << '\n';
//    Queue queue;
//    cin >> queue;
//    vector<Coords> coordonate;
//    vector<int> v(n, 1);
//    coordonate = queue.getCoordonate();
//    for (int i = 0; i < n; ++i) {
//        maze.matrix.push_back(v);
//        for (int j = 0; j < n; ++j) {
//            Coords curent(j, i);
//            for (auto coordonata: coordonate) {
//                if (coordonata == curent) {
//                    maze.matrix[i][j] = 0;
//                }
//                if (curent == maze.start) {
//                    maze.matrix[i][j] = 's';
//                }
//                if (curent == maze.end) {
//                    maze.matrix[i][j] = 'e';
//                }
//            }
//        }
//    }
//    return is;
//}
//
//ostream &operator<<(ostream &os, Maze &maze) {
//    os << "Start: " << maze.start << '\n';
//    os << "End: " << maze.end << '\n';
//    for (auto linie: maze.matrix) {
//        for (auto column: linie) {
//            if (column == 115) {
//                os << 's' << " ";
//            } else if (column == 101) {
//                os << 'e' << " ";
//            } else os << column << " ";
//        }
//        os << '\n';
//    }
//}
//
//istream &operator>>(istream &is, Coords &coords) {
//    cout << "Coordonate: \n" << "x: ";
//    is >> coords.x;
//    cout << '\n';
//    cout << "y: ";
//    is >> coords.y;
//    cout << '\n';
//}
//
//ostream &operator<<(ostream &os, Coords &coords) {
//    os << "Coordonate: \n" << "x: " << coords.x << '\n' << "y:" << coords.y << '\n';
//}
//
//istream &operator>>(istream &is, Queue &queue) {
//    queue.coordonate.empty();
//    Coords coords;
//    cout << "Numarul obstacolelor: ";
//    int n;
//    cin >> n;
//    for (int i = 0; i < n; ++i) {
//        cout << "Obstacolul " << i + 1 << ": ";
//        cin >> coords;
//        cout << '\n';
//        queue.coordonate.push_back({coords});
//    }
//}
//
//ostream &operator<<(ostream &os, Queue &queue) {
//    cout << "Obstacolele sunt urmatoarele: \n";
//    int i = 1;
//    for (auto coords: queue.coordonate) {
//        cout << "Obstacolul " << i++ << ": \n";
//        cout << coords << '\n';
//    }
//}
//
//
//int main() {
//    Maze maze;
//    cin >> maze;
//    cout << maze;
//    cout<<'\n';
//    maze.fill();
//
//    return 0;
//}
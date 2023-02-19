#include <bits/stdc++.h>

using namespace std;

ifstream in("algsort.in");
ofstream out("algsort.out");

void merge(vector<int> &v, int const left, int const mid, int const right) {
    int sub1 = mid - left + 1;
    int sub2 = right - mid;

    int *leftv = new int[sub1], *rightv = new int[sub2];
    for (auto i = 0; i < sub1; i++)
        leftv[i] = v[left + i];
    for (auto j = 0; j < sub2; j++)
        rightv[j] = v[mid + 1 + j];

    auto indexv1 = 0, indexv2 = 0;
    int indexmerged = left;
    while (indexv1 < sub1 && indexv2 < sub2) {
        if (leftv[indexv1] <= rightv[indexv2]) {
            v[indexmerged] = leftv[indexv1];
            indexv1++;
        } else {
            v[indexmerged] = rightv[indexv2];
            indexv2++;
        }
        indexmerged++;
    }
    while (indexv1 < sub1) {
        v[indexmerged] = leftv[indexv1];
        indexv1++;
        indexmerged++;
    }
    while (indexv2 < sub2) {
        v[indexmerged] = rightv[indexv2];
        indexv2++;
        indexmerged++;
    }
}

void mergeSort(vector<int> &v, int const begin, int const end) {
    if (begin >= end)
        return;

    int mid = begin + (end - begin) / 2;
    mergeSort(v, begin, mid);
    mergeSort(v, mid + 1, end);
    merge(v, begin, mid, end);
}

int main() {
    vector<int> v;
    int n;
    in >> n;
    int x;
    for (int i = 0; i < n; ++i) {
        in >> x;
        v.push_back(x);
    }

    mergeSort(v, 0, v.size()-1);

    for (auto i = 0; i < v.size(); i++)
        out << v[i] << " ";

    return 0;
}

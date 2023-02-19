"""
Pentru rezolvarea acestei probleme am folosit structura UnionFind. La parsarea initiala a datelor, am creat
Un dictionar in care am mapat fiecare email la un index, index care reprezinta numele unui utilizator, la fiecare email
din datele date verificam daca acesta exista deja in dictionar, daca da efectuam o operatie de union intre indexul
utilizatorului curent si indexul utilizatorului asociat emailului curent. La final parsam dictionarul creat si
pentru fiecare email il adaugam unei noi liste numita res la indexul parintelui corespunzator gasit folosind find.

Complexitatea algoritmului este: O(n*m), unde n - numarul de utilizatori, m - numarul de emailuri
"""


from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parinte = [x for x in range(n + 1)]

    def find(self, x):
        if x == self.parinte[x]:
            return x
        self.parinte[x] = self.find(self.parinte[x])
        return self.parinte[x]

    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        if x == y:
            return
        self.parinte[y] = x


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_map = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_map:
                    uf.union(i, email_map[email])
                email_map[email] = i

        res = defaultdict(list)
        for email, owner in email_map.items():
            res[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in res.items()]


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    print(Solution().accountsMerge(accounts))

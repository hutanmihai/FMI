"""
Pentru rezolvarea acestei probleme am folosit dfs, diferenta fata de implementarea obisnuita fiind faptul ca
fiecare intrare in dfs se face dintr-un nod al carui numar de vecini nevizitati este 0, acest
lucru ne garanteaza ca nodul din care plecam mereu cu urmatorul dfs nu mai are cursuri ce trebuie facute inainte.
La fiecare intrare in dfs adaugam unei liste finale nodul curent, aceasta lista va reprezenta ordinea in care
cursurile trebuiesc urmate. Daca lungimea acestei liste nu este egala cu numarul de cursuri din input inseamna
ca la un moment dat nu a mai existat niciun nod cu numarul de vecini nevizitati deci prin urmare a ramas un nod
ne vizitat, implicit neadaugat in lista.
Complexitate: O(n+m)
"""

from typing import List, Dict


# ----------------------- SUBPUNCTUL A -----------------------
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def citire_lista_adiacenta(numCourses: int = numCourses, prerequisites: List[List[int]] = prerequisites) -> (
                Dict[int, List[int]], List[int]):
            nr_noduri = numCourses
            graph = {}
            nr_of_prereq = [0] * nr_noduri
            for i in range(nr_noduri):
                graph[i] = []
            for _ in prerequisites:
                x, y = int(_[1]), int(_[0])
                graph[x].append(y)
                nr_of_prereq[y] += 1
            return graph, nr_of_prereq

        graph, nr_of_prereq = citire_lista_adiacenta()
        rez = []

        def dfs_a(nod):
            rez.append(nod)
            nr_of_prereq[nod] -= 1
            for vecin in graph[nod]:
                nr_of_prereq[vecin] -= 1
                if nr_of_prereq[vecin] == 0:
                    dfs_a(vecin)

        def sub_a():
            for i in range(numCourses):
                if nr_of_prereq[i] == 0:
                    dfs_a(i)
            return rez if len(rez) == numCourses else []

        return sub_a()


# ----------------------- SUBPUNCTUL B -----------------------
"""
In acest subpunct rulam codul de la subpunctul a, iar in cazul imposibilitatii terminarii tuturor cursurilor
apelam noua functie numita circuit. Aceasta functie implementeaza algorimtul lui Hierholzer.
Complexitate totala: O(n+m)
Complexitate functia circuit: O(m)
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def citire_lista_adiacenta(numCourses: int = numCourses, prerequisites: List[List[int]] = prerequisites) -> (
                Dict[int, List[int]], List[int]):
            nr_noduri = numCourses
            graph = {}
            nr_of_prereq = [0] * nr_noduri
            for i in range(nr_noduri):
                graph[i] = []
            for _ in prerequisites:
                x, y = int(_[1]), int(_[0])
                graph[x].append(y)
                nr_of_prereq[y] += 1
            return graph, nr_of_prereq

        graph, nr_of_prereq = citire_lista_adiacenta()
        rez = []

        def dfs_a(nod):
            rez.append(nod)
            nr_of_prereq[nod] -= 1
            for vecin in graph[nod]:
                nr_of_prereq[vecin] -= 1
                if nr_of_prereq[vecin] == 0:
                    dfs_a(vecin)

        def sub_a():
            for i in range(numCourses):
                if nr_of_prereq[i] == 0:
                    dfs_a(i)
            return rez if len(rez) == numCourses else []

        stack = []
        drum_circuit = []
        nr_vecini = [0] * numCourses

        def circuit():
            for i in range(numCourses):
                # calculam nr de vecini ai fiecarui nod
                nr_vecini[i] = len(graph[i])
            # initializam stiva cu un nod oarecare
            stack.append(0)
            nod = 0
            while len(stack):
                if nr_vecini[nod] != 0:  # verificam daca mai sunt vecini nevizitati
                    stack.append(nod)
                    vecin = graph[nod].pop(-1)  # luam urmatorul nod si il stergem din lista de vecini a nodului curent
                    nr_vecini[nod] -= 1  # scadem nodul luat din numarul de vecini ai nodului curent
                    nod = vecin
                else:  # back-track pentru a afla circuitul
                    drum_circuit.append(nod)
                    nod = stack.pop(-1)
            drum_circuit.reverse()
            return drum_circuit

        if len(sub_a()) == 0:
            return circuit()
